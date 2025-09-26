from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Backend service inside Kubernetes
BACKEND_URL = "http://note-backend:5000"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_note', methods=['POST'])
def add_note():
    title = request.form.get('title')
    content = request.form.get('content')
    if not title or not content:
        return jsonify({'error': 'Title and content required'}), 400
    try:
        resp = requests.post(f"{BACKEND_URL}/add_note", json={'title': title, 'content': content})
        return resp.content, resp.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/notes', methods=['GET'])
def notes():
    try:
        resp = requests.get(f"{BACKEND_URL}/get_notes")
        return resp.content, resp.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
