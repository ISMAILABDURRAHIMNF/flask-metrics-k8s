from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter("http_requests_total", "HTTP Total Request")

@app.route("/")
def main():
    return "Hello this is Ismail Abdurrahim task!", 200

@app.route("/metrics")
def metric():
    return generate_latest(), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
