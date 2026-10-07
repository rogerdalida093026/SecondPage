from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the homepage route
@app.route('/')
def home():
    return "<h1>Hello, World! Welcome to my Python Web App.</h1>"

# Run the app locally
if __name__ == '__main__':
    app.run(debug=True)
