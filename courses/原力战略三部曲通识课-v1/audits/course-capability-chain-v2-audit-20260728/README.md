# 原力战略课程全链路能力配置 v2 · 审计交付

## 结论

本轮已形成可复跑的本地课程 dry-run 链，覆盖 16 个路由阶段、9 项受管能力、L0 授课卡、四证、讲稿、PPT、DOCX、XLSX、微信生态草稿和小鹅通未发布交接包。

当前真实状态没有被抬高：

- 真实课堂仍是 live_trial_pending。
- 两班真实学员、授权录像、时码逐字稿和七天证据均未产生。
- 其余九课保持 HOLD。
- 微信、视频号、小鹅通没有正式发布、定价、分享、通知、支付或删除。
- Governor validation_state 保持 unknown。

## 评分卡

| 维度 | 状态 | 证据 |
|---|---|---|
| 路由完整性 | 🟢 | capability-router.yaml 与 02-end-to-end-dry-run.json |
| 受管身份与回滚 | 🟢 | 00-managed-capability-activation.json |
| 单能力 smoke | 🟡 | 01-capability-smoke.json；三项声明降级债 |
| 课程结构与计时预算 | 🟢 | trials/01-L0-120分钟桌面排练报告.md |
| PPT / DOCX / XLSX | 🟢 | 03-asset-validation.json |
| 内容作者声纹 | 🟡 | content-quality-report.md；L4 待明哥确认 |
| 真实课堂与迁移 | 🔴 | 尚未执行，人工门 |
| 正式发布与正典回写 | 🔴 | 未授权，保持关闭 |

## 六件套

- analysis.json：机器可读事实基线。
- verify.sh：复跑路由、Schema、资产、哈希、状态与禁区检查。
- evidence/：证据索引，不复制私有运行时路径或敏感信息。
- decision-cards/：需要明哥裁决的真实试讲与发布门。
- quickwin-receipts/：本轮已完成的低风险可逆项。

## 如何复跑

从本审计目录运行 verify.sh，并显式提供 Soul 工作树：

    SOUL_ROOT=/path/to/yuanli-strategy-soul ./verify.sh

脚本任何实测不符都会非零退出；没有 || echo PASS 或伪通过分支。

## 尚未关闭的门

1. 明哥确认公开作者经历与高弧光。
2. 两班各 8–12 人、排期、录制授权与隐私告知。
3. 真实口头计时与课堂结果。
4. 七天迁移证据。
5. 平台写入、定价与正式发布逐项确认。
