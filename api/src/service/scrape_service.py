from flask import jsonify

def scrape_logic():
    # TODO: ロジックを書く。必要ライブラリをimportする。
    result = {
        "firstname": "佐藤",
        "lastname": "太郎",
    }
    return jsonify(result)