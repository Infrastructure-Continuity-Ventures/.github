#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/"commercial/service-catalog.json"
PURCHASE=ROOT/"commercial/customer-purchase-path-census.json"
REQUEST_TRANSITION=ROOT/"commercial/engagement-request-transition.json"
PROPOSAL_ENVELOPE=ROOT/"commercial/scoped-engagement-proposal.schema.json"
ACCEPTANCE_OBSERVATION=ROOT/"commercial/contract-acceptance-observation.schema.json"
COUNTERPART_AUTHORITY=ROOT/"commercial/counterpart-authority-evidence.schema.json"
ACCEPTANCE_PREDICATES=ROOT/"commercial/contract-acceptance-predicates.schema.json"
CLASSES=[
    "RELEASED_PRODUCT","REVENUE_READY_SERVICE","MANAGED_PILOT",
    "ASSESSMENT_ONLY","DEVELOPMENT_PREVIEW","INTERNAL_SUBSTRATE",
]
REQUIRED={
    "icv.governance-assessment.v1":"REVENUE_READY_SERVICE",
    "icv.governance-boundary-validation.v1":"REVENUE_READY_SERVICE",
    "icv.admitted-code.v1":"ASSESSMENT_ONLY",
    "icv.steggate.v1":"DEVELOPMENT_PREVIEW",
    "icv.stegcrm.v1":"MANAGED_PILOT",
    "icv.hydrasafe.v1":"REVENUE_READY_SERVICE",
    "icv.gp10-field-validation.v1":"REVENUE_READY_SERVICE",
    "icv.governance-observatory.v1":"RELEASED_PRODUCT",
    "icv.knowledgevault.v1":"MANAGED_PILOT",
    "icv.stegtalk.v1":"DEVELOPMENT_PREVIEW",
    "icv.ecosystem-chat.v1":"DEVELOPMENT_PREVIEW",
    "icv.steglearn.v1":"DEVELOPMENT_PREVIEW",
    "icv.stegbusiness-ops.v1":"INTERNAL_SUBSTRATE",
}

