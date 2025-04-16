from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

responses = {
    "menu": {
        "keywords": ["menu", "burger", "price", "order"],
        "response": "Our menu:\n• Cheese Burger (Rs 99)\n• Jumbo Burger (Rs 149)\n• Mexican Burger (Rs 119)"
    },
    "delivery": {
        "keywords": ["delivery", "time"],
        "response": "Free delivery within 30 minutes. Available 11 AM to 10 PM daily."
    },
    "location": {
        "keywords": ["location", "address", "where"],
        "response": "Visit us at: [Near Narhe bus stop]. Open daily  7 PM to 11 PM."
    },
    "payment": {
        "keywords": ["payment", "pay", "cod"],
        "response": "We accept: Cash, Cards, UPI, and Digital Wallets"
    },
    "contact": {
        "keywords": ["contact", "phone", "help"],
        "response": "Contact: Phone:+91 9112916961, Email: manishladke09@gmail.com"
    },
    "recommend": {
        "keywords": ["recommend", "suggestion", "best", "popular", "special"],
        "response": "Based on our customers' favorites:\n• For Cheese Lovers: Cheese Burger\n• For Big Appetite: Jumbo Burger\n• For Spicy Food Fans: Mexican Burger\n\nToday's Special: Jumbo Burger Combo with Fries!"
    },
    "vegetarian": {
        "keywords": ["veg", "vegetarian", "plant"],
        "response": "For vegetarian options, we recommend:\n• Veg Supreme Burger\n• Paneer Tikka Burger\nAll served with fresh veggies and our special sauce!"
    },
    "spicy": {
        "keywords": ["spicy", "hot", "chilli"],
        "response": "For spicy food lovers:\n• Mexican Burger (Extra Hot)\n• Spicy Chicken Burger\nYou can customize spice levels as per your preference!"
    },
    "combo": {
        "keywords": ["combo", "meal", "package", "deal"],
        "response": "Today's Special Combos:\n• Family Pack: 3 Burgers + 2 Fries + Drinks\n• Student Meal: Burger + Fries + Drink\n• Party Pack: 5 Burgers + 3 Fries + 3 Drinks"
    }
}

def get_response(user_message):
    user_message = user_message.lower()
    
    for category, data in responses.items():
        if any(keyword in user_message for keyword in data["keywords"]):
            return data["response"]
    
    return "How can I help you? Ask me about our menu, recommendations, combos, or special deals!"

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        message = request.json.get('message', '').strip()
        if not message:
            return jsonify({"response": "Please enter a message"}), 400

        response = get_response(message)
        return jsonify({"response": response})

    except Exception:
        return jsonify({"response": "Sorry, something went wrong. Please try again."}), 500

if __name__ == '__main__':
    app.run(debug=True)