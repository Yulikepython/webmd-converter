#!/bin/bash

# convertmd.sh
VENV_PATH=".../venv" #★★環境に合わせて変更する
SCRIPT_PATH="..../hp_to_md.py"　#★★環境に合わせて変更する

# 仮想環境をアクティベート
source "$VENV_PATH/bin/Python/bin/activate" #★★環境に合わせて変更する

# Pythonスクリプトを実行し、すべての引数を渡す
python3 "$SCRIPT_PATH" "$@"

# 終了コードを保存
exit_code=$?

# 仮想環境を非アクティベート
deactivate

# スクリプトの終了コードを返す
exit $exit_code
