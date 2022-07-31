
import configparser
import sys
import numpy as np
from sklearn import tree, linear_model
import argparse
import pickle
import time
import re
import sys
import csv
from sklearn.metrics import accuracy_score
from urllib.parse import *
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

config = configparser.ConfigParser()
config.sections()
config.read('settings.conf')

MODEL = config['MODEL']['model']
FEATURES = config['FEATURES']['features'].split(',')
REGEX = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (.+) "(.*?)" "(.*?)"'
SPECIAL_CHARS = "[$&+,:;=?@#|'<>.^*()%!-]"

def encode_single_log_line(log_line):
    log_line = log_line.replace(',','_')
    log_line = re.match(REGEX,log_line).groups()
    url = log_line[2]
    return_code = log_line[3]
    param_number = len(url.split('&'))
    url_length = len(url)
    size = str(log_line[4]).rstrip('\n')
    depth = sum(1 for c in url if c == '/')
    upper_cases = sum(1 for c in url if c.isupper())
    lower_cases = sum(1 for c in url if c.islower())
    special_chars = sum(1 for c in url if c in SPECIAL_CHARS)

    if '-' in size:
        size = 0
    else:
        size = int(size)
    if (int(return_code) > 0):
        log_line_data = {}
        log_line_data['size'] = int(size)
        log_line_data['param_number'] = int(param_number)
        log_line_data['length'] = int(url_length)
        log_line_data['return_code'] = int(return_code)
        log_line_data['upper_cases'] = int(upper_cases)
        log_line_data['lower_cases'] = int(lower_cases)
        log_line_data['special_chars'] = int(special_chars)
        log_line_data['depth'] = int(depth)

    else:
        log_line_data = None
    return url,log_line_data,return_code


def load_model(model_file):
    model = pickle.dump(model_file)
    return model
