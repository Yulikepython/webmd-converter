# 変換例

このディレクトリには、WebMD Converterを使用して様々なWebページをMarkdownに変換した例が含まれています。

## ファイル一覧

- `example_output.md` - シンプルなWebページ (example.com) の変換例

## 独自のテスト方法

新しいサイトで変換をテストするには:

```bash
# 仮想環境をアクティベート
source venv/bin/activate

# URLを指定して変換を実行
python webmd_converter.py --url https://あなたのサイト --output-dir ./examples

# または、インストール済みの場合:
convertmd --url https://あなたのサイト --output-dir ./examples
```

## 注意点

- 一部のWebサイトは変換が最適化されていない場合があります
- サイトによっては特定の要素がうまく変換されないことがあります
- 画像は、変換後のMarkdownファイルではソースURLへのリンクとして保持されます