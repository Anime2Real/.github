#!/usr/bin/env python3
"""Sync noncommercial license metadata and scope notes to Hugging Face cards.

Usage:
    export HF_TOKEN=...          # write token
    python .github/scripts/sync-hf-license.py --dry-run
    python .github/scripts/sync-hf-license.py

If huggingface.co is unreachable, configure a proxy first. Do not point
HF_ENDPOINT at a read-only mirror for the upload step.
"""
import argparse
import os
import re
from pathlib import Path

from huggingface_hub import HfApi, hf_hub_download

REPOS = [
    (
        "chenxin199305/Chobits-Chii-Voice",
        "dataset",
        "https://github.com/Anime2Real/Chobits-Chii-Voice/blob/main/DATASET-TERMS.md",
    ),
    (
        "chenxin199305/Chobits-Chii-TTS-GPTSoVITS",
        "model",
        "https://github.com/Anime2Real/Chobits-Chii-TTS/blob/main/MODEL-TERMS.md",
    ),
    (
        "chenxin199305/Chobits-Chii-TTS-CosyVoice",
        "model",
        "https://github.com/Anime2Real/Chobits-Chii-TTS/blob/main/MODEL-TERMS.md",
    ),
]

SECTION = """## 范围与商业授权

- 本许可仅覆盖 Anime2Real 原创的标注、转写、筛选、元数据和模型权重；原始动画音频、角色形象、声优声音和人格权不在授权范围内。
- 不得用于商业用途。商业使用需要 Anime2Real 另行签发的书面许可，请联系 <anime2real@163.com>。
- 详细条款：{terms}
- 第三方与上游权利见 GitHub 仓库的 `NOTICE`。
- 本仓库不是 OSI 开源项目；公开许可仅限非商业使用。
"""


def ensure_license(text: str) -> str:
    if not text.startswith("---\n"):
        return "---\nlicense: cc-by-nc-sa-4.0\n---\n\n" + text
    end = text.find("\n---", 4)
    if end == -1:
        return "---\nlicense: cc-by-nc-sa-4.0\n---\n\n" + text
    front = text[4:end]
    if re.search(r"^license:\s*.*$", front, flags=re.M):
        front = re.sub(r"^license:\s*.*$", "license: cc-by-nc-sa-4.0", front, count=1, flags=re.M)
    else:
        front = front.rstrip() + "\nlicense: cc-by-nc-sa-4.0"
    return "---\n" + front.strip("\n") + "\n---" + text[end + 4:]


def ensure_section(text: str, terms: str) -> str:
    text = re.sub(r"\n## 范围与商业授权.*$", "", text, flags=re.S)
    return text.rstrip() + "\n\n" + SECTION.format(terms=terms) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    token = os.environ.get("HF_TOKEN")
    if not args.dry_run and not token:
        raise SystemExit("HF_TOKEN is required for upload. Use --dry-run to preview.")

    api = HfApi(token=token)
    out = Path("/tmp/anime2real-hf-updated")
    out.mkdir(parents=True, exist_ok=True)

    for repo, repo_type, terms in REPOS:
        try:
            path = hf_hub_download(repo_id=repo, filename="README.md", repo_type=repo_type, token=token)
            text = Path(path).read_text(encoding="utf-8")
        except Exception:
            text = f"# {repo.split('/')[-1]}\n"
        text = ensure_section(ensure_license(text), terms)
        dst = out / (repo.replace("/", "__") + ".md")
        dst.write_text(text, encoding="utf-8")
        print(f"prepared {dst}")
        if not args.dry_run:
            api.upload_file(
                path_or_fileobj=str(dst),
                path_in_repo="README.md",
                repo_id=repo,
                repo_type=repo_type,
                commit_message="docs(license): sync noncommercial scope and commercial licensing",
            )
            print(f"uploaded {repo}")


if __name__ == "__main__":
    main()
