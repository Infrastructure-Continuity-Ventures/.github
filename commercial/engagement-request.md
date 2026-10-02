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
