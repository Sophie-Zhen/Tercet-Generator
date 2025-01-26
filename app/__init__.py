from flask import Flask, send_from_directory
from flask_cors import CORS
import os

def create_app(config=None):
    app = Flask(__name__)
    CORS(app)
    
    if config:
        app.config.update(config)
    
    from .api import bp as api_bp
    app.register_blueprint(api_bp)

    @app.route('/')
    def serve_frontend():
        return send_from_directory('templates', 'index.html')

    @app.route('/<path:filename>')
    def serve_static(filename):
        return send_from_directory('static', filename)
    
    return app
