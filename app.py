# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     # Get the user's message
#     user_message = request.form['message']

#     # Process the message and generate a response
#     # You can implement your own logic here
#     bot_response = 'Hello, you said: ' + user_message

#     # Return the bot's response as a JSON object
#     return jsonify({'message': bot_response})

# if __name__ == '__main__':
#     app.run()


from flask import Flask, render_template, request, jsonify


# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch


# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print(msg)
    return "Recieved your message"


# def get_Chat_response(text):

#     # Let's chat for 5 lines
#     for step in range(5):
#         # encode the new user input, add the eos_token and return a tensor in Pytorch
#         new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')

#         # append the new user input tokens to the chat history
#         bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

#         # generated a response while limiting the total chat history to 1000 tokens, 
#         chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

#         # pretty print last ouput tokens from bot
#         return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)


if __name__ == '__main__':
    app.run()