from flask import Flask # type: ignore

# Create a Flask app instance.
app = Flask(__name__)

# Define the root route.
@app.route('/')
def home():
    # Return a simple message.
    return "Hello, Docker! This is a Flask app running inside a container."

# Run the app when this script is executed directly.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
