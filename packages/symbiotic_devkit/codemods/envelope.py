# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
===============================================================================
 envelope.py — Symbiotic result envelope & validation
===============================================================================
 Author.............: Teotoniio Fontana — Architect
 Programmed by......: Duke (GPT-5, OpenAI)
 Project............: SymK / Symbiotic DevKit
 Purpose............: Decorator enforcing input validation and a standard
                      return envelope for boundary functions.

 Contract
 --------
 Decorated functions should return a *payload dict* (your Rule #3 keeps per-key
 types static). The decorator wraps it into a standard envelope:

   {
     "ok": bool,
     "status": "success" | "invalid" | "error",
     "code": int,              # 200/422/500 by default
     "msg": str,               # optional
     "data": dict,             # payload from the function
     "errors": list,           # validation or contract errors
     "exception": {type, message, trace}?  # when status="error"
     "meta": {fn, ts, duration_ms, args}
   }

 Validation
 ---------
 Pass a per-parameter schema in the decorator:
   @enveloped(schema={
       "volume_id": {"type": str, "non_empty": True, "pattern": r"^vol-[0-9a-f]+$"},
       "limit":     {"type": int, "min": 1, "max": 1000, "required": False, "default": 100},
   })

 The decorator will:
   • bind args with defaults, then check each field;
   • check only parameters listed in the schema (unknown params are ignored);
   • never mutate your function’s signature or defaults.

 Parameters
 ----------
 enveloped(
   schema: dict[str, dict] = None,    # per-arg rules
   require_payload_dict: bool = True, # enforce payload type on success
   success_code: int = 200,
   invalid_code: int = 422,
   error_code: int = 500,
   include_trace: bool = False,       # attach traceback when exceptions occur
 )

 Notes
 -----
 • Valide pesado nas bordas; deixe helpers internos leves.
 • Se quiser validar o *shape* do payload também, acrescente depois um
   return_schema — mantido fora daqui para manter a borda enxuta.
===============================================================================
"""
# (resto do arquivo inalterado)

from __future__ import annotations
import functools, inspect, re, time, traceback
from datetime import datetime
from typing import Any, Callable, Dict, Optional

def _utc_iso() -> str: return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
def _type_name(t: Any) -> str:
    try: return t.__name__
    except Exception: return str(t)

def _check_one(name: str, value: Any, rules: Dict[str, Any]):
    required = rules.get("required", False); nullable = rules.get("nullable", False)
    if value is None:
        return (None if (not required or nullable) else f"'{name}' is required and cannot be None")
    expected = rules.get("type")
    if expected is not None and not isinstance(value, expected):
        return f"'{name}' expected type {_type_name(expected)}, got {type(value).__name__}"
    if isinstance(value, str):
        if rules.get("non_empty") and value == "": return f"'{name}' must be a non-empty string"
        pattern = rules.get("pattern")
        if pattern and not re.match(pattern, value): return f"'{name}' does not match pattern {pattern!r}"
    if isinstance(value, (int, float)):
        if "min" in rules and value < rules["min"]: return f"'{name}' must be >= {rules['min']}"
        if "max" in rules and value > rules["max"]: return f"'{name}' must be <= {rules['max']}"
    if "choices" in rules:
        try:
            if value not in rules["choices"]: return f"'{name}' must be one of {list(rules['choices'])!r}"
        except TypeError: return f"'{name}': invalid 'choices' iterable in schema"
    return None

def _bind_args(fn: Callable, *args, **kwargs) -> Dict[str, Any]:
    ba = inspect.signature(fn).bind_partial(*args, **kwargs); ba.apply_defaults(); return dict(ba.arguments)

def enveloped(*, schema: Optional[Dict[str, Dict[str, Any]]] = None, require_payload_dict: bool = True,
              success_code: int = 200, invalid_code: int = 422, error_code: int = 500, include_trace: bool = False):
    schema = schema or {}
    def _decorate(fn: Callable) -> Callable:
        @functools.wraps(fn)
        def _wrapper(*args, **kwargs) -> Dict[str, Any]:
            ts = _utc_iso(); t0 = time.perf_counter(); errors = []
            try: bound = _bind_args(fn, *args, **kwargs)
            except Exception as e:
                dur = int(1000 * (time.perf_counter() - t0))
                return {"ok": False, "status": "invalid", "code": invalid_code, "msg": "Invalid call: argument binding failed",
                        "data": {}, "errors": [str(e)], "exception": None,
                        "meta": {"fn": f"{fn.__module__}.{fn.__name__}", "ts": ts, "duration_ms": dur, "args": {}}}
            for pname, rules in schema.items():
                if pname not in bound and "default" in rules: bound[pname] = rules["default"]
            for pname, rules in schema.items():
                if pname not in bound:
                    if rules.get("required"): errors.append(f"'{pname}' is required")
                    continue
                err = _check_one(pname, bound[pname], rules)
                if err: errors.append(err)
            if errors:
                dur = int(1000 * (time.perf_counter() - t0))
                return {"ok": False, "status": "invalid", "code": invalid_code, "msg": "Input validation failed",
                        "data": {}, "errors": errors, "exception": None,
                        "meta": {"fn": f"{fn.__module__}.{fn.__name__}", "ts": ts, "duration_ms": dur, "args": bound}}
            try: payload = fn(**bound)
            except Exception as e:
                dur = int(1000 * (time.perf_counter() - t0))
                exc = {"type": type(e).__name__, "message": str(e)}
                if include_trace: exc["trace"] = traceback.format_exc()
                return {"ok": False, "status": "error", "code": error_code, "msg": "Unhandled exception during execution",
                        "data": {}, "errors": [], "exception": exc,
                        "meta": {"fn": f"{fn.__module__}.{fn.__name__}", "ts": ts, "duration_ms": dur, "args": bound}}
            if require_payload_dict and not isinstance(payload, dict):
                dur = int(1000 * (time.perf_counter() - t0))
                return {"ok": False, "status": "invalid", "code": invalid_code, "msg": "Function must return a dict payload",
                        "data": {}, "errors": [f"Invalid return type: {type(payload).__name__}"], "exception": None,
                        "meta": {"fn": f"{fn.__module__}.{fn.__name__}", "ts": ts, "duration_ms": dur, "args": bound}}
            dur = int(1000 * (time.perf_counter() - t0))
            return {"ok": True, "status": "success", "code": success_code, "msg": "",
                    "data": payload if isinstance(payload, dict) else {"value": payload},
                    "errors": [], "exception": None,
                    "meta": {"fn": f"{fn.__module__}.{fn.__name__}", "ts": ts, "duration_ms": dur, "args": bound}}
        return _wrapper
    return _decorate
