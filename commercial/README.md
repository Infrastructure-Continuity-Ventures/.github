# ICV Commercial Service Catalog

This directory separates **commercial packages** from the organization runtime service registry in `org-boundary/registry/services.json`.

The runtime registry answers: **where can an admitted organizational request be routed?**

This catalog answers: **what bounded commercial outcome may ICV offer a customer?**

They are intentionally different.

## Initial packages

- **Governance Assessment** — offerable now as a bounded professional service.
- **Admitted Code** — offerable now as an assessment/proof-of-concept; current source candidates are not represented as a released production admission runtime.
- **StegCRM** — offerable now as a managed pilot/assessment using the authority-free CRM projection already proven in StegOps; it is not represented as a standalone released SaaS product.

## Commercial state is not execution authority

A catalog entry may describe an offer without granting governance, credential, legal, operational, execution, publication, release, or source-system authority.

Each customer engagement must separately bind the customer, scope, applicable source authorities, deliverables, evidence requirements, and any governed execution path. Where canonical StegVerse task/COSV admission is required, that admission remains separate from this catalog.

The catalog intentionally records `canonical_task_binding=null` and `cosv_task_vector=null` until canonical governance supplies an authentic binding.

## Validation

```bash
python commercial/validate_catalog.py
```

The validator checks the fixed catalog identity, unique offering IDs, the three initial packages, permitted commercial statuses, explicit authority boundaries, and the absence of an invented task/COSV binding.