def main():
    doc=json.loads(CATALOG.read_text(encoding="utf-8"))
    assert doc["schema_version"]=="icv.commercial-service-catalog.v2"
    assert doc["organization"]=="Infrastructure-Continuity-Ventures"
    assert doc["catalog_authority"]=="COMMERCIAL_DESCRIPTION_ONLY"
    assert doc["canonical_task_binding"] is None
    assert doc["cosv_task_vector"] is None
    assert doc["classification_vocabulary"]==CLASSES
    offers=doc["offerings"]
    ids=[o["offering_id"] for o in offers]
    assert len(ids)==len(set(ids))
    assert set(ids)==set(REQUIRED)
    for offer in offers:
        assert offer["classification"] in CLASSES
        assert offer["classification"]==REQUIRED[offer["offering_id"]]
        assert offer["source_repository"] and offer["source_product"]
        assert offer["evidence_refs"] and offer["delivery_modes"]
        assert offer["customer_outcome"] and offer["authority_boundary"]
        if offer["classification"]=="INTERNAL_SUBSTRATE":
            assert offer["customer_facing"] is False
        else:
            assert offer["customer_facing"] is True
    purchase=json.loads(PURCHASE.read_text(encoding="utf-8"))
    assert purchase["schema_version"]=="icv.customer-purchase-path-census.v1"
    assert purchase["canonical_task_binding"] is None
    assert purchase["cosv_task_vector"] is None
    pentries=purchase["entries"]
    customer_ids={o["offering_id"] for o in offers if o["customer_facing"]}
    assert {e["offering_id"] for e in pentries}==customer_ids
    for entry in pentries:
        assert entry["transaction_state"]=="DOCUMENTED_TRANSACTION_READY"
        assert entry["acceptance_state"] in {"DOCUMENTED","DOCUMENTED_AFTER_ICV_PACKAGE_REPAIR"}
        assert entry["publicly_discoverable_and_requestable"] is False
        assert entry["payment_or_contract_execution_ready"] is False
        assert entry["payment_state"]=="NO_AUTHENTIC_PAYMENT_EXECUTION_PATH_OBSERVED"
        assert entry["transaction_evidence"]
    print("ICV_COMMERCIAL_SERVICE_CATALOG_V2_VALID")
    transition=json.loads(REQUEST_TRANSITION.read_text(encoding="utf-8"))
    assert transition["schema_version"]=="icv.engagement-request-transition.v1"
    assert transition["canonical_task_binding"] is None
    assert transition["cosv_task_vector"] is None
    assert transition["receiving_owner"]["hosted_service_created"] is False
    assert transition["payment_or_contract_execution_ready"] is False
    assert any(x["to"]=="AUTHENTIC_ENGAGEMENT_REQUEST_OBSERVED" for x in transition["transitions"])
    assert any(x["to"]=="CONTRACT_OR_SOW_ACCEPTED" and x["disposition_on_current_evidence"]=="FAIL_CLOSED" for x in transition["transitions"])
    assert any(x["to"]=="PAYMENT_EXECUTABLE_OR_OBSERVED" and x["disposition_on_current_evidence"]=="FAIL_CLOSED" for x in transition["transitions"])
    assert "Lead/Deal creation is a later separately admitted action" in transition["crm_boundary"]
    print("ICV_CUSTOMER_PURCHASE_PATH_CENSUS_V1_VALID")
    envelope=json.loads(PROPOSAL_ENVELOPE.read_text(encoding="utf-8"))
    assert envelope["schema_version"]=="icv.scoped-engagement-proposal.v1"
    assert envelope["canonical_task_binding"] is None
    assert envelope["cosv_task_vector"] is None
    assert envelope["acceptance_boundary"]["current_disposition"]=="FAIL_CLOSED"
    assert envelope["acceptance_boundary"]["envelope_effect"]=="NONE"
    assert envelope["payment_boundary"]["payment_or_contract_execution_ready"] is False
    assert envelope["payment_boundary"]["payment_execution_path"]=="NONE"
    assert len(envelope["offering_specific_preservation"])==12
    required={"proposal_id","proposal_version","engagement_id","offering_id","offering_package_ref","maturity_classification","source_authority","deliverables","exclusions","pricing_disposition","acceptance_instructions","unreleased_unproven_substrate_boundary","proposal_delivery_evidence"}
    assert required.issubset(set(envelope["required_fields"]))
    assert transition["proposal_envelope"]["schema"]=="commercial/scoped-engagement-proposal.schema.json"
    assert transition["proposal_envelope"]["creates_acceptance_authority"] is False
    print("ICV_ENGAGEMENT_REQUEST_TRANSITION_V1_VALID")
    acceptance=json.loads(ACCEPTANCE_OBSERVATION.read_text(encoding="utf-8"))
    assert acceptance["schema_version"]=="icv.contract-acceptance-observation.v1"
    assert acceptance["canonical_task_binding"] is None
    assert acceptance["cosv_task_vector"] is None
    assert acceptance["provider_observation"]["owner"]=="authenticated mailbox provider"
    assert "authority to bind organization" in acceptance["provider_observation"]["does_not_prove"]
    assert acceptance["dispositions"]["verified_counterpart_authority"]["current_status"]=="SEPARATELY_SATISFIED_PREDICATE"
    assert acceptance["dispositions"]["verified_counterpart_authority"]["mailbox_provider_sufficient"] is False
    assert acceptance["dispositions"]["contract_or_sow_accepted"]["current_disposition"]=="FAIL_CLOSED"
    assert acceptance["dispositions"]["contract_or_sow_accepted"]["legal_enforceability_effect"]=="NONE"
    assert transition["transitions"][3]["counterpart_authority_predicate"]=="VERIFIED_COUNTERPART_AUTHORITY"
    assert transition["transitions"][3]["mailbox_provider_sufficient_for_counterpart_authority"] is False
    print("ICV_SCOPED_ENGAGEMENT_PROPOSAL_V1_VALID")
    authority=json.loads(COUNTERPART_AUTHORITY.read_text(encoding="utf-8"))
    assert authority["schema_version"]=="icv.counterpart-authority-evidence.v1"
    assert authority["canonical_task_binding"] is None
    assert authority["cosv_task_vector"] is None
    assert authority["dispositions"]==["VERIFIED","UNRESOLVED","REJECTED"]
    assert authority["owner_model"]["contact_directory"]["authority_fields_observed"]==[]
    assert authority["classification_rules"]["VERIFIED"]["effect"].startswith("Satisfies VERIFIED_COUNTERPART_AUTHORITY")
    assert authority["classification_rules"]["UNRESOLVED"]["effect"]=="CONTRACT_OR_SOW_ACCEPTED remains FAIL_CLOSED."
    assert authority["separate_predicates"]["legal_enforceability"]=="UNRESOLVED_UNLESS_INDEPENDENTLY_EVIDENCED"
    assert authority["separate_predicates"]["signature_sufficiency"]=="UNRESOLVED_UNLESS_INDEPENDENTLY_EVIDENCED"
    assert acceptance["counterpart_identity_evidence"]["authority_evidence_contract"]=="commercial/counterpart-authority-evidence.schema.json"
    assert acceptance["counterpart_identity_evidence"]["real_customer_query_gate"]=="AUTHENTIC_ACCEPTANCE_EVENT_EXISTS"
    print("ICV_CONTRACT_ACCEPTANCE_OBSERVATION_V1_VALID")
    predicates=json.loads(ACCEPTANCE_PREDICATES.read_text(encoding="utf-8"))
    assert predicates["schema_version"]=="icv.contract-acceptance-predicates.v1"
    assert predicates["canonical_task_binding"] is None
    assert predicates["cosv_task_vector"] is None
    expected={"VERIFIED_COUNTERPART_AUTHORITY","VERIFIED_LEGAL_ENTITY_IDENTITY_CAPACITY","VERIFIED_SIGNATURE_SUFFICIENCY","VERIFIED_LEGAL_ENFORCEABILITY"}
    assert set(predicates["predicates"])==expected
    assert predicates["predicates"]["VERIFIED_LEGAL_ENFORCEABILITY"]["owner_refs"]==[]
    assert predicates["predicates"]["VERIFIED_LEGAL_ENFORCEABILITY"]["current_status"]=="UNRESOLVED_UNLESS_INDEPENDENTLY_EVIDENCED"
    assert "signed artifact alone" in predicates["predicates"]["VERIFIED_LEGAL_ENFORCEABILITY"]["prohibited_shortcuts"]
    assert "StegBusiness-Ops EXECUTED state alone" in predicates["predicates"]["VERIFIED_LEGAL_ENFORCEABILITY"]["prohibited_shortcuts"]
    assert predicates["contract_or_sow_accepted_gate"]["current_disposition"]=="FAIL_CLOSED"
    assert predicates["contract_or_sow_accepted_gate"]["required_predicates"]==["PURPORTED_ACCEPTANCE_OBSERVED","VERIFIED_COUNTERPART_AUTHORITY","VERIFIED_LEGAL_ENTITY_IDENTITY_CAPACITY","VERIFIED_SIGNATURE_SUFFICIENCY"]
    assert predicates["contract_or_sow_accepted_gate"]["non_gating_separate_predicates"]==["VERIFIED_LEGAL_ENFORCEABILITY"]
    assert predicates["contract_or_sow_accepted_gate"]["legal_effect"]=="NONE"
    assert predicates["predicates"]["VERIFIED_LEGAL_ENFORCEABILITY"]["gating_for_contract_or_sow_accepted"] is False
    assert acceptance["dispositions"]["contract_or_sow_accepted"]["non_gating_separate_predicates"]==["VERIFIED_LEGAL_ENFORCEABILITY"]
    assert acceptance["dispositions"]["contract_or_sow_accepted"]["contract_execution_effect"]=="NONE"
    assert acceptance["dispositions"]["contract_or_sow_accepted"]["acceptance_predicates_contract"]=="commercial/contract-acceptance-predicates.schema.json"
    print("ICV_COUNTERPART_AUTHORITY_EVIDENCE_V1_VALID")
    print("ICV_CONTRACT_ACCEPTANCE_PREDICATES_V1_VALID")

if __name__=="__main__":
    main()
