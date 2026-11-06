<div align="center">
	<img src="../resource/anime2real-logo.jpg" alt="Anime2Real" width="120" height="120" />
	<h1>Anime2Real</h1>
	<p><b>Break through the dimensional barrier!</b></p>
	<p>Bringing anime characters into the real world with AI — an open-source chain from voice and persona to visuals and everyday companionship.</p>
	<p>
		<a href="./README.md">简体中文</a> ｜ <a href="./README.ja.md">日本語</a> ｜ <a href="./README.en.md">English</a>
	</p>
	<p>
		<a href="https://github.com/Anime2Real"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-Anime2Real-181717?logo=github&amp;logoColor=white"></a>
		<a href="https://huggingface.co/chenxin199305"><img alt="Hugging Face" src="https://img.shields.io/badge/Hugging%20Face-Anime2Real-FFD21E?logo=huggingface&amp;logoColor=black"></a>
		<a href="https://discord.gg/RtEBK2NBVS"><img alt="Discord" src="https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&amp;logoColor=white"></a>
		<a href="https://qm.qq.com/q/Mvv6waayM8"><img alt="QQ" src="https://img.shields.io/badge/QQ-809591826-12B7F5?logo=tencentqq&amp;logoColor=white"></a>
		<a href="https://madewithlove.org.in"><img alt="Made with Love" src="https://img.shields.io/badge/Made%20with-Love-ff69b4.svg"></a>
	</p>
</div>

> 💖 If Anime2Real's projects help you, please give the relevant repositories a Star — your support helps more people discover us.

## 🌌 Mission

> **Break the dimensional barrier and bring characters into the real world.**

Anime2Real is an open-source organization turning characters from static designs into interactive presences. From voice data and voice cloning to persona dialogue, visual driving, and desktop companionship, we are building a complete, reproducible, and extensible open-source chain.

- **A complete chain**: data, voice, persona, visuals, and applications connect with each other instead of being scattered pieces.
- **Open and reproducible**: code, data, and models are shared whenever possible to support research and further development.
- **Respect for creators**: all projects are for study and research only and claim no rights to the original works.

## 🧩 What We Build

| 01 · Data | 02 · Voice | 03 · Persona | 04 · Visuals | 05 · Application |
| :---: | :---: | :---: | :---: | :---: |
| Voice collection & annotation | Speech synthesis / recognition | Dialogue & persona design | Live2D / motion driving | Desktop mascot & plugins |

Each module works on its own, and together they form a complete character pipeline.

## 📦 Projects

These are the currently public repositories. More modules will be opened up gradually after security and compliance reviews.

### 🎙️ Data

| Repository | Description |
| --- | --- |
| [Chobits-Chii-Voice](https://github.com/Anime2Real/Chobits-Chii-Voice) | Character voice dataset: extracted from all 24 episodes, 487 segments (~21.4 minutes), manually annotated and fully re-listened · [🤗 Dataset](https://huggingface.co/datasets/chenxin199305/Chobits-Chii-Voice) |

### 🧠 Models & Services

| Repository | Description |
| --- | --- |
| [Chobits-Chii-TTS](https://github.com/Anime2Real/Chobits-Chii-TTS) | Character text-to-speech model: fine-tuned GPT-SoVITS v2Pro, weights released · [🤗 Model](https://huggingface.co/chenxin199305/Chobits-Chii-TTS) |
| [Chobits-Chii-ASR](https://github.com/Anime2Real/Chobits-Chii-ASR) | Speech recognition service: Fun-ASR-Nano-2512 deployment + OpenAI-compatible facade, with Qwen3-ASR switchover reserved |

### 🖥️ Applications

| Repository | Description |
| --- | --- |
| [Chobits-Chii-Mascot-Release](https://github.com/Anime2Real/Chobits-Chii-Mascot-Release) | Public release channel for the AI desktop mascot: release artifacts and auto-update metadata |

### 🧩 Plugins

| Repository | Description |
| --- | --- |
| [Chobits-Chii-DSH](https://github.com/Anime2Real/Chobits-Chii-DSH) | Theme plugin for the DeepSeek Harness (DSH) Web UI: neutral warm palette + Polaroid-style photo wall · `dsh-plugin` |
| [Chobits-Chii-Kimi](https://github.com/Anime2Real/Chobits-Chii-Kimi) | Theme plugin for Kimi Code CLI: warm cream, warm ink and low-saturation rose palette, with light and dark themes and automatic plugin sync |

## 💬 Community

Join us to talk about characters, models, and desktop companionship.

<table width="100%">
<tr>
<td width="50%" valign="top" align="center">
<p><strong>QQ Group</strong><br>
Anime2Real · Group 809591826</p>
<p><a href="../resource/qq_group.jpg"><img src="../resource/qq_group_qr.jpg" alt="Anime2Real QQ group QR code" width="170"></a></p>
<p>Scan to join</p>
</td>
<td width="50%" valign="top" align="center">
<p><strong>Discord</strong><br>
Anime2Real's Server</p>
<p><a href="https://discord.gg/RtEBK2NBVS"><img src="../resource/discord_invite.png" alt="Anime2Real Discord invite QR code" width="170"></a></p>
<p>Scan or click to join</p>
</td>
</tr>
</table>

<p align="center"><sub>Discord is limited to 10 members. Fans who genuinely love anime and share constructive feedback are welcome.</sub></p>

## 📄 License & Disclaimer

- The code, data, and models in each repository follow the `LICENSE` in that repository.
- The copyright of the original anime, characters, and audio belongs to their respective rights holders. All projects under this organization are for study and research only; please do not use them for commercial purposes.
- Related projects will be taken down if the rights holders so request.
