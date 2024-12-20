# this is the "web_app/__init__.py" file...

import os
from flask import Flask

from web_app.routes.comparison_routes import comparison_routes
from web_app.routes.home_routes import home_routes
from web_app.routes.inflation_routes import inflation_routes
from web_app.routes.interest_routes import interest_routes
from web_app.routes.treasury_yield_routes import treasury_yield_routes
from web_app.routes.unemployment_routes import unemployment_routes

SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") # set this to something else on production

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(comparison_routes)
    app.register_blueprint(home_routes)
    app.register_blueprint(inflation_routes)
    app.register_blueprint(interest_routes)
    app.register_blueprint(treasury_yield_routes)
    app.register_blueprint(unemployment_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)