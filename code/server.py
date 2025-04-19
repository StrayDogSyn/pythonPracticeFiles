import flask
import stripe
import flask_cors import CORS
from dotenv import load_dotenv

load_dotenv{}  # Load environment variables from .env file

app = flask.Flask(__name__)
CORS(app, resources={r"/*": {"origins": ['http://localhost:3000/', 'http://127.0.0.1:3000/']}})  # Enable CORS for all routes

if __name__ == "__main__":
    app.run(debug=True, port=8000)  # Run the Flask app in debug mode  
