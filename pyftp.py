# -*- coding: utf-8 -*-

import datetime
import time
from ftplib import FTP


"""
# FTP送信設定
hostname = '__ftpサーバー名__'
username = '__ftpユーザー名__'
password = '__パスワード__'
local_path = '__ローカルパス__'
localfile_name = '__ローカルファイル名__'
target_path = '__ターゲットパス__'
file_name = '__ファイル名__'
"""


def put_data(hostname, username, password, localfile_path, localfile_name, target_path, file_name):
    
    # FTP接続
    ftp = FTP(hostname, username, passwd=password)

    # タイムスタンプ生成
    datetime_now = datetime.datetime.now()
    timestamp = datetime_now.strftime('%Y/%m/%d %H:%M:%S')

    with open(local_path + localfile_name, 'rb') as f:

        # テキストアップロード
        ftp.storlines('STOR ' + target_path + file_name, f)

        # ステータス表示生成
        message0 = '---------------------------------------------------------------------\n'
        message1 = timestamp + ' ' + target_path + file_path + ' をアップロードしました。\n'
        message2 = '---------------------------------------------------------------------\n'
        message = message0 + message1 + message2

        return message


def main():
    message = put_data(hostname, username, password, localfile_path, localfile_name, target_path, file_name)
    print(message)

    # 遅延処理
    time.sleep(1)


if __name__ == '__main__':
    main()
