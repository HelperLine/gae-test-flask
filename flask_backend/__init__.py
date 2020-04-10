
# [START gae_python37_app]
from flask import Flask

from google.cloud import datastore
import os

app = Flask(__name__)


if os.getenv("ENVIRONMENT") != "production":
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service-account.json"

client = datastore.Client()

for name in ["SECRET_TOKEN"]:
    raw_query_result = client.query(kind='Secrets').add_filter('name', '=', 'SECRET_TOKEN').fetch()
    os.environ["SECRET_TOKEN"] = list(raw_query_result)[0]["value"]


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return dict(os.environ)
