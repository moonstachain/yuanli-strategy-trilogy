# 课程证据包

本目录保存进入讲稿前的理论、数据、案例与反例核验记录。

每条证据使用：

```yaml
lesson_id:
evidence_type: theory | data | case | counterexample
claim:
source:
evidence_level: primary | official_data | longitudinal_or_cross_case | single_case | anecdotal
status: verified | candidate | to_verify
checked_at:
notes:
```

规则：

- `candidate` 和 `to_verify` 不得在正式讲稿中写成确定事实。
- 单个案例只解释机制，不证明普遍性。
- 反例必须进入课程边界，不得只放附录。
- 外部来源核验完成后，再建立每节课独立证据文件。

当前状态：A1、B1、C4 已完成证据结构规划，外部论文、数据与企业案例仍待逐条核验。
