#!/usr/bin/python3
from flask import Flask
from flask_cors import CORS
import os
import router
from config import config
import db
from model import models
from migration import migration

def create_app():
    # Generate Flask App Instance
    app = Flask(__name__)

    # Read DB setting & Initialize
    app.config.from_object(config.Config) # TODO: config.config.Configを''でくくる？
    db.init_db(app)
    db.init_ma(app)
    db.init_seeder(app)

    # Register Router Instance
    app.register_blueprint(router.router)

    # Additional Configuration 
    app.config['JSON_AS_ASCII'] = False #日本語文字化け対策
    app.config["JSON_SORT_KEYS"] = False #ソートをそのまま
    CORS(
        app,
        resources = {
            r"/api/*": {"origins": ["http://localhost", "http://localhost:4200"]}
        }
    )
    return app

app = create_app()
if __name__ == "__main__":
    # Migrate before running App 
    if not os.path.exists('./migrations'):
        migration.initialize_migration()
    migration.execute_migration()
    # Comment out when unnecessary
    # migration.exec_seed()

    # Run Flask App
    app.run(host='0.0.0.0', debug=True, port=8080, threaded=True)
    