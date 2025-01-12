from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')  # Ensure you have an index.html in the templates folder

# Other routes can be added here as necessary

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Listen on all IPs (0.0.0.0) and port 5000
