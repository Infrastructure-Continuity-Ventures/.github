# ICV Scoped Engagement Proposal / SOW Envelope

This is the common **proposal envelope** for all twelve customer-facing ICV offerings. It is not itself a signed contract, electronic-signature mechanism, payment instrument, legal-entity assertion, runtime activation, CRM record, Task Registry record or COSV binding.

The machine-readable contract is `commercial/scoped-engagement-proposal.schema.json`.

## Proposal identity

- proposal_id:
- proposal_version:
- engagement_id:
- offering_id:
- offering package / transaction-boundary reference:
- customer organization:
- customer contact as supplied:
- proposal issuer:
- issued at:
- valid until, or explicit NONE:

## Offering posture

- maturity classification:
- canonical source authority:
- unreleased / unproven substrate boundary:

These values must agree with the current ICV catalog and the offering-specific transaction package. The envelope cannot upgrade maturity or source authority.

## Objective and bounded scope

- requested outcome / objective:
- exact in-scope systems, facility, dataset, workflow or scenario:
- explicit out-of-scope boundary:

## Deliverables and exclusions

List the exact selected deliverables from, or consistent with, the offering package.

List all applicable offering-specific exclusions. Do not remove an exclusion merely because the customer requests a broader outcome.

## Customer responsibilities

Record authorized source provision, factual-review duties, professional/external dependencies, privacy/security obligations and any offering-specific prerequisites.

## Evidence / receipt expectations

State the source/provenance, disposition, delivery and reconstruction evidence expected for the engagement. Private provider identifiers and customer content remain private unless separately authorized.

## Commercial terms

- pricing disposition: FIXED_FEE / FEE_RANGE / COST_PLUS / SCOPE_BEFORE_PRICE / NO_FEE_RESEARCH_COLLABORATION / OTHER_EXPLICIT_WRITTEN_TERMS
- fee or range, if applicable:
- deposit / milestone semantics, if applicable:
- external professional / pass-through treatment, if applicable:
- target schedule:
- review period:
- retention / IP / publication / support terms, if applicable:
- change-order / stop-work conditions:

Offering-specific semantics control. For example, HydraSafe may include deposit/milestone and separately governed professional-review terms; GP10 requires exact written scope and fee/cost-plus terms before accepting payment. A blank field does not silently become zero, included, waived or not applicable.

## Acceptance instructions

State the requested method by which the customer should communicate acceptance or corrections for this exact proposal. These instructions **do not determine legal sufficiency or counterpart authority**.

Until separately observed and validated:

```text
SCOPED_ENGAGEMENT_PROPOSED = proposal may be delivered with evidence
CONTRACT_OR_SOW_ACCEPTED = FAIL_CLOSED
PAYMENT_OR_CONTRACT_EXECUTION_READY = false
NO_PAYMENT_EXECUTION_PATH = true
```

Acceptance requires separate authentic evidence attributable to an authorized customer counterpart, bound to the exact `proposal_id` and `proposal_version`, with applicable legal-entity/signature/professional requirements resolved. Proposal delivery, an email open, a generic reply, GitHub reaction, CRM state or payment intent is not sufficient by itself.

## Authority boundary

Creating or delivering this proposal does not create a Lead, Deal, probability, qualification, buyer record, electronic signature, contract authority, payment credential, payment execution, release/runtime activation, source-system write-back, Task Registry authority or COSV authority.
