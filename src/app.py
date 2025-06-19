from flask import Flask, request
import utils  # Your video processing code

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    url = request.json.get('url')
    # Call your processing functions from utils.py
    return {"status": "success"}