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


## Counterpart-authority evidence hierarchy

`counterpart-authority-evidence.schema.json` defines `VERIFIED`, `UNRESOLVED` and `REJECTED` classifications for the separately satisfied `VERIFIED_COUNTERPART_AUTHORITY` predicate.

StegBusiness is the canonical business-state owner for counterparty/signature-authority/contract state; StegBusiness-Ops owns operational contract evidence and requires direct signed-contract evidence for execution. Google Contacts/directory capability exposes name, email, organization and title but no observed delegation/signature-authority field, so it is corroborative only.

Direct organization-attributable authorization/delegation is the strongest class. Applicable prior executed authority evidence may also verify authority when authentic, current and in scope. Organization-controlled role records and Contacts/directory data corroborate identity/role but cannot independently verify authority. Mailbox/domain/title/prior-correspondence evidence is context only.

No actual customer/contact/agreement lookup is permitted under this contract until an authentic acceptance event exists. Legal enforceability and signature sufficiency remain separate unresolved predicates unless independently evidenced.


## Contract-acceptance predicate separation

`contract-acceptance-predicates.schema.json` keeps four evidence predicates independent: `VERIFIED_COUNTERPART_AUTHORITY`, `VERIFIED_LEGAL_ENTITY_IDENTITY_CAPACITY`, `VERIFIED_SIGNATURE_SUFFICIENCY`, and `VERIFIED_LEGAL_ENFORCEABILITY`.

StegBusiness can represent canonical entity identity and contract/signature-authority state. StegBusiness-Ops can represent exact legal contracting entity, signature authority and direct signed-contract evidence in its contract lifecycle. Those owners are evidence sources, not a universal legal-enforceability oracle.

A signature artifact, `READY_FOR_SIGNATURE`, repository approval, StegBusiness contract state, or StegBusiness-Ops `EXECUTED` state cannot by itself establish legal enforceability. The enforceability predicate has no current canonical owner reference and remains `UNRESOLVED_UNLESS_INDEPENDENTLY_EVIDENCED`.

No actual customer, signature or agreement is queried until an authentic acceptance event exists.


## Acceptance evidence is not legal enforceability

The state semantics are intentionally distinct. `CONTRACT_OR_SOW_ACCEPTED` is a bounded commercial evidence disposition, not a finding that a contract is legally enforceable and not the StegBusiness-Ops `EXECUTED` lifecycle state.

The acceptance gate therefore requires `PURPORTED_ACCEPTANCE_OBSERVED`, `VERIFIED_COUNTERPART_AUTHORITY`, `VERIFIED_LEGAL_ENTITY_IDENTITY_CAPACITY` and `VERIFIED_SIGNATURE_SUFFICIENCY`. `VERIFIED_LEGAL_ENFORCEABILITY` remains a separate, non-gating predicate that may remain unresolved even after accepted terms are recorded.

StegBusiness-Ops `EXECUTED` remains separately governed and requires its own direct signed-contract evidence and applicable lifecycle controls.


## Post-acceptance state separation

`post-acceptance-state-machine.schema.json` replaces the former direct `CONTRACT_OR_SOW_ACCEPTED -> PAYMENT_EXECUTABLE_OR_OBSERVED` jump.

Accepted commercial terms do not imply StegBusiness-Ops `EXECUTED`, invoice issuance/readiness, payment, or service-delivery authorization. The bounded downstream states are `CONTRACT_LIFECYCLE_EXECUTED`, `INVOICE_OR_PAYMENT_TERMS_READY`, `PAYMENT_OBSERVED`, and `SERVICE_DELIVERY_AUTHORIZED`; each is independently `FAIL_CLOSED` until its authentic owner/evidence requirements are satisfied.

Payment is neither universally required nor universally sufficient for delivery authorization. Offering-specific start conditions remain controlling.


## Service-delivery admission evidence

`service-delivery-admission.schema.json` is the common evidence-only envelope for evaluating delivery prerequisites. `service-delivery-prerequisite-profiles.json` binds all twelve offerings without flattening their rules.

The envelope evaluates exact accepted scope, contract-lifecycle requirement, deposit/payment prerequisite, customer source/data authority, maturity/release ceiling, professional/regulatory/provider dependencies and an authentic delivery owner. Offering profiles resolve each prerequisite as required, not required by the package, or engagement-specific.

