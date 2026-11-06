<div align="center">

# Anime2Real

**次元の壁を超えよう！**

AI 技術で二次元キャラクターを現実世界へ。

<p>
<a href="./README.md">简体中文</a> ｜ <a href="./README.ja.md">日本語</a> ｜ <a href="./README.en.md">English</a>
</p>

</div>

現在のフラッグシッププロジェクトは、『ちょびっツ』(Chobits) の **ちぃ (Chii / 小叽)** です —— 音声データセット、声質クローン、対話モデルからデスクトップマスコットまでをカバーする完全オープンソースのチェーンです。

## プロジェクト一覧

### データセット

| リポジトリ | 概要 |
| --- | --- |
| [Chobits-Chii-Voice](https://github.com/Anime2Real/Chobits-Chii-Voice) | ちぃの音声データセット（CV：田中理恵）：TV 全 24 話から抽出、487 セグメント約 21.4 分、人手によるアノテーション＋全数再聴取 · [🤗 Dataset](https://huggingface.co/datasets/chenxin199305/Chobits-Chii-Voice) |

### モデルとサービス

| リポジトリ | 概要 |
| --- | --- |
| [Chobits-Chii-TTS](https://github.com/Anime2Real/Chobits-Chii-TTS) | ちぃの音声合成モデル：GPT-SoVITS v2Pro をファインチューニング、重みを公開済み · [🤗 Model](https://huggingface.co/chenxin199305/Chobits-Chii-TTS) |
| [Chobits-Chii-ASR](https://github.com/Anime2Real/Chobits-Chii-ASR) | ちぃの音声認識サービス：Fun-ASR-Nano-2512 をデプロイ＋OpenAI 互換フロントを提供、Qwen3-ASR への切り替えを想定 |

### アプリケーション

| リポジトリ | 概要 |
| --- | --- |
| [Chobits-Chii-Mascot-Release](https://github.com/Anime2Real/Chobits-Chii-Mascot-Release) | AI デスクトップマスコット「ちぃ」の公開リリースチャンネル：Release 成果物と自動更新メタデータ |

### プラグイン

| リポジトリ | 概要 |
| --- | --- |
| [Chobits-Chii-DSH](https://github.com/Anime2Real/Chobits-Chii-DSH) | DeepSeek Harness (DSH) Web UI 向けちぃスキンプラグイン：ニュートラルで暖色系の配色＋ポラロイド風フォトウォール · `dsh-plugin` |
| [Chobits-Chii-Kimi](https://github.com/Anime2Real/Chobits-Chii-Kimi) | Kimi Code CLI 向けちぃテーマプラグイン：ウォームクリーム、ウォームインク、低彩度ローズの配色。ライト／ダーク 2 種類のテーマとプラグイン自動同期を搭載 |

## コミュニティ

<table width="100%">
<thead>
<tr>
<th align="center" width="50%">QQ</th>
<th align="center" width="50%">Discord</th>
</tr>
</thead>
<tbody>
<tr>
<td width="50%" valign="top" align="center">
<p>QQ グループ <strong>Anime2Real</strong>（グループ番号：809591826）にぜひご参加ください。QR コードから参加できます：</p>
<p><a href="../resource/qq_group.jpg"><img src="../resource/qq_group.jpg" alt="Anime2Real QQ グループの QR コード" width="180"></a></p>
</td>
<td width="50%" valign="top" align="center">
<p>Discord サーバー <strong>Anime2Real's Server</strong> へようこそ。現在 10 名までの限定です。ちぃを本当に愛し、前向きなフィードバックをくださる方のご参加をお待ちしています。</p>
<p><a href="https://discord.gg/RtEBK2NBVS"><img src="https://img.shields.io/badge/Discord-Join%20Anime2Real-5865F2?logo=discord&amp;logoColor=white&amp;style=for-the-badge" alt="Join Anime2Real on Discord"></a></p>
<p><a href="../resource/discord_invite.png"><img src="../resource/discord_invite.png" alt="Anime2Real Discord 招待 QR コード" width="180"></a></p>
</td>
</tr>
</tbody>
</table>

## 免責事項

原作アニメおよび音声の著作権は各権利者に帰属します。本組織のすべてのプロジェクトは学習・研究目的のみであり、商用利用はご遠慮ください。
