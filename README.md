# HTML to Markdown Converter

Webページを簡単にMarkdownファイルに変換するコマンドラインツールです。
変換したファイルは自動的にローカルに保存され、メタデータ（タイトルとソースURL）も含まれます。

## クイックスタート

```bash
# 1. リポジトリのクローン
git clone https://github.com/yourusername/html-to-markdown.git
cd html-to-markdown

# 2. 初期設定を実行
./setup.sh

# 3. 使用例
convertmd --url https://example.com
```

## 機能

- HTMLページをMarkdownに変換
- メタデータ（タイトル、ソースURL）の自動付与
- カスタム出力ディレクトリの指定が可能
- ファイル名の自動生成

## 必要要件

- Python 3.7以上
- pip (Pythonパッケージマネージャー)
- Linux または macOS（Windowsは現在未対応）

## 詳細なインストール手順

1. **リポジトリのクローン**:
```bash
git clone https://github.com/yourusername/html-to-markdown.git
cd html-to-markdown
```

2. **setup.shの編集**:
```bash
# 環境に合わせてパスを編集
nano setup.sh
```

3. **セットアップスクリプトの実行**:
```bash
chmod +x setup.sh
./setup.sh
```

## 基本的な使い方

1. **基本的な変換**:
```bash
convertmd --url https://example.com
```

2. **出力先を指定して変換**:
```bash
convertmd --url https://example.com --output-dir ~/my_markdown
```

3. **ヘルプの表示**:
```bash
convertmd -h
```

## 出力について

- **デフォルトの出力先**: `~/Documents/hp_to_md`
- **ファイル形式**: Markdown (.md)
- **ファイル名**: URLのパスから自動生成
- **出力例**:
```markdown
---
title: Example Domain
source_url: https://example.com
---

# Example Domain

This domain is for use in illustrative examples...
```

## トラブルシューティング

よくある問題と解決方法:

1. **`convertmd: command not found`**
```bash
# コマンドへのパスを確認
echo $PATH
# 必要に応じて再インストール
sudo cp convertmd.sh /usr/local/bin/convertmd
sudo chmod +x /usr/local/bin/convertmd
```

2. **仮想環境のエラー**
```bash
# convertmd.shの中のVENV_PATHを確認・修正
sudo nano /usr/local/bin/convertmd
```

3. **権限エラー**
```bash
# 出力ディレクトリの権限を確認
ls -la ~/Documents/hp_to_md
# 必要に応じて権限を変更
chmod 755 ~/Documents/hp_to_md
```

## カスタマイズ

設定の変更方法:

- **出力先の変更**: `hp_to_md.py`の`default`パラメータを編集
- **変換設定の変更**: `hp_to_md.py`の`url_to_markdown`関数を編集

## ライセンス

MIT License

## 貢献について

1. Issueの作成
2. プルリクエストの手順:
   - フォーク
   - 新規ブランチ作成 (`feature/amazing-feature`)
   - コミット (`git commit -m 'Add feature'`)
   - プッシュ (`git push origin feature/amazing-feature`)
   - プルリクエスト作成

## 作者

- Your Name (@yourusername)