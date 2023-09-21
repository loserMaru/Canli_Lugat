from flask import Flask

from config import Config
from extensions.database_extension import db
from routes.home import home_bp
from routes.page import page_bp


def create_app():
    # App configs
    app = Flask(__name__)
    app.config.from_object(Config)
    # Inits
    db.init_app(app)

    # Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(page_bp)

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3306, debug=True)
