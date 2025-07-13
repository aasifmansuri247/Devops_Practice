from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h2 style='color:green;'>Hello from Flask running inside Docker!</h2><p>Containerized and working on port 5000</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)