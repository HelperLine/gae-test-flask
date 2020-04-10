
# [START gae_python37_app]
from flask import Flask

try:
    from secrets import SECRET_TOKEN
except Exception as e:
    SECRET_TOKEN = "'secrets.py' does not exist"

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return f"Hello World! Token = '{SECRET_TOKEN}'"
