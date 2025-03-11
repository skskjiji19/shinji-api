import telebot  # Telegram Bot用ライブラリ
import os  # 環境変数を取得するためのライブラリ
from collections import deque  # 簡易的な記憶システム

# 🔹 環境変数からトークンを取得
TOKEN = os.getenv("TOKEN")

# 🔹 デバッグ用: TOKENの値をログに出力
print(f"DEBUG: TOKEN='{TOKEN}'")

# 🔹 トークンが設定されていない、またはスペースが含まれている場合、エラーを出す
if not TOKEN:
    raise ValueError("TOKENが設定されていません！")
if " " in TOKEN:
    raise ValueError("TOKENにスペースが含まれています！")

# 🔹 Botのインスタンスを作成
bot = telebot.TeleBot(TOKEN)

# 🔹 /start コマンドの処理
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "おう、シンジ！シバはここにいるぞ！")

# 🔹 Botを起動
bot.polling()
