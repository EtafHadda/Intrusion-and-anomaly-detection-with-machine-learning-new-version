# About: predict.py
# Author: walid.daboubi@gmail.com
# Version: 1.3 - 2021/10/30
#python3 predict.py -l DATA/raw_data/predict.log -m MODELS/model_RandomForestClassifier.pkl
import json

from utilities import *

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--log_file', help = 'The log file  you want to assess',  required=True)
parser.add_argument('-m', '--model', help = 'The trained model',required=True )

args = vars(parser.parse_args())

log_file_name = args['log_file']
model_file=args['model']

with open("prediction_output.json", "r") as read_file:
    data_from_json = json.load(read_file)

log_file = open(log_file_name,'r')
index=0

for log_line in log_file:
    index += 1
    desc='there is no attack to be described'
    log_line=unquote_plus(log_line)
    url,encoded,return_code = encode_single_log_line(log_line)
    formatte_encoded = []
    for feature in FEATURES:
        formatte_encoded.append(encoded[feature])
    model = pickle.load(open(model_file, 'rb'))
    prediction = int(model.predict([formatte_encoded])[0])

    print(prediction)
    csv_file = open(r'regex_4_labels.csv', 'r')
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if re.search(row[2], url):
            attack = row[0]
            desc = row[1]

    data_from_json.append({"attack_prediction": prediction, "URL": url,"description":desc,"return_code":return_code,"log_record":log_line})

with open("prediction_output.json", "w") as write_file:
    json.dump(data_from_json, write_file, indent=2)

