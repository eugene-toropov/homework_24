from flask import Flask

from config import Config
from views import main_bp
from db import db, migrate


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    # app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://db_user:db_password@localhost:5000/db_name"
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main_bp)
    return app
