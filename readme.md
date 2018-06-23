## Python Google AppEngine app


This app can be depoyed to appengine to log simple post messages. This app can be used test webhooks from Google pub sub.



## Running app locally

- `pip install -r requirements.txt`
- `export DEV=True`
- `python main.py`


## Deploy to Google AppEngine Standard

- `gcloud beat app deploy --quiet`


## See logs

- Get last `1 minute` logs of `request-post-app` of type `INFO`.
- Process the log using `jq` tool and print only logmessage.


```

gcloud beta logging read 'resource.type="gae_app" AND protoPayload.line.severity="INFO" AND resource.labels.module_id="request-post-app" ' --format=json --freshness 1m | jq -rnc --stream 'fromstream(1|truncate_stream(inputs)) | .protoPayload.line[0].logMessage'

```