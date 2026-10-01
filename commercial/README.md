# ICV Commercial Service Catalog

This directory separates **customer-facing commercial packages** from the organization runtime service registry in `org-boundary/registry/services.json`.

The runtime registry answers: **where can an admitted organizational request be routed?**

This catalog answers: **what evidence-supported commercial posture may ICV describe for a product or service today?**

## Classification vocabulary

- `RELEASED_PRODUCT` — a product with direct current release evidence.
- `REVENUE_READY_SERVICE` — a bounded service with explicit commercial/delivery definition; not a claim of a released software product.
- `MANAGED_PILOT` — a bounded customer-facing capability suitable for managed pilot delivery while production/product conditions remain incomplete.
- `ASSESSMENT_ONLY` — customer-facing assessment or proof-of-concept whose production execution/authority boundary is not established.
- `DEVELOPMENT_PREVIEW` — implemented/source-demonstrated capability whose own evidence does not support production/released-product claims.
- `INTERNAL_SUBSTRATE` — materially built ecosystem infrastructure that is not presently represented as an independent customer-facing ICV offering.

## Current census

| Offering | Classification | Evidence-bounded reason |
| --- | --- | --- |
| Governance Assessment | REVENUE_READY_SERVICE | bounded ICV assessment plus revenue-grade governance validation source |
| Governance & AI Boundary Validation | REVENUE_READY_SERVICE | canonical source explicitly designates a revenue-grade product and commercial forms |
| Admitted Code | ASSESSMENT_ONLY | assessment/PoC is supportable; production admission authority/release is not |
| StegGate 0.3.0 | DEVELOPMENT_PREVIEW | current portable product source exists, but canonical handoff says v0.3.0 NOT YET RELEASED |
| StegCRM | MANAGED_PILOT | authority-free CRM projection is implemented; no standalone released SaaS claim |
| HydraSafe | REVENUE_READY_SERVICE | explicit commercial delivery environment, SOW/gap-assessment assets and bounded paid facility packet |
| GP10 Field Validation | REVENUE_READY_SERVICE | explicit revenue-ready paid field-validation offer |
| Governance Observatory 0.1.0 | RELEASED_PRODUCT | VERSION.json records RELEASED plus Git tag/GitHub Release evidence |
| KnowledgeVault / MyKV | MANAGED_PILOT | installable/file-based vault and bounded projections exist; provider/runtime transitions remain separately governed |
| StegTalk | DEVELOPMENT_PREVIEW | release verification says verified_non_production_local_prototype and production_ready=false |
| Ecosystem Chat | DEVELOPMENT_PREVIEW | source positioning is released, but live distributed execution/integrations are explicitly not implemented/proven |
| StegLearn | DEVELOPMENT_PREVIEW | product spec and materialized learning-loop source exist without evidence of a generally released platform |
| StegBusiness / StegBusiness-Ops | INTERNAL_SUBSTRATE | canonical internal business lifecycle/operations owner; no independent customer package is claimed |

## Evidence and authority rules

Every entry records `source_repository`, `source_product`, `version` when established, and `evidence_refs`. A classification is bounded by those sources. Source presence, CI, merge, a product specification, a public page, a local prototype, commercial readiness, and an actual product release are distinct facts.

A catalog entry grants no governance, credential, legal, operational, execution, publication, release, source-system, provider, customer, payment, or custody authority.

The catalog intentionally records `canonical_task_binding=null` and `cosv_task_vector=null` until canonical governance supplies an authentic binding.

## Validation

```bash
python commercial/validate_catalog.py
```

The validator requires the exact six-state classification vocabulary, the reconciled candidate set, unique offering IDs, source/product/evidence lineage, authority boundaries, customer-facing flags, and absence of an invented Task Registry/COSV binding.


## Release-hardening census

`release-hardening-census.json` records the observed release chain separately from commercial classification. It distinguishes service-only offerings from distributable software and prevents a current-main capability from being attributed to an older immutable release.

A software release chain is considered complete only when the applicable canonical owner establishes the required version/release predicates and the observed tag, GitHub Release, and packaged artifact agree. Missing release machinery is not a blocker for a service-only offering unless that service claims delivery of released software.
