import telebot  # Telegram Bot用ライブラリ
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

# 🔹 記憶システム（直近5つのメッセージを記憶する）
recent_messages = deque(maxlen=5)

@bot.message_handler(func=lambda message: True)  # すべてのメッセージを処理
def respond_to_message(message):
    recent_messages.append(message.text)  # メッセージを記憶
    response = responses.get(message.text, "それについてはまだ考え中だな。")
    bot.reply_to(message, f"おう、{response} そういうことだ。")

# 🔹 Botの起動
print("シバBotが起動中…")
bot.polling()
