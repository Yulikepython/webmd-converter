#!/bin/bash

# 仮想環境のセットアップ
python3 -m venv venv
source venv/bin/activate

# 必要なパッケージのインストール
pip install -r requirements.txt

# 現在のディレクトリのパスを取得
CURRENT_DIR=$(pwd)

# convertmd.shの内容を生成
cat > convertmd.sh << EOL
#!/bin/bash

# 環境設定
VENV_PATH="${CURRENT_DIR}/venv"
SCRIPT_PATH="${CURRENT_DIR}/hp_to_md.py"

# 仮想環境をアクティベート
source "\$VENV_PATH/bin/activate"

# Pythonスクリプトを実行
python3 "\$SCRIPT_PATH" "\$@"

# 終了コードを保存
exit_code=\$?

# 仮想環境を非アクティベート
deactivate

# スクリプトの終了コードを返す
exit \$exit_code
EOL

# convertmd.shに実行権限を付与
chmod +x convertmd.sh

# システムのパスにインストール
sudo cp convertmd.sh /usr/local/bin/convertmd

echo "セットアップが完了しました！"
echo "使用例: convertmd --url https://example.com"