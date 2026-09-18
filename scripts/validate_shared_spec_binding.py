from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
def load(p): return yaml.safe_load((ROOT/p).read_text())
b=load("governance/shared-spec/yuanli-shared-spec-binding.v0.1.yaml")
p=load("governance/shared-spec/domain-profile.v0.1.yaml")
r=load("governance/receipts/shared-spec-binding-genesis-venture.v0.1.yaml")
assert b["project_id"]=="YVENTURE"
assert b["registry_ref"]["version"]=="v0.2"
assert all(x["pin_policy"]=="FOLLOW_ACTIVE_OWNER" for x in b["bindings"])
auth=next(x for x in b["bindings"] if x["spec_id"]=="HumanAuthorization")
assert auth["canonical_state"]=="ACTIVE_SHARED_RULE"
assert p["mappings"]["TaskContract"]["projection_does_not_create_canon"] is True
assert p["mappings"]["HumanAuthorization"]["projection_ne_authority"] is True
assert r["binding_effect"]["canon_authority_changed"] is False
assert r["binding_effect"]["business_runtime_authorized"] is False
print("YVENTURE SHARED SPEC BINDING VALID")
