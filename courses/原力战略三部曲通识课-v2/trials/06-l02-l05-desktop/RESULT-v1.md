# Trial 06｜L02—L05 Secret-Life Desktop v1

```yaml
trial_id: YL-TRILOGY-GENERAL-v2-TRIAL-06-v1
scope: L02-L05
status: FAIL_WITH_ACTIONABLE_PATCHES
live_trial: not_run
promotion_effect: none
```

# 总结

四课的叙事龙骨、Evidence Gate、Director 时间预算和法权边界整体成立；但第一次桌面模拟抓出 **2 个 P0 + 3 个 P1**。因此不允许直接标记四课 `LIVE_TRIAL_READY`。

---

# L02｜秘密入世

```yaml
structure: PASS
timing: PASS_ON_PAPER
artifact: PASS_WITH_P1
canon_boundary: PASS
secret_thread: PASS
result: PASS_WITH_P1
```

## 成立
- 83min 净内容 + 7min buffer；
- 见名繁守能压住四模块复杂度；
- Nokia/Wii 各只承担一次认知动作；
- B4 严格虚实入出。

## P1-01｜“两个 Anchor”可能让主角感松散

处理：Director 中明确 Dyson 只作承上对象；Nokia 是“见”的证据镜头，Wii 是“名”的证据镜头，二者不得被讲成完整第二主故事。

---

# L03｜秘密寻主

```yaml
structure: PASS
timing: RISK
artifact: FAIL
construct_boundary: PASS
result: FAIL_P0
```

## P0-01｜母体假设卡课堂负荷过大

当前卡同时要求：3实例 + 4线索 + 假设 + 反证 + 替代解释 + 取舍 + 隐性判断 + 90天验证。

在 5—7 分钟现场不现实，会导致：
- 学员草率写“母体标签”；
- 反证被跳过；
- 最后的高弧光被工具时间吃掉。

### 修复
课堂必填压成 5 项：
1. 3 个跨时期关键词（不是完整故事）；
2. Mother Hypothesis v0.1；
3. 1 个反证；
4. 1 个加减停拒；
5. 1 个 90 天验证。

“4线索细化 / 替代解释 / 隐性判断外化”转为课后扩展，但保留在卡中。

---

# L04｜秘密得生

```yaml
structure: PASS
timing: RISK
artifact: FAIL
c1_c4_boundary: PASS
result: FAIL_P0
```

## P0-02｜OS 一页架构在课堂里仍太像系统设计

当前卡要求 C1 3条 + C2 5项 + C3 3项 + C4 7项。7分钟内无法高质量完成。

### 修复
课堂只做“最小控制循环”：
- 单点判断 1 个；
- C1 边界 1 条 + Human Gate 1 个；
- C2 证据 1 条 + Unknown 1 个；
- C3 Top1 + Stop Condition；
- C4 Owner + Next Action + Outcome + Learning/Reuse。

完整字段保留为课后扩展。

---

# L05｜秘密定向

```yaml
structure: PASS
timing: PASS_ON_PAPER
artifact: PASS
integration_boundary: PASS
result: PASS_WITH_P1
```

## P1-02｜“Washington → 价值方向”可能被误读成道德说教

修复：Director 明确不要求学员赞成 Washington，只研究“可以继续 ≠ 应该继续”的结构；Patagonia 也仅证明方向可以进入机制，不当模板。

## P1-03｜“守生事人留”容易被误记为新五模块

修复：Deck 第6页和工具页持续标记 `integration questions only / not modules`。

---

# 跨课检查

```text
L01 exit S3 == L02 enter S3  PASS
L02 exit S4 == L03 enter S4  PASS
L03 exit S5 == L04 enter S5  PASS
L04 exit S6 == L05 enter S6  PASS
L05 exit S8 → 新异常         PASS
```

## 当前 Gate

```yaml
L02: DESKTOP_PASS_WITH_P1
L03: BLOCKED_BY_ARTIFACT_P0
L04: BLOCKED_BY_ARTIFACT_P0
L05: DESKTOP_PASS_WITH_P1
G2: NOT_YET_PASS
```

下一动作：修复 L03/L04 Artifact，随后运行 v2。
