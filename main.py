import os
from flask import Flask

from init import db, ma, bcrypt, jwt # import from init.py

def create_app(): # create the flask within a def
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)

    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    from controllers.card_controller import cards_bp
    app.register_blueprint(cards_bp)

    # changes
    
    return app