# Ichi Flask Challenge Application
アーキテクチャとして、

- フロントをTypescript(Angular)  
- バックエンドをPython(Flask)  
- インフラをDocker  

で開発したアプリケーション。  

APIの実行、CRUD、DBマイグレーション  
等ができるアーキテクチャ

# Infrastructure Description

Container nginx: Angular + Nginx  
Container api: Python3.7  
Container DB: MySQL5.7


# Features
Twitter APIを使用して、取得したツイートを元に、テキストを解析。  

マルコフ連鎖と形態素解析（Mecab）を用いて、そのユーザーがつぶやきそうなテキストを自動生成してフロント側に返すアプリケーション。

API実行時のロギングや認可設定、DBマイグレーション等、DevOpsにも意識したアーキテクチャです。  
Dockerアプリケーションにすることで、起動停止を簡単に行える。


# Requirement

* Python 3.7.10
* nginx 1.17.3
* Angular 11.2.6
* Node.js: 14.16.0
* Docker 20.10.5
* Docker Compose 1.16.1
* Flask 1.1.2
* Flask-Cors 3.0.10
* mecab-python3 1.0.3
* PyMySql 1.0.2
* python-dotenv 0.17.1
* markovify 0.9.0
* Flask-SQLAlchemy 2.5.1
* flask-marshmallow 0.14.0
* marshmallow-sqlalchemy 0.25.0
* Flask-Migrate 3.0.0
* tweepy 3.10.0
* Flask-Seeder 1.2.0

# Installation

Requirementで列挙したライブラリなどのインストール方法を説明する

## Pythonライブラリ準備
```bash
$ pip install Flask # 1.1.2
$ pip install Flask-Cors # 3.0.10
$ pip install python-dotenv # 0.17.1
$ pip install PyMySql # 1.0.2
$ pip install Flask-SQLAlchemy # 2.5.1
$ pip install flask-marshmallow # 0.14.0
$ pip install marshmallow-sqlalchemy # 0.25.0
$ pip install Flask-Migrate # 3.0.0
$ pip install Flask-Seeder # 1.2.0
```

## Augular準備
```bash
$ npm install -g @angular/cli
```


# Usage

```bash
$ git clone https://github.com/IchiroKobayashi/ichi-flask-challenge
$ cd ichi-flask-challenge
$ docker-compose up -d --remove-orphans
```

# Note

使用前にnginxとapiのDockerfileをビルドしておく。

```bash
$ cd ./ichi-flask-challenge
$ docker build -f ./docker/nginx/Dockerfile -t ichi-flask-challenge:nginx .
$ cd ./ichi-flask-challenge/docker/python
$ docker build .
```

# Author

* Ichiro Kobayashi
* seerged89@gmail.com


# License
"ichi-flask-challenge" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
