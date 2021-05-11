import pymysql

def getConnection():
    return pymysql.connect(
        host='db:3306',# TODO: 正しいか確認する
        user='local',
        password='local',
        db='flask-challenge',
        charset='utf8mb4',
        collation='utf8_unicode_ci',
        parseTime='true',
        cursorclass=pymysql.cursors.DictCursor,
    )