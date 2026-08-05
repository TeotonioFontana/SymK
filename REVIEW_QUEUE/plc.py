# -*- coding: utf-8 -*-
"""
Project-level PLC skeleton creation for symk-project-init.
"""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent
from typing import Dict, List

from .utils import write_file


def create_plc_structure(root: Path, project_name: str) -> None:
    """
    Create the project PLC skeleton under root/PLC.

    This is the *instance* PLC for this project (not the meta PLC template).
    It follows the agreed phase structure and drops a tiny README.md into
    each subfolder so the tree is visible and ready to be filled.
    """
    plc_root = root / "PLC"
    phases: Dict[str, List[str]] = {
        "1_Discovery": [
            "1.1_Product_Vision",
            "1.2_Market_Research",
            "1.3_Stakeholder_Map",
        ],
        "2_Architecture": [
            "2.1_System_Blueprints",
            "2.2_Reference_Stacks",
            "2.3_Security_Model",
        ],
        "3_Planning": [
            "3.1_Roadmap",
            "3.2_Release_Trains",
            "3.3_Scope_Definition",
        ],
        "4_Design": [
            "4.1_UX_Flows",
            "4.2_IA_Diagrams",
            "4.3_Design_System",
        ],
        "5_Development": [
            "5.1_Backend",
            "5.2_Frontend",
            "5.3_Infrastructure",
        ],
        "6_Testing": [
            "6.1_Test_Plans",
            "6.2_QA_Suites",
            "6.3_Security_Tests",
        ],
        "7_Deployment": [
            "7.1_Runtime_Configs",
            "7.2_CICD_Pipelines",
            "7.3_Observability",
        ],
        "8_Operations": [
            "8.1_SRE_Procedures",
            "8.2_Incident_Response",
            "8.3_Performance_Tuning",
        ],
        "9_GTM": [
            "9.1_Positioning",
            "9.2_Sales_Enablement",
            "9.3_Pricing",
        ],
        "10_Documentation": [
            "10.1_Technical_Docs",
            "10.2_User_Docs",
            "10.3_Release_Notes",
        ],
    }

    plc_root.mkdir(parents=True, exist_ok=True)

    # Root README for PLC
    write_file(
        plc_root / "README.md",
        dedent(
            f"""\
            # Product Lifecycle (PLC) — {project_name}

            This folder contains the *project-level* PLC instance for this product.
            Each phase folder groups the working artifacts for that phase.
            """
        ),
        force=False,
    )

    for phase, subfolders in phases.items():
        phase_dir = plc_root / phase
        phase_dir.mkdir(parents=True, exist_ok=True)

        # Simple phase README
        pretty_phase = phase.replace("_", " ")
        write_file(
            phase_dir / "README.md",
            dedent(
                f"""\
                # {pretty_phase}

                Project PLC phase for **{project_name}**.
                """
            ),
            force=False,
        )

        for sub in subfolders:
            sub_dir = phase_dir / sub
            sub_dir.mkdir(parents=True, exist_ok=True)
            pretty_sub = sub.replace("_", " ")
            write_file(
                sub_dir / "README.md",
                dedent(
                    f"""\
                    # {pretty_sub}

                    TODO: fill in for project **{project_name}**.
                    """
                ),
                force=False,
            )
