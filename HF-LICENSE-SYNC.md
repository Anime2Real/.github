# Hugging Face 许可元数据同步

## 当前状态

- `chenxin199305/Chobits-Chii-Voice`（dataset）：`license: cc-by-nc-sa-4.0` 已存在。
- `chenxin199305/Chobits-Chii-TTS-GPTSoVITS`（model）：`license: cc-by-nc-sa-4.0` 已存在。
- `chenxin199305/Chobits-Chii-TTS-CosyVoice`（model）：`license: cc-by-nc-sa-4.0` 已存在。
- `chenxin199305/Chobits-Chi`（dataset）：没有 README 或已空；跳过。

因此 SPDX 许可字段本身已经正确；需要同步的是 **范围说明、商业授权入口和声优/角色权利排除**。

## 为什么没有直接上传

- 当前网络无法直连 `huggingface.co`（连接被重置）。
- 环境里的 `HF_TOKEN` 和缓存 token 均已失效，无法鉴权上传。

## 如何完成

在有可用 token 和 HF 网络（或代理）的环境运行：

```bash
export HF_TOKEN=...          # 有效的 HF write token
# 如直连被阻断，先配置代理；不要改 HF_ENDPOINT 为只读镜像
python .github/scripts/sync-hf-license.py --dry-run
python .github/scripts/sync-hf-license.py
```

`--dry-run` 会把更新后的 README 写到 `/tmp/anime2real-hf-updated/`，不会上传。

## 脚本做什么

- 确保 README front matter 有 `license: cc-by-nc-sa-4.0`。
- 在 README 末尾追加“范围与商业授权”一节：
  - 仅覆盖 Anime2Real 原创的标注/权重；
  - 原始动画音频、角色 IP、声优权利不在授权范围内；
  - 商业使用需要单独授权；
  - 链接到 GitHub 的 `DATASET-TERMS.md` / `MODEL-TERMS.md`。
- 保留原有 README 内容，不覆盖模型卡主体。

## 覆盖仓库

| 仓库 | 类型 | 条款链接 |
|---|---|---|
| `chenxin199305/Chobits-Chii-Voice` | dataset | `Chobits-Chii-Voice/DATASET-TERMS.md` |
| `chenxin199305/Chobits-Chii-TTS-GPTSoVITS` | model | `Chobits-Chii-TTS/MODEL-TERMS.md` |
| `chenxin199305/Chobits-Chii-TTS-CosyVoice` | model | `Chobits-Chii-TTS/MODEL-TERMS.md` |

## 如果 token 过期

```bash
hf auth login --force
# 或重新生成 write token：https://huggingface.co/settings/tokens
```
