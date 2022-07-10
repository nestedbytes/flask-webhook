from flask import Flask, request

app = Flask(__name__)

@app.route('/hook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        return "Webhook received!"

app.run(debug=False)