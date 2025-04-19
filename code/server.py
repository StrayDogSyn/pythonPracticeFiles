import flask
import stripe
import os
from flask_cors import CORS
from flask import Flask, jsonify
from dotenv import load_dotenv
# I attempted to keep the example as simple as possible, focusing on the core functionality of fetching products from Stripe and formatting them for the frontend.
load_dotenv()  # Load environment variables from .env file

app = flask.Flask(__name__)
CORS(app, resources={r"/*": {"origins": ['http://localhost:3000/', 'http://127.0.0.1:3000/']}})  # Enable CORS for all routes


stripe.api_key = os.getenv("STRIPE_SECRET_KEY")  # Set your Stripe secret key from environment variables

@app.route("/products", methods=["GET"])
def get_all_products():
    
    # print("Fetching all products...")
    
    products = stripe.Product.list(active=True)  # Fetch all active products from Stripe
    
    # print(f"Products: {products}")

    formatted_products = []  # Format the products into a list of dictionaries
    
    for product in products.data:
        prices = stripe.Price.list(product=product.id, active=True).data
        price_amount = None
        if prices:
            price_amount = prices[0].unit_amount / 100
            
        formatted_product = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "images": product.images,
            "price": price_amount
        }
        formatted_products.append(formatted_product)
   
    print(f"Formatted Products: {formatted_products}")
    
    return flask.jsonify(formatted_products)  # Return the formatted products as JSON

if __name__ == "__main__":
    app.run(debug=True, port=8000)  # Run the Flask app in debug mode
