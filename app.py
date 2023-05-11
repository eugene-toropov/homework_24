from flask import Flask

from config import Config
from views import main_bp
from db import db, migrate


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main_bp)
    return app
