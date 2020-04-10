
# Google App Engine Test - Setup + Secure Environmen Variables

Basic `app.yaml` for regular flask setup. Setup `standard` for now.

Environment variables - idea: Setting them with Google Datastore. Since the App Engine app 
is automatically authenticated with the Datastore to its project, it is just a simple query

<br/>

### GAE Deploy

1. Type `gloud init`

2. Setup configuration 

3. Run `gloud app deploy` and confirm

<br/>

### Helpful Links

App Engine Python Docs:
https://cloud.google.com/appengine/docs/python

`app.yaml` reference for standard environment:
https://cloud.google.com/appengine/docs/standard/python3/config/appref

`app.yaml` reference for flexible environment:
https://cloud.google.com/appengine/docs/flexible/python/reference/app-yaml

<br/>

Install datastore dependencies with `pip install google.cloud`

Datastore idea source *(libraries deprecated but method still the same)*:
https://stackoverflow.com/questions/22669528/securely-storing-environment-variables-in-gae-with-app-yaml

Accessing Datastore in Python:
https://google-cloud-python.readthedocs.io/en/0.32.0/datastore/usage.html

<br/>

Testing the App (`--no-promote`):
https://cloud.google.com/appengine/docs/flexible/nodejs/testing-and-deploying-your-app
