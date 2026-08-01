# 课程证据包

本目录保存进入讲稿前的理论、数据、案例与反例核验记录。

---

## 当前文件

- `00-原力战略-证据计划.md`：L0核心概念课完整证据需求、分层、案例计划与核验闸门。

当前状态：

```text
正典证据：verified
课程逻辑：structural_pass
外部证据需求：mapped
外部逐条核验：pending
正式数据与案例入稿：blocked_by_verification
```

A1、B1、C4已完成证据结构规划，外部论文、数据与企业案例仍待逐条核验。

---

## 证据记录格式

每条证据使用：

```yaml
lesson_id:
evidence_type: theory | data | case | counterexample | teaching_protocol
claim:
source:
evidence_level: canon | primary | official_data | longitudinal_or_cross_case | single_case | anecdotal
status: verified | candidate | to_verify
checked_at:
notes:
```

---

## 规则

- `candidate`和`to_verify`不得在正式讲稿中写成确定事实。
- 单个案例只解释机制，不证明普遍性。
- 反例必须进入课程边界，不得只放附录。
- 外部来源核验完成后，再建立每节课独立证据条目。
- 数字必须同时标记数据年份与发布时间。
- 事实、作者主张与课程推论必须分开。
- 正典证据可以支持课程结构，但不能替代外部经验事实。
- B4永远使用虚、实、入、出四大控制权口径。

---

## 证据优先级

```text
Soul正典 / 原始论文 / 官方数据
＞ 长期序列 / 跨案例比较
＞ 单一企业或个人案例
＞ 名人故事 / 个人感受
```

个人叙事只承担高弧光与价值裁决，不承担普遍事实证明。

---

## 正式讲稿闸门

- [ ] 每个关键主张有明确证据指针。
- [ ] 来源与主张匹配。
- [ ] 所有外部数字完成核验。
- [ ] 单一案例配有边界或反例。
- [ ] 未核验内容保持候选状态。
- [ ] 推论明确标记为推论。
- [ ] 作者经历获得确认。
- [ ] 真实试讲后补充学员语言、误解和失败样本。
