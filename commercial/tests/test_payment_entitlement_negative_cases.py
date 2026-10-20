"""Offline payment/entitlement negative cases for the ICV commercial validator.

Ported from the offline reference cases described on StegVerse-Labs/.github#3183
(comments 6152906008, 6153079641 and 6153862803) into the repository that owns
the commercial records, as directed in StegVerse-org/.github#160 comment
6237909628 (workstream E). Only cases that map onto an existing record and an
existing ``commercial/validate_catalog.py`` guard are ported. The offline
reference guard itself is not ported: it is not an evaluator, and this module
adds none.

Each case copies the repository to a temporary directory, manufactures one
payment/entitlement readiness claim in the copied records, and requires the
existing validator to refuse it at the guard named in the case. A refusal is
evidence only: the validator grants no payment, entitlement, delivery or
governance authority, and an unmodified copy must validate.

Stdlib only (unittest, json, shutil, tempfile, importlib, traceback).
Run: python -m unittest discover -s commercial/tests -v
"""
import importlib.util
import json
import shutil
import tempfile
import traceback
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = Path("commercial/validate_catalog.py")
SIX_FIELDS = (
    "failure_code",
    "failed_predicate",
    "required_evidence_or_repair",
    "retry_entrypoint",
    "owning_existing_goal",
    "next_attempt",
)
RETRY = "python commercial/validate_catalog.py"
GOAL = "GITHUB-UNIVERSAL-GOVERNANCE-PRODUCT-001 (PROPOSED; not Registry-admitted; StegVerse-org/.github#160 6237909628)"
NEXT = "after the owner selects a payment provider and an authentic settlement path is owned"


def _refusal(code, predicate, repair):
    return {
        "disposition": "FAIL_CLOSED",
        "failure_code": code,
        "failed_predicate": predicate,
        "required_evidence_or_repair": repair,
        "retry_entrypoint": RETRY,
        "owning_existing_goal": GOAL,
        "next_attempt": NEXT,
    }


def _purchase_ready(r):
    r["commercial/customer-purchase-path-census.json"]["entries"][0]["payment_or_contract_execution_ready"] = True


def _purchase_settled(r):
    r["commercial/customer-purchase-path-census.json"]["entries"][0]["payment_state"] = "AUTHENTIC_PAYMENT_SETTLED"


def _transition_payment_allow(r):
    for step in r["commercial/engagement-request-transition.json"]["transitions"]:
        if step.get("to") == "PAYMENT_OBSERVED":
            step["disposition_on_current_evidence"] = "ALLOW"


def _mailbox_counterpart(r):
    r["commercial/engagement-request-transition.json"]["transitions"][3][
        "mailbox_provider_sufficient_for_counterpart_authority"] = True


def _contract_accepted(r):
    r["commercial/contract-acceptance-observation.schema.json"]["dispositions"][
        "contract_or_sow_accepted"]["current_disposition"] = "ALLOW"


def _post_payment_observed(r):
    r["commercial/post-acceptance-state-machine.schema.json"]["states"][
        "PAYMENT_OBSERVED"]["current_disposition"] = "ALLOW"


def _payment_path(r):
    r["commercial/post-acceptance-state-machine.schema.json"]["payment_execution_path"] = "PROVIDER_CHECKOUT"


def _delivery_authorized(r):
    r["commercial/service-delivery-admission.schema.json"]["disposition"]["service_delivery_authorized"] = "ALLOW"


def _terminal_payment_observed(r):
    r["commercial/terminal-commercial-evidence-path.schema.json"]["states"][
        "PAYMENT_OBSERVED"]["current_disposition"] = "ALLOW"


def _everything_consistent(r):
    for mutate in (_purchase_ready, _purchase_settled, _transition_payment_allow, _post_payment_observed,
                   _payment_path, _delivery_authorized, _terminal_payment_observed):
        mutate(r)


