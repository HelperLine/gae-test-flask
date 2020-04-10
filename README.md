
# GAE Test - Setup + Secure Environment Variables

*GAE = "Google App Engine"*

1. Basic `app.yaml` for regular flask setup. Setup `standard` for now.

2. Environment variables - idea: Setting them with Google Datastore. Since the App Engine app 
is automatically authenticated with the Datastore to its project, it is just a simple query

<br/>

### GAE Deploy

1. Type `gloud init`

2. Setup configuration 

3. Run `gloud app deploy` and confirm

<br/>

### Helpful Links

App Engine Python Docs: <br/>
https://cloud.google.com/appengine/docs/python


`app.yaml` reference for standard environment: <br/>
https://cloud.google.com/appengine/docs/standard/python3/config/appref


`app.yaml` reference for flexible environment: <br/>
https://cloud.google.com/appengine/docs/flexible/python/reference/app-yaml

<br/>

Install datastore dependencies with `pip install google.cloud`

Datastore idea source *(libraries deprecated but method still the same)*: <br/>
https://stackoverflow.com/questions/22669528/securely-storing-environment-variables-in-gae-with-app-yaml

Accessing Datastore in Python: <br/>
https://google-cloud-python.readthedocs.io/en/0.32.0/datastore/usage.html

<br/>

Testing the App (`--no-promote`): <br/>
https://cloud.google.com/appengine/docs/flexible/nodejs/testing-and-deploying-your-app
