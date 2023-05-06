from flask import Flask

from views import main_bp
from db import db, migrate


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main_bp)
    return app
