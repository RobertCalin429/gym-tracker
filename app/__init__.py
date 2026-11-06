from flask import Flask


def create_app():
    app = Flask(__name__)
    @app.route("/")
    def index():
        return app.send_static_file("index.html")
    
    return app