from flask import Flask, render_template, request, jsonify
from granite_model.load_model import tokenizer, model
from data.dummy_health_data import get_dashboard_data
import torch
from waitress import serve

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/data')
def data():
    return jsonify(get_dashboard_data())


@app.route('/dashboard')
def dashboard():
    data = get_dashboard_data()
    return render_template('dashboard.html', **data)

@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_message = request.json['message']
        inputs = tokenizer(user_message, return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=150)
        reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return jsonify({"response": reply.split("Assistant:")[-1].strip()})
    except Exception as e:
        return jsonify({"response": f"❌ Error: {str(e)}"})




if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)

