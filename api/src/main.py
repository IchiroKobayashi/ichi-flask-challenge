#!/usr/bin/python3
from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(
    app,
    resources = {
        r"/api/*": {"origins": ["http://localhost", "http://localhost:4200"]}
    }
)

@app.route("/", methods=['GET'])
def main():
    return "Hello World!!"

@app.route("/api/v1/scrape", methods=['GET'])
def scrape():
    result = {
        "firstname": "佐藤",
        "lastname": "太郎",
    }
    return jsonify(result)

@app.after_request
def after_request(response):
  # response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080, threaded=True)