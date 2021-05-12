from flask import Blueprint
from service.scrape_service import scrape_logic

scrape_app = Blueprint('scrape_app', __name__)

@scrape_app.route("/api/v1/scrape", methods=['GET'])
def scrape():
    return scrape_logic()