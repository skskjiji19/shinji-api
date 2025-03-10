from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Shinji! Your API is live!"

# 🔥 Webhook機能を追加！ 🔥
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # 外部から送られてきたデータを受け取る
    if not data:
        return jsonify({"error": "No data received"}), 400

    # 受け取ったデータをログに記録（今後データ保存に拡張可能）
    print("Received data:", data)

    return jsonify({"message": "Data received successfully", "received_data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)