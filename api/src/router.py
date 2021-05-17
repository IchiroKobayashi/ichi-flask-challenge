from flask import Blueprint, request
from controller import controllers
from logging import config
from json import load
import auth
import logger

router = Blueprint('router', __name__)
with open("./config/logging.json", "r", encoding="utf-8") as f:
    config.dictConfig(load(f))

@router.route("/", methods=['GET'])
@logger.http_request_logging
@auth.requires_auth
def hello_world():
    return "Hello World!!"

@router.route("/api/v1/scrape/getTweetsById", methods=['GET'])
@logger.http_request_logging
@auth.requires_auth
def scrape_get_tweets_by_id():
    account_id = request.args.get('twitterUserName', '', type=str)
    limit = request.args.get('limit', '', type=int)
    return controllers.scrape_by_id(account_id, limit)

@router.route("/api/v1/scrape/getHondaTweets", methods=['GET'])
@logger.http_request_logging
@auth.requires_auth
def scrape_get_honda_tweets():
    limit = request.args.get('limit', '', type=int)
    return controllers.scrape_honda(limit)

@router.route("/api/v1/users/getUserList", methods=['GET'])
@logger.http_request_logging
@auth.requires_auth
def users_get_user_list():
    return controllers.get_user()

@router.after_request
def after_request(response):
    # response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response