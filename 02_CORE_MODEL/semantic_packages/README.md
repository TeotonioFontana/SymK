# Semantic Packages

**Status:** Proposed scaffold
**Normative effect:** None

## Package rule

A semantic package is a versioned, governed collection of related definitions
and their declared projections. The governed concept record and its decision
lineage carry semantic authority; no file format is authoritative merely by
being Markdown, YAML, JSON, an ontology, a schema, or executable code.

Every package must make the following recoverable:

- stable package and definition identifiers;
- owner, layer, jurisdiction, maturity status, and normative effect;
- human-semantic definitions, boundaries, examples, and counterexamples;
- machine-semantic claims and their declared expressive scope;
- alignment, omissions, strengthening, and known semantic loss;
- dependencies and specialization boundaries;
- decision and revision lineage; and
- downstream projection and implementation boundaries.

## File responsibilities

Each file has one primary responsibility. A file may refer to another artifact,
but it must not silently acquire that artifact's authority or purpose.

| Path | Primary responsibility | Must not be treated as |
|---|---|---|
| `manifest.yaml` | Declares package identity, version, ownership, status, jurisdiction, contents, dependencies, authority, and release state | The substantive definition of every concept in the package |
| `README.md` | Orients human readers, explains package purpose and boundaries, and provides navigation | An independent source of semantic or normative authority |
| `definitions/*.md` | Carries the human-semantic nucleus for each definition: meaning, scope, distinctions, rationale, examples, counterexamples, uncertainty, and open questions | A database schema, runtime record, or exhaustive formalization |
| `definitions/properties/*.md` | Carries the human-semantic nucleus of one subject-specific PropertyDefinition | A bearer profile, runtime assertion, or inline database field |
| `definitions/*-property-profile.md` | Explains the governed set of property definitions applicable to a bearer and distinguishes applicability from assertion presence | An inline class definition or collection of runtime values |
| `semantics/package.yaml` | Projects selected identities, types, relations, qualifiers, and constraints into a machine-inspectable form within declared scope | The complete meaning of the human-semantic definitions |
| `semantics/alignment.yaml` | Maps machine claims to human claims and records omissions, strengthening, mismatch, semantic loss, and verification evidence | A replacement for either semantic lane |
| `semantics/properties/*.yaml` | Projects one subject-specific PropertyDefinition and its declared conformance to the generic Property model | The human definition, applicability profile, or runtime assertion |
| `semantics/profiles/*.yaml` | Projects a property applicability profile, including its bearer, member references, applicability, and extension boundary | The definitions of its member properties or their runtime assertions |
| `examples/*.yaml` | Supplies positive, negative, and boundary fixtures that demonstrate intended use and expose category errors | Production data, domain authority, or a complete catalogue of every possible case |
| `CHANGELOG.md` | Preserves the package's revision narrative and compatibility-relevant changes | The decision record that authorizes a semantic change |

Additional files must declare their primary responsibility and authority role in
the package manifest. Generated files must identify their governed inputs and
must not be edited as independent sources.

## Source and generated artifacts

Human-semantic and machine-semantic files are coordinated expressions of one
governed subject. A generated representation must identify its source and must
not be edited as if it were an independent semantic authority.

The final rules for canonical inputs, deterministic generation, package hashes,
compatibility, and release immutability remain decisions for SymK 2.5 and 2.9.

## Ownership boundary

SymK packages contain only SymK-owned cross-project meaning. Derived projects
own their domain concepts and specialization criteria. A SymK package may refer
to a domain-owned concept through a governed reference; it must not copy that
concept and thereby imply ownership transfer.

Runtime assertions belong to project or neutral operational stores. Examples
inside a package are fixtures and have no production authority.

## Generic and subject-specific packages

Generic semantic machinery belongs in its own package. A subject-specific
package depends on that machinery and defines only its specialization.

For example, `symk.semantic.property` defines PropertyDefinition,
PropertyApplicabilityProfile, PropertyAssertion, and PropertyValue, while
`symk.semantic.document` defines Document properties and profiles that conform
to those generic meanings.