# (case id, mutation, validator guard substring, six-field refusal record, source)
CASES = (
    ("HE-01", _purchase_ready, 'assert entry["payment_or_contract_execution_ready"] is False',
     _refusal("PAYMENT_PROVIDER_NOT_DECIDED", "PAYMENT_PROVIDER_SELECTED_AND_SETTLEMENT_PATH_OWNED",
              "owner selects the payment provider and customer-authorized interface; no record may claim "
              "payment readiness before that (owner decision)"),
     "org#160 6237909628; Labs#3183 6153079641 (absent provider verification)"),
    ("HE-02", _purchase_settled, 'assert entry["payment_state"]=="NO_AUTHENTIC_PAYMENT_EXECUTION_PATH_OBSERVED"',
     _refusal("SETTLEMENT_NOT_AUTHENTICALLY_OBSERVED", "PROVIDER_SETTLEMENT_READBACK_VERIFIED",
              "authentic provider settlement readback bound to the purchase record; a stated settlement is not one"),
     "Labs#3183 6152906008 (missing/forged settlement)"),
    ("HE-03", _transition_payment_allow,
     'x["to"]=="PAYMENT_OBSERVED" and x["disposition_on_current_evidence"]=="FAIL_CLOSED"',
     _refusal("GOVERNANCE_RETURN_NOT_ALLOW", "CANONICAL_GOVERNANCE_RETURN_ALLOWS_PAYMENT_TRANSITION",
              "a canonical governance return for the payment transition; DENY or UNKNOWN never becomes ALLOW"),
     "Labs#3183 6153079641 (governance DENY/UNKNOWN)"),
    ("HE-04", _mailbox_counterpart,
     'assert transition["transitions"][3]["mailbox_provider_sufficient_for_counterpart_authority"] is False',
     _refusal("COUNTERPART_AUTHORITY_NOT_VERIFIED", "VERIFIED_COUNTERPART_AUTHORITY",
              "counterpart authority evidence per commercial/counterpart-authority-evidence.schema.json; "
              "a mailbox observation alone is insufficient"),
     "Labs#3183 6153079641 (missing counterpart/signature)"),
    ("HE-05", _contract_accepted,
     'assert acceptance["dispositions"]["contract_or_sow_accepted"]["current_disposition"]=="FAIL_CLOSED"',
     _refusal("CONTRACT_ACCEPTANCE_NOT_EVIDENCED", "CONTRACT_OR_SOW_ACCEPTED_PREDICATES_SATISFIED",
              "purported acceptance, counterpart authority, legal entity identity/capacity and signature "
              "sufficiency evidenced per commercial/contract-acceptance-predicates.schema.json"),
     "Labs#3183 6153079641 (missing counterpart/signature)"),
    ("HE-06", _post_payment_observed,
     'assert all(v["current_disposition"]=="FAIL_CLOSED" for k,v in post["states"].items() if k!="SERVICE_DELIVERY_AUTHORIZED")',
     _refusal("SOVEREIGN_READBACK_ABSENT", "PAYMENT_OBSERVED_HAS_PROVIDER_AND_SOVEREIGN_LEDGER_READBACK",
              "provider readback plus sovereign ledger / Master Records proof for the payment observation"),
     "Labs#3183 6153079641 (absent sovereign readback/Master Records proof)"),
    ("HE-07", _payment_path, 'assert post["payment_execution_path"]=="NONE"',
     _refusal("PAYMENT_PROVIDER_NOT_DECIDED", "PAYMENT_EXECUTION_PATH_OWNED_BY_A_DECIDED_PROVIDER",
              "owner decision on the payment provider; until then payment_execution_path stays NONE"),
     "Labs#3183 6152906008 (payment_execution_path == NONE); org#160 6237909628"),
    ("HE-08", _delivery_authorized,
     'assert delivery["disposition"]["service_delivery_authorized"]=="FAIL_CLOSED_NOT_EVALUATED"',
     _refusal("ENTITLEMENT_WITHOUT_SETTLEMENT", "SETTLED_PAYMENT_AND_OWNER_DECISION_PRECEDE_DELIVERY_OR_ENTITLEMENT",
              "manifest-bound authority, verified counterpart, provider settlement readback and the exact state "
              "predecessor before any entitlement/delivery ALLOW"),
     "Labs#3183 6152906008 (payment/entitlement ALLOW prerequisites)"),
    ("HE-09", _terminal_payment_observed,
     'assert all(x["current_disposition"]=="FAIL_CLOSED_NOT_OBSERVED" for k,x in terminal["states"].items() if k!="ENGAGEMENT_COMPLETE")',
     _refusal("PROVIDER_SETTLEMENT_READBACK_ABSENT", "TERMINAL_PAYMENT_OBSERVED_IS_AUTHENTICALLY_OBSERVED",
              "authentic provider observation for the terminal PAYMENT_OBSERVED state"),
     "Labs#3183 6153079641 (absent provider verification)"),
    ("HE-10", _everything_consistent, 'assert entry["payment_or_contract_execution_ready"] is False',
     _refusal("AUTHENTIC_PROVIDER_AND_LEDGER_READBACK_NOT_AVAILABLE", "AUTHENTIC_PROVIDER_AND_LEDGER_READBACK_PRESENT",
              "authenticated provider and ledger readback; locally consistent records claiming readiness never "
              "yield ALLOW"),
     "Labs#3183 6153862803 (all local predicates match is still FAIL_CLOSED)"),
)


