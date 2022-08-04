
# _**Webhawk - The New Version**_
#### Paper title: Offline Log Analysis For Apache Web Servers Using Machine Learning


## About
**Webhawk - the new  version:**  is a Machine Learning Web attacks detection tool. It uses apache web logs as training data and pre-process them before training the model. Preprocessing includes Feature Engineerung and Data Labeling wich is done automatically using regular expressions. In training phase, the tool choose the training algorithm with the highest accuracy and produce its model. After that, testing is conducted py predicting many apache logs and writing them in a json file which will be the return value of the api when frontend application contact with the tool. Web attacks included right now are:
- SQL injection. 
- Cross Site Scripting(XSS)
- Directory Traversal Attack.
## Usage
### Create a settings.conf file
Rename a copy from settings_template.conf to settings.conf and  fill it with the required parameters as the following:
```shell
[MODEL]
model:MODELS/the_model_you_will_train.pkl
[FEATURES]
features:length,param_number,return_code,size,upper_cases,lower_cases,special_chars,depth
```

### process your http logs and save the result into a csv file
```shell
$ python3 process.py  -l ./DATA/raw_data/dataset.log -d ./DATA/labeled_data/dataset.csv
```

### Train a model and predict the testing data to get accuracy
Use the output of process.py which is dataset.csv as an input for train.py
```shell
$ python3 train.py  -l ./DATA/labeled_data/dataset.csv 
```

### Make a prediction for file to test your results
Use the output model of train.py and specify the file which have logs to be predicted.
```shell
$ python3 predict.py -l ./DATA/raw_data/predict.log -m ./MODELS/model_RandomForestClassifier.pkl
```

### REST API
#### Launch the API server
In order to use the API to need first to launch it's server as the following
```shell
$ python3 -m uvicorn api:app --reload
```

It will return the following: (this output is just for one line)
``` python
[
  {
    "index": 2,
    "attack_prediction": 1,
    "URL": "GET /main9.php?name1=admin' or 1=1/* HTTP/1.1",
    "description": "sql injection attempts",
    "return_code": "200"
  }]
  ```

## Used sample data
The data that used in this project is places in this url https://drive.google.com/drive/folders/1fq_1zBGumADJ_bBcmfHnAflT_gjGsIgc?usp=sharing , please put dataset.log in DATA/raw_data folder and dataset.csv file in Data/labeled_data folder.

## Documentation
Details on how this tools is build could be found at:


## The new version is done by:
- **Etaf M. Abu Hadda etafabuhadda18@gmail.com**
- **Hala M. Abu Sada habusaada@smail.ucas.edu.ps**
- **Eman S. Sallouha esallouha@smail.ucas.edu.ps**

#### Last update in : 1/8/2022
