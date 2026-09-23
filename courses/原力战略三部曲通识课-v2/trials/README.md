# trials｜课程试讲与验证路由

本目录只承载课程验证协议、桌面试讲证据、真实试讲证据与版本比较，不拥有 Soul 正典法权。

## 当前 G3 验证主线

```text
G3 Course Convergence
↓
Trial 08｜新版 L03 Desktop Regression
↓
Trial 09｜G3 五幕 3—8 人真人试讲
↓
24h Recall
↓
Human Gate
↓
APPROVE_PROMOTION / REVISE_AND_RETEST
```

### 08｜L03 G3 Desktop Regression

`08-l03-g3-desktop-regression/RESULT-v1.md`

状态：

```yaml
status: PASS_WITH_OVERLAY
mode: simulated_desktop_regression
live_evidence: none
```

说明：旧 L03 Desktop PASS 因课程结构级重写已经 stale；Trial 08 是新版 L03 的桌面重新资格审查。

### 09｜G3 五幕真人试讲

`09-g3-five-act-live/README.md`

这是当前唯一推荐的真人执行入口。

```yaml
status: READY_NOT_RUN
sample: 3_to_8_real_target_learners
```

它验证：

- 五幕“重估→入世→留存→继承→定向”能否 24h 重建；
- 五课是否围绕同一个 VALUE THREAD；
- 新版 L03 最小资产卡是否能独立完成；
- 课间悬念是否自然产生下一课需求；
- 是否出现真实行为改变信号。

## 历史验证轨道

`00-v1-v2-A-B-Test-Protocol.md`：保留作 v1/v2 对照协议。

`01-five-lesson-desktop-trial/`：历史五课 Desktop。

`02-anchor-cut-live-trial/`：历史 Anchor Cut 真人协议。

`03-anchor-word-level-rehearsal/`：逐字级排练。

`04-secret-life-reconstruction/`：旧“秘密的一生”连续性重构。

`05-l01-secret-life-desktop/`：旧 L01 Desktop。

`06-l02-l05-desktop/`：旧 L02—L05 Desktop；其中旧 L03 PASS 不再自动适用于新版 L03。

`07-five-act-live/`：旧五幕真人包，现被 G3 `09-g3-five-act-live/` 取代为当前执行入口；保留作历史对照，不删除。

## 法权纪律

1. Trial 不修改 Soul 正典。
2. Desktop Trial 只能产生模拟证据，不能冒充真实 24h / 7d / 30d 学员证据。
3. 真人 Trial 必须使用真实目标学员与原始记录。
4. G3 后不得用旧 L03 的 PASS 证明新 L03 已验证。
5. 未经真实课堂、24h Recall 与 Human Gate，不得设置 `reusable: true` 或 `supersedes_v1: true`。
6. 失败优先做减法：先删字段、删解释、收敛悬念，不先增加概念与案例。