# trials｜课程试讲与验证路由

本目录只承载课程验证协议、桌面试讲证据、真实试讲证据与版本比较，不拥有 Soul 正典法权。

## 当前验证轨道

### 00｜v1 / v2 A/B Test

`00-v1-v2-A-B-Test-Protocol.md`

用途：在 v2 完成自身桌面试讲后，与 v1 做真实教学对照。当前不是下一步默认执行入口。

### 01｜五课 Desktop Trial

`01-five-lesson-desktop-trial/`

用途：在进入真人课堂前，对 v2 五课做受控压力测试，专门寻找：

- 理解断点；
- 危险误解；
- 认知过载；
- 工具不可完成；
- 节奏超载；
- 课间悬念断裂；
- 五课龙骨无法重建。

当前状态：

```yaml
trial_id: YL-TRILOGY-GENERAL-v2-DESKTOP-01
status: READY_NOT_RUN
input_snapshot_commit: 6be729bf56759604f2ce2ff19e5163e2206ae2cf
results_exist: false
desktop_trial: not_run
live_trial: not_run
```

## 法权纪律

1. Trial 不修改 Soul 正典。
2. Round 1 运行期间不得修改冻结课程输入。
3. Observer 记录问题但不救场。
4. Learner 不得访问 Soul、其他课正文或项目记忆来补足当前课程。
5. Desktop Trial 只能产生模拟证据，不能冒充真实 24h / 7d / 30d 学员证据。
6. 只有 Receipt 明确 PASS，才允许将课程状态推进为 `live_trial: ready_not_run`。
7. 未经真实课堂、迁移验证与 Human Gate，不得设置 `reusable: true` 或 `supersedes_v1: true`。
