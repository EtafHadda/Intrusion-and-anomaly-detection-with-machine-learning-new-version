
# Web attacks detection with machine learning
## About
Web attack detection using Machine Learning trained with your HTTP logs.

## Usage
### Encode your http logs and save the result into a csv file
```shell
$ python encode.py -a -l ./DATA/raw-http-logs-samples/access-2018-12-15.log -d ./DATA/labeled-data-samples/access-2018-12-15.csv
```

### Train a model and test the prediction
```shell
$ python train.py -a 'lr' -t ./DATA/labeled-data-samples/all.csv -v ./DATA/labeled-data-samples/access-2018-12-15.csv
```

### Make a prediction for a single log line
```shell
$ python predict.py -l '198.72.227.213 - - [16/Dec/2018:00:39:22 -0800] "GET /self.logs/access.log.2016-07-20.gz HTTP/1.1" 404 340 "-" "python-requests/2.18.4"'
```

### Make a prediction using a the REST API
#### Launch the API server 
In order to use the API to need first to launch it's server as the following
```shell
$ python3 -m uvicorn prediction_api:app --reload --host 0.0.0.0 --port 8000
```
#### Make a predciton request 
You can use the following code which based on Python 'requests' (the same in test_api.py) to make a prediction using the REST API
```python
import requests
import json
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}
data = {
    'http_log_line': '187.167.57.27 - - [15/Dec/2018:03:48:45 -0800] "GET /honeypot/Honeypot%20-%20Howto.pdf HTTP/1.1" 200 1279418 "http://www.secrepo.com/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/61.0.3163.128 Safari/534.24 XiaoMi/MiuiBrowser/9.6.0-Beta"'
}
response = requests.post('http://127.0.0.1:8000/predict', headers=headers, data=json.dumps(data))
print (response.text)
```
It will return the following:
``` python
{"prediction":"0","proba":"0.9975490196078431","log_line":"187.167.57.27 - - [15/Dec/2018:03:48:45 -0800] \"GET /honeypot/Honeypot%20-%20Howto.pdf HTTP/1.1\" 200 1279418 \"http://www.secrepo.com/\" \"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/61.0.3163.128 Safari/534.24 XiaoMi/MiuiBrowser/9.6.0-Beta\""}
```
## Documentation
Details could be found here:
<br>
http://enigmater.blogspot.fr/2017/03/intrusion-detection-based-on-supervised.html
