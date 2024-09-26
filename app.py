from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# OpenAI API Key
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_gpt():
    data = request.json
    prompt = data.get("prompt")
    
    # Interact with OpenAI's GPT
    response = openai.Completion.create(
        engine="text-davinci-003",  # or the model of your choice
        prompt=prompt,
        max_tokens=150
    )
    
    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == "__main__":
    app.run(debug=True)
