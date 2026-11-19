# 许可切换进度

本文件记录「严格 NC + 双授权」在各仓库的落地状态。**远端尚未推送**；以下状态指本地工作区。

| 仓库 | 本地状态 | 内容分支 | 备注 |
|---|---|---|---|
| Chobits-Chii-ASR | 已改 | 待同步 | `main` 是索引；分支见 `BRANCH-LICENSING.md` |
| Chobits-Chii-TTS | 已改 | 待同步 | 同上 |
| Chobits-Chii-LLM | 已改 | 待同步 | 同上 |
| Chobits-Chii-Voice | 已改 | 无 | 保持 CC BY-NC-SA 4.0，补数据范围 |
| Chobits-Chii-Voice-Extra | 已改 | 无 | 同上 |
| Chobits-Chii-DSH | 已改 | 无 | 代码 PolyForm；资产另计 |
| Chobits-Chii-Kimi | 已改 | 无 | 代码 PolyForm；无角色资产 |
| Chobits-Chii-Claude | 已改 | 无 | 代码 PolyForm；无角色资产 |
| Chobits-Chii-LiveTalk | 已改 | 无 | 代码 PolyForm；安装包另计 |
| Chobits-Chii-LiveTalk-Release | 已改 | 无 | 发布页 PolyForm；安装包 EULA/各自许可 |
| Chobits-Chii-Live2D | 已改 | 无 | 代码 PolyForm；Live2D 素材另计 |
| Chobits-Chii-ElectricCamera | 已改 | 无 | 代码 PolyForm；厂商资料另计 |
| Chobits-Chii-ElectricMotor | 已改 | 无 | 代码 PolyForm；厂商资料另计 |
| Chobits-Chii-ElectricAudio | 已改 | 无 | 代码 PolyForm；厂商资料另计 |
| Chobits-Chii-ElectricEye | 已改 | 无 | 固件 PolyForm；硬件文档 CC |
| Chobits-Chii-ParallelNeck | 已改 | 无 | 设计 CC；代码 PolyForm |
| Chobits-Chii-KigurumiHead | 已改 | 无 | 设计 CC；代码 PolyForm |
| Chobits-Chii-Live3D | 已改 | 无 | 设计 CC；代码 PolyForm |
| Chobits-Chii-ServerDeploy | 已改 | 无 | 配置/脚本 PolyForm |
| Chobits-Chii-Mascot | 例外 | 多分支 | 保留 MIT；外部贡献者未签 CLA |
| Chobits-Chii-Mascot-Release | 例外 | 无 | 二进制 EULA；补商业授权入口 |
| Chobits-Chii-Pipecat | 例外 | 无 | 上游 BSD-2；不能整体改 NC |
| Chobits-Chii-Resource | 例外 | 无 | 第三方素材；无 LICENSE，默认保留所有权利 |
| GPT-SoVITS | 未改 | — | 上游 fork，保留 MIT |
| live2d-add-motion-sample-web-ui | 未改 | — | 上游 fork，保留 MIT |

## 完成切换所需的操作

1. 在各仓库提交本地变更。
2. 推送 `main`。
3. 对 ASR/TTS/LLM 的内容分支执行 `BRANCH-LICENSING.md` 中的 cherry-pick/覆盖步骤。
4. 在 Hugging Face 的模型/数据集页面同步许可元数据和范围说明。
5. 填写 `COPYRIGHT.md`，确认法律主体。
6. 由律师审阅 `CLA.md`、`COMMERCIAL-LICENSE-TEMPLATE.md` 和 `Mascot-Release/LICENSE`（EULA）。

## 验证命令

```bash
git show main:LICENSE | head -1
# 应为 PolyForm Noncommercial License 1.0.0

git show <branch>:LICENSE | head -1
# 内容分支也应为 PolyForm

git status --porcelain
# 确认只包含预期的许可/文档变更
```
