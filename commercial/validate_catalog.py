#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/"commercial/service-catalog.json"
PURCHASE=ROOT/"commercial/customer-purchase-path-census.json"
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
    print("ICV_CUSTOMER_PURCHASE_PATH_CENSUS_V1_VALID")

if __name__=="__main__":
    main()
