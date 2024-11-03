import requests
from bs4 import BeautifulSoup
import html2text
import os
from urllib.parse import urlparse
import argparse


def url_to_markdown(url, output_dir):
    """
    指定されたURLのWebページをMarkdownファイルとして保存する関数

    Parameters:
        url (str): 変換したいWebページのURL
        output_dir (str): 出力先ディレクトリ名
    """
    try:
        # URLからコンテンツを取得
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # エラーチェック

        # エンコーディングを設定
        response.encoding = response.apparent_encoding

        # BeautifulSoupでHTMLをパース
        soup = BeautifulSoup(response.text, 'html.parser')

        # 不要な要素を削除
        for script in soup(["script", "style"]):
            script.decompose()

        # タイトルを取得
        title = soup.title.string if soup.title else "untitled"

        # HTML to Markdownコンバーターの設定
        h2t = html2text.HTML2Text()
        h2t.ignore_links = False
        h2t.ignore_images = False
        h2t.ignore_emphasis = False
        h2t.body_width = 0  # 行の折り返しを無効化

        # HTMLをMarkdownに変換
        markdown_content = h2t.handle(str(soup))

        # 出力ディレクトリの作成
        os.makedirs(output_dir, exist_ok=True)

        # ファイル名の生成（URLのパスから）
        parsed_url = urlparse(url)
        filename = parsed_url.path.strip('/').replace('/', '_') or 'index'
        if not filename.endswith('.md'):
            filename += '.md'

        # フルパスの作成
        filepath = os.path.join(output_dir, filename)

        # Markdownファイルとして保存
        with open(filepath, 'w', encoding='utf-8') as f:
            # メタデータを追加
            f.write(f'---\n')
            f.write(f'title: {title}\n')
            f.write(f'source_url: {url}\n')
            f.write(f'---\n\n')
            f.write(markdown_content)

        return filepath

    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        return None


def parse_arguments():
    """コマンドライン引数をパースする関数"""
    parser = argparse.ArgumentParser(
        description='WebページをMarkdownファイルに変換するツール',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  convertmd --url https://example.com
  convertmd --url https://example.com --output-dir ~/my_markdown

注意:
  - 出力ディレクトリが存在しない場合は自動的に作成されます
  - ファイル名はURLのパスから自動的に生成されます
""")

    parser.add_argument('--url', type=str, required=True,
        help='変換したいWebページのURL')
    parser.add_argument('--output-dir', type=str,
        default=os.path.expanduser('~/Documents/hp_to_md'),
        help='出力先ディレクトリのパス (デフォルト: ~/Documents)')
    return parser.parse_args()


if __name__=="__main__":
    args = parse_arguments()
    # 出力ディレクトリのパスを絶対パスに変換
    output_dir = os.path.expanduser(args.output_dir)
    output_file = url_to_markdown(args.url, output_dir)
    if output_file:
        print(f"\n変換が完了しました。")
        print(f"出力ディレクトリ: {output_dir}")
        print(f"出力ファイル: {os.path.basename(output_file)}")