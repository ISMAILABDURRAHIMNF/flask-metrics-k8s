from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter("http_requests_total", "HTTP Total Request")

@app.route("/")
def main():
    REQUEST_COUNT.inc()
    return "Hello this is Ismail Abdurrahim task!", 200
    
@app.route("/metrics")
def metric():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
