import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/prediction", methods=["POST"])
def prediction():
    return

@app.route("/image_ocr", methods=["POST"])
def ocr_enable():
    return
