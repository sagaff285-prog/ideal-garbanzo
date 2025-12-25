#!/data/data/com.termux/files/usr/bin/python3
from flask import Flask, render_template, render_template_string, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Phone Calculator</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial; padding: 20px; background: #f0f0f0; }
            .container { max-width: 400px; margin: auto; background: white; padding: 20px; border-radius: 10px; }
            input, select, button { width: 100%; padding: 10px; margin: 10px 0; }
            .result { background: #e8f5e8; padding: 10px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📱 Phone Calculator</h1>
            <form method="post">
                <input type="number" step="any" name="num1" placeholder="First number" required>
                <select name="operation">
                    <option value="+">➕ Addition</option>
                    <option value="-">➖ Subtraction</option>
                    <option value="*">✖️ Multiplication</option>
                    <option value="/">➗ Division</option>
                </select>
                <input type="number" step="any" name="num2" placeholder="Second number" required>
                <button type="submit">Calculate</button>
            </form>
            {% if result is not none %}
            <div class="result">
                <h3>Result: {{ result }}</h3>
            </div>
            {% endif %}
            <hr>
            <h3>System Info</h3>
            <p>Directory: {{ dir }}</p>
            <p>Files: {{ file_count }} items</p>
        </div>
    </body>
    </html>
    '''

@app.route('/', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero!"
        else:
            result = "Invalid operation"
            
    except ValueError:
        result = "Invalid input"
    
    # Get system info
    current_dir = os.getcwd()
    file_count = len(os.listdir('.'))
    
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Phone Calculator</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial; padding: 20px; background: #f0f0f0; }
            .container { max-width: 400px; margin: auto; background: white; padding: 20px; border-radius: 10px; }
            input, select, button { width: 100%; padding: 10px; margin: 10px 0; }
            .result { background: #e8f5e8; padding: 10px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📱 Phone Calculator</h1>
            <form method="post">
                <input type="number" step="any" name="num1" value="{{ num1 }}" placeholder="First number" required>
                <select name="operation">
                    <option value="+" {% if operation == '+' %}selected{% endif %}>➕ Addition</option>
                    <option value="-" {% if operation == '-' %}selected{% endif %}>➖ Subtraction</option>
                    <option value="*" {% if operation == '*' %}selected{% endif %}>✖️ Multiplication</option>
                    <option value="/" {% if operation == '/' %}selected{% endif %}>➗ Division</option>
                </select>
                <input type="number" step="any" name="num2" value="{{ num2 }}" placeholder="Second number" required>
                <button type="submit">Calculate</button>
            </form>
            {% if result is not none %}
            <div class="result">
                <h3>Result: {{ result }}</h3>
                <p>{{ num1 }} {{ operation }} {{ num2 }} = {{ result }}</p>
            </div>
            {% endif %}
            <hr>
            <h3>System Info</h3>
            <p>Directory: {{ dir }}</p>
            <p>Files: {{ file_count }} items</p>
            <p><a href="/">New Calculation</a></p>
        </div>
    </body>
    </html>
    ''', result=result, num1=request.form['num1'], num2=request.form['num2'], 
         operation=request.form['operation'], dir=os.getcwd(), file_count=len(os.listdir('.')))

if __name__ == '__main__':
    print("Starting web calculator...")
    print("Open your phone browser and go to: http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)
