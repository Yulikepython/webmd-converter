#!/bin/bash

# WebMD Converter セットアップスクリプト
echo "WebMD Converter をセットアップしています..."

# Pythonバージョンチェック
PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)

if [[ "$PYTHON_MAJOR" -lt 3 || ("$PYTHON_MAJOR" -eq 3 && "$PYTHON_MINOR" -lt 7) ]]; then
  echo "エラー: Python 3.7以上が必要です。現在のバージョン: $PYTHON_VERSION"
  echo "Python 3.7以上をインストールしてから再度実行してください。"
  exit 1
fi

echo "Python $PYTHON_VERSION を使用します"

# 仮想環境の確認と作成
if [ -d "venv" ]; then
  echo "既存の仮想環境を使用します"
else
  echo "新しい仮想環境を作成しています..."
  python3 -m venv venv
fi

# 仮想環境のアクティベート
source venv/bin/activate || {
  echo "仮想環境のアクティベートに失敗しました"
  echo "Python venvパッケージがインストールされているか確認してください"
  echo "Ubuntu/Debian: sudo apt install python3-venv"
  echo "Fedora: sudo dnf install python3-virtualenv"
  echo "Arch: pacman -S python-virtualenv"
  exit 1
}

# 必要なパッケージのインストール
echo "依存パッケージをインストールしています..."
pip install -r requirements.txt || {
  echo "パッケージのインストールに失敗しました"
  exit 1
}

# 現在のディレクトリのパスを取得
CURRENT_DIR=$(pwd)

# スクリプトに実行権限を付与
chmod +x webmd_converter.py

# 使用方法の説明
cat > run-webmd-converter.sh << EOL
#!/bin/bash
# WebMD Converter 実行スクリプト
source "${CURRENT_DIR}/venv/bin/activate"
python "${CURRENT_DIR}/webmd_converter.py" "\$@"
EOL
chmod +x run-webmd-converter.sh

echo "実行スクリプトを作成しました"
echo "これで仮想環境のアクティベートなしで直接実行できます"
echo "使用方法: ./run-webmd-converter.sh --url <URL>"

# 出力ディレクトリの作成
DEFAULT_OUTPUT_DIR=$(python3 -c "import os; print(os.path.expanduser('~/Documents/webmd_output'))")
mkdir -p "$DEFAULT_OUTPUT_DIR" || {
  echo "警告: 出力ディレクトリの作成に失敗しました"
  echo "手動で作成してください: mkdir -p $DEFAULT_OUTPUT_DIR"
}

if [ -d "$DEFAULT_OUTPUT_DIR" ]; then
  echo "デフォルト出力ディレクトリを作成しました: $DEFAULT_OUTPUT_DIR"
fi

echo ""
echo "===================================="
echo "セットアップが完了しました！"
echo "===================================="
echo ""
echo "使用方法:"
echo "./run-webmd-converter.sh --url https://example.com"
echo ""
echo "ヘルプの表示:"
echo "./run-webmd-converter.sh -h"
echo ""
echo "詳細な使用方法については README.md をご覧ください"