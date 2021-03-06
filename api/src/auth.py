from flask import request
from functools import wraps

def requires_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization", None)
        # TODO: 認証処理
        print(auth)
        print('認証デコレータで関数パワーアップした')
        return func(*args, **kwargs)
    return wrapper