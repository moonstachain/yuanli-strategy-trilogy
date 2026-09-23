# L03 Runtime Patch｜P0-SIM-01 External Reward Ablation
## 外部奖励消融 Gate

```yaml
patch_id: YFA-GC2.1-P0-SIM-01
lesson: YL-TRILOGY-GENERAL-v2-L03
status: HUMAN_ACCEPTED_AND_APPLIED
authority: teaching_runtime_patch
applies_to: v2.2-DT1 -> LT1 candidate
canon_effect: none
insert_point: A1_Mother_Hypothesis_after_peer_check_before_A2_self_endorsement
live_trial: not_run
reusable: false
```

## 1｜为什么需要这个补丁

LT1 企业家 Persona 模拟发现：

> 高成就型企业家可能把“赢、第一、高标准、极强执行、身份认可”写成 Mother。

这类答案：

- 可能跨时间出现；
- 可能跨情境出现；
- 也未必能被“能否写进岗位 JD”击穿。

因此，现有 `三表型 + JD Gate + 反证` 对此类高度身份化驱动力仍存在假绿风险。

本补丁不新增理论，只增加一次消融：

> # **如果没有排名、掌声、身份和外部认可，你还会持续对什么问题投入？**

---

## 2｜课堂插入位置

现有导演脚本：

```text
A1｜Mother Hypothesis
→ 三表型
→ 一个反证
→ Peer Check：JD Gate / 表型差异
→ A2｜Self-Endorsed Direction
```

LT1 运行时改为：

```text
A1｜Mother Hypothesis
→ 三表型
→ 一个反证
→ Peer Check：JD Gate / 表型差异
→ P0-SIM-01｜External Reward Ablation
→ A2｜Self-Endorsed Direction
```

不新增模块编号，不改变 `找 → 归 → 炼 → 证`。

---

## 3｜讲师逐字动作

[BLACK]

> **“先做一个非常短的消融。”**

[SCREEN]

> # **如果没有排名、掌声、身份和外部认可，你还会持续对什么问题投入？**

[WRITE｜60-90 sec]

学员只写一句。

[SELF-CHECK]

将答案与刚才的 Mother Hypothesis 对照：

```text
A｜核心生成机制仍然存在
B｜明显减弱，但仍值得验证
C｜几乎消失
```

如果是 C：

> **不要宣布“这是假的你”；只把当前 Mother Confidence 降低，回到 A1 重写或标记为竞争解释。**

---

## 4｜必须讲清的三条边界

讲师只允许补三句：

1. **外部塑造不等于虚假。**
2. **有外部奖励，不等于 Mother 无效。**
3. **这一问只校准假设置信度，不诊断“真正的你”。**

---

## 5｜禁止扩张

本补丁禁止扩张成：

- 内在动机 vs 外在动机理论课；
- 荣格 / 情结 / 创伤诊断；
- “真正自我”宣判；
- “有成就欲就是补偿”的结论；
- 新增第七格工具卡；
- 新增 A0 / A5；
- 新增第四条课程主口号。

时间预算：

```yaml
screen_and_prompt: 30sec
write: 60-90sec
self_check: 30sec
max_total: 3min
```

---

## 6｜LT1 观察项

真人 LT1 必须单独记录：

```yaml
external_reward_ablation:
  initial_mother_contains:
    - winning
    - ranking
    - achievement
    - extreme_execution
    - status_or_recognition
  ablation_answer: free_text
  effect_on_mother_confidence:
    - unchanged
    - lowered
    - rewritten
  teacher_rescue_required: boolean
```

### PASS 信号

- 高成就学员能够在不由讲师给答案的情况下，把“赢/第一”进一步下潜到问题选择、注意模式、判断方式或长期责任；
- 或者诚实降低当前 Mother Hypothesis 置信度。

### FAIL 信号

- 学员只是把“我想赢”换成同义词；
- 必须由老师直接告诉其 Mother 才能继续；
- 讲师把消融结果解释成心理诊断；
- 额外消耗 >3min 并挤压六格主卡完成时间。

---

## 7｜Authority Boundary

```yaml
source: YFA-GC2.1-LT1-SIM simulated entrepreneur rehearsal
human_decision: ACCEPT_P0_SIM_01
teaching_patch: AUTHORIZED
scientific_claim_upgrade: none
soul_canon_upgrade: none
real_human_evidence: false
```

本补丁只有教学运行法权。

它不能证明：

- 外部奖励与 Mother 的稳定因果关系；
- 某个学员的“真实 Self”；
- Mother 已经成立；
- 真人课堂已经通过。

# 最终一句

> **拿掉掌声，不是为了找到“纯粹的你”；而是为了看清，究竟什么问题即使无人喝彩，你仍然会回来。**
