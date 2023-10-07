import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
model_name = "gpt2"  # You can choose different models like "gpt2-medium" for more complexity
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Set the model to evaluation mode
model.eval()

# Initialize conversation history
conversation_history = []

# Simulate user authentication
def authenticate_user():
    # You can implement user authentication here, such as verifying credentials
    return True  # Return True for simplicity

# Banking functions
def check_account_balance():
    # Simulate checking account balance (replace with actual logic)
    return "Your account balance is ₹10,000."

def transfer_funds(to_account, amount):
    # Simulate fund transfer (replace with actual logic)
    return f"₹{amount} has been transferred to {to_account}."

def convert_currency(amount, source_currency, target_currency):
    # Simulate currency conversion (replace with actual logic)
    return f"₹{amount} in {source_currency} is equivalent to $10 in {target_currency}."

# Main conversation loop
print("Bank Assistant: Hello! How can I assist you today?")

while True:
    # User input
    user_input = input("You: ")

    # Add user input to conversation history
    conversation_history.append(f"You: {user_input}")

    # Tokenize and generate a response
    input_text = ' '.join(conversation_history)
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    response_ids = model.generate(input_ids, max_length=50, num_return_sequences=1)
    bot_response = tokenizer.decode(response_ids[0], skip_special_tokens=True)

    # Add bot response to conversation history
    conversation_history.append(f"Bank Assistant: {bot_response}")

    # Handle banking-related queries
    if "balance" in user_input.lower() and authenticate_user():
        response = check_account_balance()
    elif "transfer" in user_input.lower() and authenticate_user():
        # Parse recipient and amount from user input (replace with actual parsing)
        recipient = "Recipient's Account"  # Replace with parsed recipient
        amount = 1000  # Replace with parsed amount
        response = transfer_funds(recipient, amount)
    elif "convert" in user_input.lower():
        # Parse amount, source currency, and target currency from user input (replace with actual parsing)
        amount = 100  # Replace with parsed amount
        source_currency = "INR"  # Replace with parsed source currency
        target_currency = "USD"  # Replace with parsed target currency
        response = convert_currency(amount, source_currency, target_currency)
    else:
        response = "I'm sorry, I didn't understand your request."

    # Display the bot's response
    print(f"Bank Assistant: {response}")

    # Exit the loop if the user says goodbye
    if "goodbye" in user_input.lower():
        print("Bank Assistant: Goodbye! If you have more questions, feel free to ask.")
        break
