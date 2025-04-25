#!/usr/bin/env python3
"""
Stripe API Integration - Flask Server Example

This module demonstrates how to create a simple Flask server that integrates with 
Stripe API to fetch product information. It serves as an educational example of:
1. Building a REST API with Flask
2. Integrating with third-party services (Stripe)
3. Error handling and environment configuration
4. Cross-Origin Resource Sharing (CORS) setup
"""

# Standard library imports
import os

# Third-party imports
import flask
import stripe
from flask_cors import CORS
from flask import Flask, jsonify
from dotenv import load_dotenv

# CONFIGURATION SECTION
print("Starting Stripe API integration server...")

# Load environment variables from .env file
# This is a security best practice to avoid hardcoding sensitive information
load_dotenv()
print("Environment variables loaded from .env file")

# Initialize Flask application
app = flask.Flask(__name__)
print(f"Flask application initialized with name: {__name__}")

# Configure CORS (Cross-Origin Resource Sharing)
# This allows the specified frontend domains to access this API
CORS(app, resources={r"/*": {"origins": ['http://localhost:3000/', 'http://127.0.0.1:3000/']}})
print("CORS configured to allow requests from localhost:3000")

# Configure Stripe with API key
# The API key should be stored in the .env file as STRIPE_SECRET_KEY
stripe_key = os.getenv("STRIPE_SECRET_KEY")
if stripe_key:
    stripe.api_key = stripe_key
    print("Stripe API key loaded successfully")
else:
    print("WARNING: Stripe API key not found. Please check your .env file.")

# API ENDPOINTS
@app.route("/products", methods=["GET"])
def get_all_products():
    """
    Handle GET requests to /products endpoint
    
    This function:
    1. Fetches all active products from Stripe
    2. For each product, retrieves its price information
    3. Formats the data into a clean JSON structure
    4. Returns the formatted data to the client
    
    Returns:
        JSON: List of formatted products with their details
        or error message with 500 status code if something fails
    """
    print("\n--- Handling request to GET /products ---")
    
    try:
        print("Fetching active products from Stripe...")
        products = stripe.Product.list(active=True)
        print(f"Retrieved {len(products.data)} products from Stripe")

        # Format the products into a list of dictionaries for the frontend
        formatted_products = []
        
        print("Processing product data...")
        for index, product in enumerate(products.data):
            print(f"Processing product {index+1}/{len(products.data)}: {product.id}")
            
            # Get price information for the current product
            print(f"  Fetching price information for product: {product.id}")
            prices = stripe.Price.list(product=product.id, active=True).data
            
            price_amount = None
            if prices:
                # Convert price from cents to dollars
                price_amount = prices[0].unit_amount / 100
                print(f"  Product price: ${price_amount}")
            else:
                print("  No price information found for this product")
            
            # Create a formatted product object    
            formatted_product = {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "images": product.images,
                "price": price_amount
            }
            formatted_products.append(formatted_product)
            print(f"  Added product to response: {product.name}")
       
        print(f"Formatted Products (sample of first 2): {formatted_products[:2] if formatted_products else []}")
        print(f"Total products in response: {len(formatted_products)}")
        
        # Return the formatted products as JSON
        print("Returning successful response")
        return flask.jsonify(formatted_products)
    
    except stripe.error.StripeError as e:
        # Handle Stripe-specific errors
        print(f"Stripe API error occurred: {e.user_message}")
        return jsonify({"error": e.user_message}), 500
    
    except Exception as e:
        # Handle any unexpected errors
        error_message = f"Unexpected error: {str(e)}"
        print(error_message)
        return jsonify({"error": error_message}), 500
    
# SERVER EXECUTION
if __name__ == "__main__":
    print("\n=== Starting Flask development server ===")
    print("Access the API at: http://localhost:8000")
    print("Available endpoints:")
    print("  - GET /products : Retrieve all active products from Stripe")
    print("Press CTRL+C to stop the server")
    print("=======================================\n")
    
    # Run the Flask app in debug mode
    app.run(debug=True, port=8000)
