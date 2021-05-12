#!/usr/bin/python3
from flask import Flask, jsonify
from flask_cors import CORS
import router

app = Flask(__name__)
app.register_blueprint(router.router)
app.config['JSON_AS_ASCII'] = False #日本語文字化け対策
app.config["JSON_SORT_KEYS"] = False #ソートをそのまま
CORS(
    app,
    resources = {
        r"/api/*": {"origins": ["http://localhost", "http://localhost:4200"]}
    }
)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080, threaded=True)