from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from difflib import get_close_matches  # For fuzzy matching

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key here
OPENAI_API_KEY = "your-openai-api-key"  # Replace with your actual OpenAI API key
openai.api_key = OPENAI_API_KEY  # Set API key globally

# Predefined FAQ Responses
faq_responses = {
    "do you provide bulk order discounts?": "Yes! We offer discounts on bulk orders. Please share your order quantity.",
    "what types of uniforms do you make?": "We manufacture school, corporate, hospital, and industrial uniforms.",
    "what is your delivery time?": "Our standard delivery time is 7-10 business days for bulk orders.",
    "what fabrics do you use?": "We use high-quality cotton, polyester, and blended fabrics based on customer preference.",
    "do you offer custom branding on uniforms?": "Yes, we offer embroidery and printing for company logos and branding.",
}

# Function to find the closest FAQ match
def get_faq_answer(user_message):
    user_message = user_message.lower()  # Convert input to lowercase
    matches = get_close_matches(user_message, faq_responses.keys(), n=1, cutoff=0.6)

    if matches:
        return faq_responses[matches[0]]  # Return closest matching answer
    return None  # No match found

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    # Step 1: Check predefined FAQ responses
    bot_reply = get_faq_answer(user_message)

    # Step 2: If no match, use GPT API
    if not bot_reply:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a chatbot for a uniform manufacturing company named Shubham Collection. Provide clear and professional answers about uniforms, pricing, bulk orders, and materials."},
                    {"role": "user", "content": user_message}
                ]
            )
            bot_reply = response.choices[0].message["content"]
        except Exception as e:
            bot_reply = "Please get in touch with us by send a message in contact us section."

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":  # Fixed incorrect `_main_` typo
    app.run(port=5000, debug=True)