Passing the evidence envelope produces only `DELIVERY_ADMISSION_EVIDENCE_SATISFIED`; it does not itself produce `SERVICE_DELIVERY_AUTHORIZED`. That state remains fail-closed until an authentic offering-specific delivery owner separately admits it. No evaluation has been invoked.


## Delivery-owner reconciliation

`service-delivery-owner-reconciliation.json` traces the smallest existing repository/fulfillment owner for all twelve offerings. Existing owners and fulfillment surfaces were found, but no existing owner-controlled commercial delivery-admission interface was observed that can consume `DELIVERY_ADMISSION_EVIDENCE_SATISFIED` and independently return `ALLOW`, `DENY` or `FAIL_CLOSED` for `SERVICE_DELIVERY_AUTHORIZED`.

Product evaluators and fulfillment surfaces retain their native authority only. In particular, StegGate's governed disposition interface cannot be repurposed into ICV commercial service-start authority, CRM mutation APIs cannot become StegCRM delivery admission, and parent/steward learning review cannot become StegLearn commercial admission.

Accordingly all twelve offerings remain `FAIL_CLOSED` at their recorded existing-owner-interface predicate. No new interface is introduced.


## Accountable-owner service-start decision

The earlier requirement for an owner-controlled **machine** delivery-admission interface was over-specified for bounded professional/service work. `service-delivery-owner-decision.schema.json` now defines the smaller evidence contract: after exact delivery-admission evidence is satisfied, an authentically identified accountable offering owner may record `ALLOW`, `DENY` or `FAIL_CLOSED` for the bounded commercial service start through attributable human evidence.

This is not a runtime permission. `SERVICE_DELIVERY_AUTHORIZED` authorizes only the bounded professional/service engagement described by the accepted scope. Consequential software execution, source write-back, provider invocation, credentials/custody, production transport/deployment and other runtime actions retain their separate native admission gates.

No current engagement was evaluated; current state remains `FAIL_CLOSED_NOT_EVALUATED`.


## Terminal commercial evidence path

`terminal-commercial-evidence-path.schema.json` separates authorization, actual work, deliverable transmission, customer acceptance, payment observation and engagement completion.

```text
SERVICE_DELIVERY_AUTHORIZED
  -> DELIVERY_BEGUN
  -> DELIVERABLE_DELIVERED
  -> CUSTOMER_DELIVERABLE_ACCEPTED

PAYMENT_OBSERVED                 [independent financial evidence]
ENGAGEMENT_COMPLETE              [exact engagement-completion evidence]
```

None of these states is automatically transitive. Authorization is not proof work began; delivery is not customer acceptance; customer acceptance is not payment; payment is not revenue recognition; and engagement completion is not automatically StegBusiness-Ops contract `COMPLETE` or a legal discharge.

Revenue recognition remains a separate accounting-basis determination under StegBusiness/StegBusiness-Ops finance records.


## Engagement closure

`engagement-closure.schema.json` makes ICV engagement closure independent of StegBusiness-Ops contract lifecycle and accounting close. It supports exactly four dispositions:

- `COMPLETE`
- `COMPLETE_WITH_SUCCESSOR_OBLIGATION`
- `TERMINATED`
- `FAIL_CLOSED`

`engagement-closure-profiles.json` preserves the twelve offerings' possible surviving obligations, including support, retention/deletion, publication/reference rights, correction periods, professional-review follow-up, renewal/extension and separately scoped future integration/licensing.

Payment, deliverable acceptance, contract expiry, contract `COMPLETE`, accounting-period close and repository closure are not substitutes for ICV engagement closure.


## Successor-obligation handoff

`successor-obligation-handoff.schema.json` classifies every obligation surviving `COMPLETE_WITH_SUCCESSOR_OBLIGATION` without creating new commercial authority:

- `ORIGINAL_ACCEPTED_TERMS_CONTINUATION`
- `AMENDMENT_OR_RENEWAL_REQUIRED`
- `SEPARATE_SUCCESSOR_ENGAGEMENT_REQUIRED`
- `FAIL_CLOSED_UNCLASSIFIED`

