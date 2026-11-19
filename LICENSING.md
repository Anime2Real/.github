# Anime2Real 许可政策

Anime2Real 的公开仓库采用 **「严格非商用 + 双授权」** 模式。

> **这不是 OSI 开源。** 公开许可禁止商业使用，不符合 OSI 开源定义第 6 条。对外请使用「源码公开 / source-available」的表述，不要使用「开源」或 OSI 标识。

## 许可矩阵

| 内容 | 许可 | 文件 |
|---|---|---|
| 应用、服务、固件、脚本 | PolyForm Noncommercial 1.0.0 | `LICENSE` |
| 插件、库、驱动 | PolyForm Noncommercial 1.0.0（例外见下） | `LICENSE` |
| 数据集、标注、转写 | CC BY-NC-SA 4.0 | `LICENSE` / `LICENSE-DATA` |
| 模型权重 | CC BY-NC-SA 4.0 + `MODEL-TERMS.md` | `LICENSE-DATA` |
| 硬件设计、CAD、文档 | CC BY-NC-SA 4.0 | `LICENSE` |
| 二进制、安装包 | EULA | `LICENSE` |
| 第三方素材、角色 IP、声优权利 | 各自许可，不在上述授权内 | `ASSETS.md` / `NOTICE` |

## 双授权

公开许可只允许非商业用途。商业使用——包括付费产品、付费服务、SaaS、商业模型训练、广告变现、企业内部商业生产、商业分发——需要 Anime2Real 另行签发的书面商业许可。

各仓库的 `COMMERCIAL.md` 是商业授权入口；合同模板见 `COMMERCIAL-LICENSE-TEMPLATE.md`。

## 历史版本

此前以 MIT、Apache-2.0、CC BY-NC-SA 4.0 发布的版本，其授权对该版本继续有效，不因新版本切换而撤回。每个仓库的 `LICENSE-HISTORY.md` 记录切换时间和旧许可。

**重要**：已经以 MIT/Apache-2.0 发布的版本，任何人都可以继续按旧许可商用；双授权只对新版本生效。

## 已解决

- `Chobits-Chii-Mascot`：外部贡献者 yuqian 已全权授权 Anime2Real，仓库已切换为 PolyForm Noncommercial 1.0.0；此前以 MIT 发布的版本继续适用 MIT。见 [`CONTRIBUTOR-ASSIGNMENTS.md`](CONTRIBUTOR-ASSIGNMENTS.md) 与仓库 `LICENSE-HISTORY.md`。

## 例外

- `Chobits-Chii-Pipecat`：上游 Pipecat 为 BSD-2-Clause，fork 保留上游许可。见仓库 `LICENSING-NOTE.md` 与 `NOTICE`。
- `GPT-SoVITS`、`live2d-add-motion-sample-web-ui`：上游 fork，保留上游 MIT；不适用本政策，也不得改为 NC。
- `Chobits-Chii-Mascot-Release`：二进制按 EULA 发布；源码不在该仓库。

## 文件级标记

混合许可仓库使用 SPDX 标识：

- `SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0`
- `SPDX-License-Identifier: CC-BY-NC-SA-4.0`
- `SPDX-FileCopyrightText: 2025-2026 Anime2Real`

可选 `REUSE.toml` 做目录级映射。新增文件必须带 SPDX 头，或在 `REUSE.toml` 中登记。

## 贡献

贡献前必须签署 `CLA.md`。DCO 只证明提交权，不授予再许可/商业化权利，**不足以支持双授权**。没有 CLA 的 PR 不会被合并。见 `CONTRIBUTING.md`。

## 版权归属

本组织仓库的版权人统一为 `Anime2Real 组织`。对外签约代表、注册信息见 [`COPYRIGHT.md`](COPYRIGHT.md)；贡献者授权见 [`CONTRIBUTOR-ASSIGNMENTS.md`](CONTRIBUTOR-ASSIGNMENTS.md)。

> 法律文件状态：`CLA.md`、`COMMERCIAL-LICENSE-TEMPLATE.md` 和 `Mascot-Release/LICENSE`（EULA）尚未经律师审阅，当前为草案；详见 [`LEGAL-REVIEW.md`](LEGAL-REVIEW.md)。

## 角色、声优与第三方权利

本政策只覆盖 Anime2Real 拥有权利的内容。以下内容不随仓库授权：

- 《Chobits》（人形电脑天使心）的角色形象、名称、动画音频/画面：权利归 CLAMP 及相关权利方。
- 声优（田中理惠）的声音、姓名、肖像和人格权。
- Live2D Cubism Core、示例模型和其他 Live2D 素材。
- 达妙、灵足、轮趣等厂商资料。
- 上游 fork 的代码和模型（GPT-SoVITS、Pipecat、Qwen、Fun-ASR 等）。

## 商业联系

Anime2Real <anime2real@163.com>

各仓库的切换进度和内容分支同步清单见 [`LICENSING-ROLLOUT.md`](LICENSING-ROLLOUT.md)。

邮件主题请注明 `Commercial License - <仓库名>`，并说明使用场景、分发方式、用户规模和预计收入。

## 免责声明

本政策是工程和合规设计建议，不是法律意见。角色 IP、声优人格权、CLA 和 EULA 的可执行性，请咨询熟悉中国/日本/美国法的专业律师。
