# Change Log — `symk.semantic.document`

## 0.1.0-proposed

- Created a noncanonical semantic-package scaffold.
- Added candidate definitions for Document, DocumentType, and
  `symk.document.classified_as_type`.
- Added a bounded machine-semantic projection and explicit alignment record.
- Added illustrative valid assertions and counterexamples.
- Added the candidate `symk.document.core_properties` applicability profile in
  aligned human-semantic and machine-semantic forms.
- Distinguished Property Definition, Property Applicability Profile, and
  Property Assertion explicitly.
- Added an explicit dependency on `symk.semantic.property`.
- Moved the human `classified_as_type` definition into `definitions/properties/`
  and extracted its structured projection into `semantics/properties/`.
- Reduced the Document profile to applicability membership and profile-level
  constraints rather than implicit property semantics.
- Preserved unresolved package, versioning, authority, domain-import, and
  lowering questions for SymK 2.5–2.9.
