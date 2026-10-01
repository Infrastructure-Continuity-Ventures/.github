#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/"commercial/service-catalog.json"
REQUIRED={
    "icv.governance-assessment.v1":"OFFERABLE_BOUNDED_SERVICE",
    "icv.admitted-code.v1":"OFFERABLE_ASSESSMENT_ONLY",
    "icv.stegcrm.v1":"OFFERABLE_MANAGED_PILOT",
}

def main():
    doc=json.loads(CATALOG.read_text(encoding="utf-8"))
    assert doc["schema_version"]=="icv.commercial-service-catalog.v1"
    assert doc["organization"]=="Infrastructure-Continuity-Ventures"
    assert doc["catalog_authority"]=="COMMERCIAL_DESCRIPTION_ONLY"
    assert doc["canonical_task_binding"] is None
    assert doc["cosv_task_vector"] is None
    offers=doc["offerings"]
    ids=[o["offering_id"] for o in offers]
    assert len(ids)==len(set(ids))
    observed={o["offering_id"]:o["commercial_status"] for o in offers}
    for oid,status in REQUIRED.items():
        assert observed.get(oid)==status
    for offer in offers:
        assert offer["source_refs"]
        assert offer["authority_boundary"]
        assert offer["included"]
        assert offer["excluded"]
    print("ICV_COMMERCIAL_SERVICE_CATALOG_VALID")

if __name__=="__main__":
    main()
