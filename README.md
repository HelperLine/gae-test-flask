
# Google App Engine - Test (Flask)

*GAE = Google App Engine*

<br/><br/>
### Basic Deploy flow

1. Type `gloud init` (you don't need to do this when the last deploy was with the same configuration)

2. Setup configuration 

3. Run `gloud app deploy` and confirm (check if the correct source/destination is configured!)

4. Use `gloud app deploy --no-promote` to launch a new version that does not receive any traffic.

`gloud app deploy` reference: <br/>
https://cloud.google.com/sdk/gcloud/reference/app/deploy

<br/><br/>
### Basic Flask Setup

Goal: Basic `app.yaml` for regular flask setup. Setup `standard` for now.

<br/>

App Engine Python Docs: <br/>
https://cloud.google.com/appengine/docs/python


`app.yaml` reference for standard environment: <br/>
https://cloud.google.com/appengine/docs/standard/python3/config/appref


`app.yaml` reference for flexible environment: <br/>
https://cloud.google.com/appengine/docs/flexible/python/reference/app-yaml

<br/><br/>
### Secure Environment Variables

Goal: Environment variables - idea: Setting them with Google Datastore. Since the App Engine app 
is automatically authenticated with the Datastore to its project, it is just a simple query

<br/>

Install datastore dependencies with `pip install google-cloud-datastore`.
Make sure to initialize a service account and download the authentication `json`
**after** you have set all permissions for that service account

Datastore idea source *(libraries deprecated but method still the same)*: <br/>
https://stackoverflow.com/questions/22669528/securely-storing-environment-variables-in-gae-with-app-yaml

Accessing Datastore in Python: <br/>
https://google-cloud-python.readthedocs.io/en/0.32.0/datastore/usage.html
