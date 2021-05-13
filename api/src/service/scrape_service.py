from flask import jsonify
from .. import settings
import subprocess

API_KEY = settings.AP
path = 'text_editor.py'

def scrape_logic():
    # TODO: ロジックを書く。必要ライブラリをimportする。
    result = {
        "firstname": "佐藤",
        "lastname": "太郎",
    }
    subprocess('python %s' % path)
    return jsonify(result)