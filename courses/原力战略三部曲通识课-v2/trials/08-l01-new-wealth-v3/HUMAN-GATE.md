# Trial 08｜Human Patch Gate

```yaml
trial_id: YL-L01-V3-TRIAL-08
gate: HUMAN_PATCH_GATE
status: APPROVED
opened_at: 2026-08-16
approved_at: 2026-08-16
decision: AUTHORIZE_V3_1_MINIMAL_PATCH_SET
authority: human_user
canon_effect: none
```

## 批准 Patch Set

以下五项一次性批准：

- `P0-01` 秘密 ≠ 商业机会；
- `P1-01` Live Core Artifact 10—12min；
- `P1-02` 三本书脚注化 + 稀缺阶梯压缩；
- `P1-03` 关闭 L03/L05 竞争悬念，只留 L02；
- `P1-04` Value Candidate ≠ 唯一使命。

详见：`PATCH-CANDIDATES.md`。

## 授权执行链

```text
PATCH_AUTHORIZED
→ apply minimal patches
→ freeze V3.1 snapshot
→ regression desktop trial
→ context-isolated recall proxy
→ Live Readiness ruling
```

## 授权边界

本 Gate 授权：

- 修改 L01 V3 Candidate 为 V3.1 Candidate；
- 修改对应 Director / Deck / Artifact；
- 冻结 V3.1 snapshot；
- 运行 simulated desktop regression；
- 运行 context-isolated recall proxy；
- 若全部 Live Gate 清零，则将状态升级为 `LIVE_TRIAL_READY`。

本 Gate **不授权**：

- 把模拟 recall 冒充真实 24h Recall；
- 自动执行真人试讲；
- Promotion / 替换现役 V2；
- Canon upgrade；
- 修改 `CONSTITUTION.md`。

## Promotion 边界

即使 V3.1 Desktop Regression 全部 PASS，也最多只能进入：

```yaml
simulated_desktop_trial: PASS
live_trial: READY_NOT_RUN
real_24h_recall: NOT_RUN
promotion: NOT_AUTHORIZED
```
