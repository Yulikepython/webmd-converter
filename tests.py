#!/usr/bin/env python3
"""
WebMD Converter - テストスイート
"""

import unittest
import os
import tempfile
from webmd_converter import url_to_markdown, parse_arguments
from unittest.mock import patch, MagicMock


class TestWebMDConverter(unittest.TestCase):
    """WebMD Converterの機能テスト"""

    def setUp(self):
        """テスト前の準備"""
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """テスト後のクリーンアップ"""
        # 一時ファイルの削除などが必要な場合
        pass

    @patch('requests.get')
    @patch('webmd_converter.BeautifulSoup')
    def test_url_to_markdown_basic(self, mock_soup, mock_requests):
        """基本的な変換機能のテスト"""
        # モックの設定
        mock_response = MagicMock()
        mock_response.text = "<html><head><title>Test Title</title></head><body><h1>Test Content</h1></body></html>"
        mock_response.apparent_encoding = 'utf-8'
        mock_requests.return_value = mock_response

        # タイトル要素のモック
        mock_title = MagicMock()
        mock_title.string = "Test Title"
        mock_soup_instance = MagicMock()
        mock_soup_instance.title = mock_title
        mock_soup.return_value = mock_soup_instance

        # html2textの出力をモック
        with patch('html2text.HTML2Text.handle', return_value="# Test Content"):
            # 関数を実行
            output_file = url_to_markdown("https://example.com", self.temp_dir)

            # 出力を検証
            self.assertIsNotNone(output_file)
            
            # ファイルの内容を確認
            with open(output_file, 'r', encoding='utf-8') as f:
                content = f.read()
                self.assertIn("title: Test Title", content)
                self.assertIn("source_url: https://example.com", content)
                self.assertIn("# Test Content", content)

    def test_parse_arguments(self):
        """コマンドライン引数のパース機能のテスト"""
        with patch('argparse.ArgumentParser.parse_args', return_value=MagicMock(url='https://example.com', output_dir='/tmp/test')):
            args = parse_arguments()
            self.assertEqual(args.url, 'https://example.com')
            self.assertEqual(args.output_dir, '/tmp/test')

    @patch('requests.get')
    def test_error_handling(self, mock_requests):
        """エラーハンドリングのテスト"""
        # 例外を発生させるようにモックを設定
        mock_requests.side_effect = Exception("Test error")
        
        # 関数を実行
        output_file = url_to_markdown("https://example.com", self.temp_dir)
        
        # 結果を検証（エラー時はNoneを返すことを確認）
        self.assertIsNone(output_file)


if __name__ == '__main__':
    unittest.main()