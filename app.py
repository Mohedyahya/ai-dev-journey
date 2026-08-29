# Day 10 - Smart Agent Project: Flask Hello World
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>Smart Agent</title></head>
    <body style="text-align:center; font-family:Arial; margin-top:50px;">
        <h1>Smart Agent v1.0</h1>
        <p>Your AI assistant is running!</p>
        <hr>
        <p>Built with Python + Flask</p>
    </body>
    </html>
    """

@app.route("/about")
def about():
    return "<h2>About Smart Agent</h2><p>This is Week 2 of the Smart Agent Project.</p>"

@app.route("/status")
def status():
    return '{"status": "online", "version": "1.0"}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

