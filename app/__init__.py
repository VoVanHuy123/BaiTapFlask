from flask import Flask


def create_app(config_class='config.Config'):
    app = Flask(__name__)

  
    return app