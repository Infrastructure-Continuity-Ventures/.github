# ICV Customer Engagement Request — Internal Commercial Intake Contract

This is the minimum source-level intake record for turning a catalog offering into a concrete quote/SOW request. It is not a hosted form, payment mechanism, executed contract, runtime admission, or evidence that a customer submitted a request.

## Required request fields
- offering_id
- customer / organization name
- accountable customer contact
- requested outcome
- bounded scope / system / facility / dataset
- source materials the customer is authorized to provide
- requested delivery mode
- timing constraints
- data-handling / confidentiality constraints
- acceptance owner
- known external professional or regulatory dependencies, if applicable

## Commercial response fields
- engagement_id
- exact deliverables
- exclusions
- customer responsibilities
- evidence / receipt expectations
- fixed fee, range, or scope-before-price disposition
- deposit / milestone terms when applicable
- target schedule
- review / acceptance period
- stop-work / change-order conditions
- source authority and unreleased/unproven substrate boundary

## State boundary
A completed intake record is only `ENGAGEMENT_REQUEST_DOCUMENTED`. A quote or SOW is separately authored and accepted. Payment is separately observed. Delivery and acceptance are separately evidenced. No state may be inferred from the existence of this template.

## Public-path boundary
This file is inside the ICV organization repository and does not establish public discoverability or a public submission endpoint. A future public contact/intake surface must be separately published and observed before any catalog entry is marked `PUBLICLY_DISCOVERABLE_AND_REQUESTABLE`.


## Existing receiving owner

The smallest existing receiving seam is the authenticated mailbox behind the published offer-specific `mailto:rigel@stegverse.org` links. This reuses an existing communication/provider evidence owner and does not create a hosted intake service.

An email link or a sent message is not an engagement. The first admissible inbound transition requires an **authenticated provider observation of an inbound message** whose offer-specific subject or content establishes an ICV engagement request.

The StegOps `POST /leads` and `POST /leads/{lead_id}/deals` APIs are explicitly **not** the receiving owner for this transition. Those APIs create CRM state, and the deal endpoint currently creates `stage=scoping` with `probability=50`; invoking them from mere inbound receipt would manufacture commercial state.

## Exact request transition

```text
PUBLICLY_DISCOVERABLE_AND_REQUESTABLE
  -> AUTHENTIC_ENGAGEMENT_REQUEST_OBSERVED
  -> ENGAGEMENT_REQUEST_DOCUMENTED
  -> SCOPED_ENGAGEMENT_PROPOSED
  -> CONTRACT_OR_SOW_ACCEPTED       [FAIL_CLOSED without separate acceptance evidence]
  -> PAYMENT_EXECUTABLE_OR_OBSERVED [FAIL_CLOSED; NO_PAYMENT_EXECUTION_PATH]
```

The machine-readable predicates are in `commercial/engagement-request-transition.json`.

Provider message/thread identifiers and message bodies remain private unless separately authorized for publication. Public evidence may retain only bounded state/disposition plus an authorized redacted/hash/locator reference.

No inbound request automatically creates a Lead, Deal, probability, qualification, contract, payment state, Task Registry record or COSV binding.
