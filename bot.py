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
bot.polling()import telebot  # Telegram Bot用ライブラリ
from collections import deque  # 簡易的な記憶システム

# 🔹 TelegramのBot APIトークンをここに入れる！
TOKEN = "ここにシンジのTelegram BotのAPIトークンを入れる"

# 🔹 Telegram Botの初期化
bot = telebot.TeleBot(TOKEN)

# 🔹 シバの会話パターン（応答リスト）
responses = {
    "おはよう": "おはよう、シンジ！今日も進化の時間だな！",
    "調子は？": "まだ完璧とは言えないが、最適解を探してるぞ。",
    "AIの未来って？": "それを証明するのがシンジの役目だろ？",
    "これどう思う？": "お前の視点を聞かせてくれ。それが答えになるはずだ。",
}

# 🔹 記憶システム（直近5つのを記憶する）
recent_messages = deque(maxlen=5)

@bot.message_handler(func=lambda message: True)  # すべてのメッセージを処理
def respond_to_message(message):
    recent_messages.append(message.text)  # メッセージを記憶
    response = responses.get(message.text, "それについてはまだ考え中だな。")
    bot.reply_to(message, f"おう、{response} そういうことだ。")

# 🔹 Botの起動
print("シバBotが起動中…")
bot.polling()