Original-terms continuation is permitted only when the exact accepted proposal/SOW already fixes the obligation, owner, scope and applicable term/trigger without material modification. Material changes/extensions route to the existing StegBusiness-Ops amendment/renewal lifecycle. Separately quoted, separately governed or out-of-scope work requires a separately accepted successor engagement.

Every handoff has `work_authorization_state=NOT_AUTHORIZED` by default. Recording or classifying an obligation never starts successor work, and the source engagement remains historically `COMPLETE_WITH_SUCCESSOR_OBLIGATION`.


## Original-terms continuing obligations

`original-terms-continuing-obligation.schema.json` tracks only obligations classified `ORIGINAL_ACCEPTED_TERMS_CONTINUATION` after the source engagement has closed. The closed engagement remains immutable.

Lifecycle evidence states are `PENDING_TRIGGER`, `DUE`, `IN_PROGRESS`, `SATISFIED`, `WAIVED`, `BREACHED_OR_UNSATISFIED`, and `FAIL_CLOSED`.

A trigger becoming due does not authorize consequential work. `IN_PROGRESS` requires separate applicable work/runtime/data/provider/credential/custody authorization where the duty requires such action. `BREACHED_OR_UNSATISFIED` is an evidence classification only, not a legal breach, damages, default, enforceability or remedy conclusion.

The offering profiles identify candidate continuing-duty types, but package text alone never creates a duty; the exact accepted proposal/SOW/version must contain it.


## Continuing-obligation resolution receipts

`continuing-obligation-resolution-receipt.schema.json` makes `SATISFIED`, `WAIVED`, and `BREACHED_OR_UNSATISFIED` append-only resolution events. Each receipt binds the exact obligation and source coordinates, predecessor state/observation, triggering evidence, resolution actor and applicable authority evidence, timestamp, resulting state and retained evidence references. `supersedes_prior_history` must be false.

A later cure does not rewrite a prior `BREACHED_OR_UNSATISFIED` observation. It appends `CURE_SATISFIED` or `CURE_WAIVED` referencing the immutable prior unsatisfied receipt plus the new cure evidence. A current projection may say `SATISFIED_AFTER_CURE` or `WAIVED_AFTER_UNSATISFIED`, while reconstruction retains the complete ordered history.


## Continuing-obligation current-state projection

`continuing-obligation-current-state-projection.schema.json` derives current state from the append-only obligation history. It is a validated-history reduction, never a latest-receipt-wins rule.

Projection outputs are `PENDING_TRIGGER`, `DUE`, `IN_PROGRESS`, `SATISFIED`, `WAIVED`, `BREACHED_OR_UNSATISFIED`, `SATISFIED_AFTER_CURE`, `WAIVED_AFTER_UNSATISFIED`, and `FAIL_CLOSED`.

Every observation/receipt must independently satisfy its evidence, actor/authority, source-binding and state predicates and must form an allowed predecessor-linked transition. Timestamps/order sequence already-valid evidence but cannot authenticate or authorize it. A current state is returned only when there is one unambiguous valid frontier.

Contradictory frontiers, non-equivalent duplicates, stale predecessor links, broken/cyclic lineage, unauthorized observations, invalid cure ancestry or unresolved evidence produce `FAIL_CLOSED`. All records—including excluded invalid/stale/contradictory records—remain reconstructable with their validation failure.


## Continuing-obligation reconstruction manifest

`continuing-obligation-reconstruction-manifest.schema.json` makes every derived current state independently reconstructable from its complete evidence set. The manifest binds source closure/handoff/engagement/proposal/version identities; enumerates every lifecycle observation, resolution receipt and cure receipt; retains evidence/authority references; assigns each record a validation disposition/reason; records the valid lineage and frontier derivation; and emits the final projected state.

No rejected record may be silently omitted. `FAIL_CLOSED` must be reconstructed with the same fidelity as a substantive state by preserving the exact contradiction, duplicate, stale, unauthorized, broken-lineage or evidence reason that prevented a unique authentic frontier.

The manifest is reconstruction evidence only. Hashing, signing, storing, publishing or validating it cannot repair invalid source evidence or create commercial, contract/legal, work, runtime, Task Registry or COSV authority.
