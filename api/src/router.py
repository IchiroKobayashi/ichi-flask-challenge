from flask import Blueprint
from controller import scrape_controller

router = Blueprint('router', __name__)

@router.route("/api/v1/scrape", methods=['GET'])
def api_v1_scrape():
    return scrape_controller.scrape()