from flask import Blueprint
from controller import scrape_controller

router = Blueprint('router', __name__)

@router.route("/", methods=['GET'])
def hello_world():
    return "Hello World!!"

@router.route("/api/v1/scrape", methods=['GET'])
def api_v1_scrape():
    return scrape_controller.scrape()

@router.after_request
def after_request(response):
  # response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response