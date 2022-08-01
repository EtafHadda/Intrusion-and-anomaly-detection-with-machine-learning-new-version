
# About: Artificailly generate labeled data starting form raw http log file by adding rule based tags
# Author: walid.daboubi@gmail.com
# Version: 1.3 - 2021/10/30

#	A sample of lableled data:
# 	url_length,param_number,return_code,label, http_query
# 	49,1,404,1,GET /honeypot/bsidesdfw%20-%202014.ipynb HTTP/1.1
#       Label could be 1 (attack detected) or 0 (no attack detected)

# A HTTP LOG LINE SAMPLE
# 182.74.246.198 - - [01/Mar/2017:02:18:36 -0800] "GET /bootstrap/img/favicon.ico HTTP/1.1" 200 589 "http://www.secrepo.com/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"

from utilities import *

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--log_file', help = 'The raw http log file', required = True)
parser.add_argument('-d', '--dest_file', help = 'Destination to store the resulting csv file', required = True)

args = vars(parser.parse_args())

log_file = args['log_file']
dest_file =args['dest_file']


# Encode all the data in http log file (access_log)
def encode_log_file(log_file):
	data = {}
	log_file = open(log_file,'r')
	for log_line in log_file:
		log_line=unquote_plus(log_line)
		url,log_line_data,return_code=encode_single_log_line(log_line)
		if log_line_data != None:
			data[url] = log_line_data
	return data


def encode_single_line(single_line,features):
	encoded = ""
	for feature in features:
		encoded += str(single_line[feature]) + ','
	return encoded



def save_encoded_data(data,encoded_data_file):
	for w in data:
		attack='0'
		with open('regex_4_labels.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				if re.search(row[2], w.lower()):
					attack = row[0]
		data_row = encode_single_line(data[w],FEATURES) + attack + ',' + w + '\n'
		encoded_data_file.write(data_row)
	print (str(len(data)) + ' rows have successfully saved to ' + dest_file)

save_encoded_data(encode_log_file(log_file),open(dest_file, 'w'))




