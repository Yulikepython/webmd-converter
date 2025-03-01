# WebMD Converter

Webページを簡単にMarkdownファイルに変換するコマンドラインツールです。
変換したファイルは自動的にローカルに保存され、メタデータ（タイトルとソースURL）も含まれます。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/Yulikepython/webmd-converter/actions/workflows/tests.yml/badge.svg)](https://github.com/Yulikepython/webmd-converter/actions/workflows/tests.yml)

## クイックスタート

```bash
# 1. 前提条件
# - Python 3.7以上がインストールされていること
# - pipがインストールされていること

# 2. リポジトリのクローン
git clone https://github.com/Yulikepython/webmd-converter.git
cd webmd-converter

# 3. セットアップスクリプトに実行権限を付与
chmod +x setup.sh

# 4. 初期設定を実行（仮想環境を作成し、依存パッケージをインストール）
./setup.sh

# 5. 使用例
./run-webmd-converter.sh --url https://example.com
```

## 機能

- HTMLページをMarkdownに変換
- メタデータ（タイトル、ソースURL）の自動付与
- カスタム出力ディレクトリの指定が可能
- ファイル名の自動生成

## 必要要件

- Python 3.7以上
- pip (Pythonパッケージマネージャー)
- bash シェル環境
- 対応OS:
  - **Linux**: 完全対応
  - **macOS**: 完全対応
  - **Windows**: 以下のいずれかの方法で対応
    - [WSL (Windows Subsystem for Linux)](https://learn.microsoft.com/ja-jp/windows/wsl/install) を使用
    - [Git Bash](https://gitforwindows.org/) を使用
    - [Cygwin](https://www.cygwin.com/) を使用

## 詳細なインストール手順

1. **環境の確認**:
```bash
# Pythonバージョンの確認（3.7以上が必要）
python3 --version

# pipがインストールされていることを確認
pip --version
```

2. **リポジトリのクローン**:
```bash
git clone https://github.com/Yulikepython/webmd-converter.git
cd webmd-converter
```

3. **セットアップスクリプトに実行権限を付与**:
```bash
chmod +x setup.sh
```

4. **セットアップスクリプトの実行**:
```bash
./setup.sh
```

セットアップスクリプトは以下の処理を行います:
- Pythonの仮想環境の作成
- 必要なパッケージのインストール
- `webmd_converter.py`スクリプトに実行権限を付与
- 仮想環境を自動的にアクティベートする実行スクリプト（run-webmd-converter.sh）の作成
- デフォルトの出力ディレクトリの作成

## 基本的な使い方

1. **基本的な変換**:
```bash
./run-webmd-converter.sh --url https://example.com
```

2. **出力先を指定して変換**:
```bash
./run-webmd-converter.sh --url https://example.com --output-dir ~/my_markdown
```

3. **ヘルプの表示**:
```bash
./run-webmd-converter.sh -h
```

## 出力について

- **デフォルトの出力先**: `~/Documents/webmd_output`
- **ファイル形式**: Markdown (.md)
- **ファイル名**: URLのパスから自動生成
- **出力例**: [サンプル出力例](examples/example_output.md)

```markdown
---
title: Example Domain
source_url: https://example.com
---

# Example Domain

This domain is for use in illustrative examples...
```

プロジェクトの[examples](examples/)ディレクトリには、さらに詳細な変換例が含まれています。

## トラブルシューティング

よくある問題と解決方法:

1. **実行スクリプトのエラー**
```bash
# 実行スクリプトが存在するか確認
ls -la run-webmd-converter.sh
# 実行権限を確認
chmod +x run-webmd-converter.sh
# 実行スクリプトが存在しない場合はセットアップを再実行
./setup.sh
```

2. **仮想環境のエラー**
```bash
# 仮想環境が作成されているか確認
ls -la venv
# 仮想環境が存在しない場合は再作成
python3 -m venv venv
# 必要なパッケージを再インストール
source venv/bin/activate && pip install -r requirements.txt
```

3. **権限エラー**
```bash
# 出力ディレクトリの権限を確認
ls -la ~/Documents/webmd_output
# 必要に応じて権限を変更
chmod 755 ~/Documents/webmd_output
```

4. **Windowsでの実行エラー**
```bash
# WSLを使用してLinux環境で実行
# または
# Git Bashを使用して実行
# Pythonのパスが異なる場合はsetup.shを編集
```

## カスタマイズ

設定の変更方法:

- **出力先の変更**: `webmd_converter.py`の`--output-dir`パラメータを編集
- **変換設定の変更**: `webmd_converter.py`の`url_to_markdown`関数を編集

## PyPIパッケージとしてリリース（開発者向け）

開発後、PyPIにパッケージをリリースする場合:

```bash
# ビルド
pip install --upgrade build
python -m build

# アップロード（TestPyPIへ）
pip install --upgrade twine
python -m twine upload --repository testpypi dist/*

# 本番PyPIへアップロード
python -m twine upload dist/*
```

リリース後はpipでインストール可能になります:

```bash
pip install webmd-converter
```

## ライセンス

MIT License

## 貢献について

プロジェクトへの貢献を歓迎します。詳細な貢献ガイドラインは [CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。

基本的な流れ:
1. Issueの作成
2. プルリクエストの手順:
   - フォーク
   - 新規ブランチ作成 (`feature/amazing-feature`)
   - コミット (`git commit -m 'Add feature'`)
   - プッシュ (`git push origin feature/amazing-feature`)
   - プルリクエスト作成

## テスト

テストの実行方法:

```bash
# テスト実行（自動的に仮想環境を使用）
./run-webmd-converter.sh --test

# または手動で
./run-webmd-converter.sh -m unittest tests.py
```

## 作者

- Hiroshi Nishito (@yulikepython)

## 行動規範

このプロジェクトは [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md) に準拠しています。参加する際にはこの行動規範に従うことが求められます。