#!/usr/bin/python3
from flask import Flask, jsonify
from flask_cors import CORS
import db

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #日本語文字化け対策
app.config["JSON_SORT_KEYS"] = False #ソートをそのまま
CORS(
    app,
    resources = {
        r"/api/*": {"origins": ["http://localhost", "http://localhost:4200"]}
    }
)

@app.route("/", methods=['GET'])
def main():
    return "Hello World!!"

@app.route("/create/<name>", methods=['GET'])
def create(name):
    db = db.getConnection()
    cur = db.cursor()
    sql = "select * from members"
    cur.execute(sql)
    members = cur.fetchall()
    cur.close()
    db.close()
    return jsonify({
            'status':'OK',
            'members':members
        })


@app.route("/api/v1/scrape", methods=['GET'])
def scrape():
    # TODO: ロジックを書く。必要ライブラリをimportする。
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