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


## Customer purchase-path census

`customer-purchase-path-census.json` distinguishes three states that must not be collapsed:

1. `DOCUMENTED_TRANSACTION_READY` — scope, deliverables, exclusions, commercial terms, evidence and acceptance can be stated.
2. `PUBLICLY_DISCOVERABLE_AND_REQUESTABLE` — a prospective customer can find the offer and an offer-specific public request path is actually documented/observable.
3. `PAYMENT_OR_CONTRACT_EXECUTION_READY` — an authentic contract/payment execution path is established rather than merely described.

The current census finds all twelve customer-facing entries transaction-documented after bounded source repairs, but **none** has evidence for the full public-request plus contract/payment execution chain. Public repository presence alone is not a commercial intake endpoint.

`engagement-request.md` defines the minimum internal source-level intake contract for a quote/SOW request. It does not create a hosted/public form, payment credential, contract authority or customer request.


## Authentic engagement-request transition

The existing public mailto path terminates at an existing authenticated mailbox provider. `engagement-request-transition.json` defines the evidence boundary from public discovery to a scoped proposal without creating a new intake service or automatic CRM state.

An inbound message must first be authentically provider-observed. Only then may its bounded fields be normalized into `ENGAGEMENT_REQUEST_DOCUMENTED`. A scoped proposal/SOW is a separate state. Contract/SOW acceptance and payment remain fail-closed without their own authentic evidence.

StegOps Lead/Deal APIs are not the receiving seam: they create CRM state and must not be called merely because an inbound message exists.


## Common scoped-engagement proposal envelope

`scoped-engagement-proposal.schema.json` and `scoped-engagement-proposal.md` normalize the `SCOPED_ENGAGEMENT_PROPOSED` state across all twelve customer-facing offerings. The envelope references, rather than replaces, each offering's transaction package.

Existing HydraSafe, GP10 and StegOps SOW documents remain offering/source-specific. None is promoted to universal ICV authority: HydraSafe carries facility/professional/deposit semantics, GP10 requires scope-specific pricing before payment, and StegOps hard-codes audit tiers/modules and issue-based acceptance.

The common envelope cannot upgrade maturity, alter source authority, invent price, create electronic-signature sufficiency, or establish acceptance/payment. `CONTRACT_OR_SOW_ACCEPTED` remains `FAIL_CLOSED` until separate authentic acceptance attributable to an authorized customer counterpart is observed.


## Contract acceptance observation

`contract-acceptance-observation.schema.json` defines the bounded evidence contract for a customer's purported acceptance of an exact proposal. The authenticated mailbox provider can prove message receipt, provider-observed sender metadata and timestamp; it cannot by itself prove legal identity, organizational role, authority to bind the customer, signature sufficiency or enforceability.

The acceptance path therefore separates `PURPORTED_ACCEPTANCE_OBSERVED` from `VERIFIED_COUNTERPART_AUTHORITY`. The latter is a separately satisfied predicate requiring independently attributable organization-specific evidence. Email address, matching company domain, signature-block job title, prior correspondence, CRM state, proposal opening or payment intent are insufficient by themselves.

`CONTRACT_OR_SOW_ACCEPTED` remains `FAIL_CLOSED` until purported acceptance, verified counterpart authority and applicable legal/entity/signature/professional requirements are all separately satisfied.
