from flask import Flask
import pyrebase
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask_session import Session

firebaseConfig = {
        "apiKey": "AIzaSyCv2QujyROpTAi_if3UpiQ12Nq0Uaa6W-0",
        "authDomain": "quizapp-d9df7.firebaseapp.com",
        "projectId": "quizapp-d9df7",
        "storageBucket": "quizapp-d9df7.appspot.com",
        "messagingSenderId": "991096854411",
        "appId": "1:991096854411:web:ec9a2b69f55e3e0d0cc18e", 
        "databaseURL" : "https://quizapp-d9df7-default-rtdb.firebaseio.com/" 
    }

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates", static_url_path="")

    app.secret_key = "emovie"
    fb = pyrebase.initialize_app(firebaseConfig)
    app.auth = fb.auth()
    app.db = fb.database()

    from .routes import main
    
    app.register_blueprint(main)

    return app