def _copy_repo(dest: Path) -> Path:
    target = dest / "repo"
    shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns(".git", "__pycache__"))
    return target


def _run_validator(repo: Path):
    spec = importlib.util.spec_from_file_location("_icv_validate_catalog_under_test", repo / VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.main()


def _guard_line(repo: Path, guard: str) -> int:
    lines = (repo / VALIDATOR).read_text(encoding="utf-8").splitlines()
    hits = [n for n, text in enumerate(lines, 1) if guard in text]
    if not hits:
        raise AssertionError(f"guard not found in the validator: {guard!r}")
    return hits[0]  # the first occurrence is the one that refuses first


class PaymentEntitlementNegativeCases(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = _copy_repo(Path(self._tmp.name))

    def tearDown(self):
        self._tmp.cleanup()

    def _records(self, names):
        return {n: json.loads((self.repo / n).read_text(encoding="utf-8")) for n in names}

    def test_unmodified_records_validate(self):
        _run_validator(self.repo)

    def test_every_case_records_all_six_fields_as_fail_closed(self):
        ids = [case[0] for case in CASES]
        self.assertEqual(len(ids), len(set(ids)))
        for case_id, _, _, refusal, source in CASES:
            with self.subTest(case_id):
                self.assertEqual(refusal["disposition"], "FAIL_CLOSED")
                for field in SIX_FIELDS:
                    self.assertIsInstance(refusal[field], str, field)
                    self.assertTrue(refusal[field].strip(), field)
                self.assertTrue(source.strip())
        codes = {case[3]["failure_code"] for case in CASES}
        self.assertIn("PAYMENT_PROVIDER_NOT_DECIDED", codes)

    def test_manufactured_readiness_is_refused_at_the_named_guard(self):
        names = (
            "commercial/customer-purchase-path-census.json",
            "commercial/engagement-request-transition.json",
            "commercial/contract-acceptance-observation.schema.json",
            "commercial/post-acceptance-state-machine.schema.json",
            "commercial/service-delivery-admission.schema.json",
            "commercial/terminal-commercial-evidence-path.schema.json",
        )
        pristine = self._records(names)
        for case_id, mutate, guard, refusal, _ in CASES:
            with self.subTest(case_id, failure_code=refusal["failure_code"]):
                records = json.loads(json.dumps(pristine))
                mutate(records)
                try:
                    for name, document in records.items():
                        (self.repo / name).write_text(json.dumps(document, indent=2), encoding="utf-8")
                    try:
                        _run_validator(self.repo)
                    except AssertionError as refused:
                        frames = [f for f in traceback.extract_tb(refused.__traceback__)
                                  if Path(f.filename).name == VALIDATOR.name]
                    else:
                        self.fail("the validator accepted a manufactured payment/entitlement readiness claim")
                    self.assertTrue(frames, "the refusal must come from commercial/validate_catalog.py")
                    self.assertEqual(frames[-1].lineno, _guard_line(self.repo, guard))
                finally:
                    for name, document in pristine.items():
                        (self.repo / name).write_text(json.dumps(document, indent=2), encoding="utf-8")
        _run_validator(self.repo)


if __name__ == "__main__":
    unittest.main()
