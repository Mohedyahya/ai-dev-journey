# Day 11 - Smart Agent Project: Flask + HTML Templates
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Data sent to HTML template
    user = "Mohedyahya"
    agent_skills = [
        "Python Programming",
        "Customer Database",
        "File Handling",
        "Internet APIs",
        "Web Server (Flask)"
    ]
    
    return render_template(
        "index.html",
        username=user,
        skills=agent_skills
    )

if __name__ == "__main__":
    print("=" * 45)
    print("SMART AGENT: Day 11 - Flask Templates")
    print("Open: http://10.124.231.49:5000")
    print("=" * 45)
    app.run(host="0.0.0.0", port=5000, debug=True)

