# Code partially from https://www.kaggle.com/code/bouweceunen/garbage-detection-with-tensorflow/notebook
# Code to recreate label map from the TACO data set

import json
from google.protobuf import text_format
from object_detection.protos import string_int_label_map_pb2


def createLabelMap():
    ANNOTATION_FILE = '/home/ryan/SEP/code/Reconstruction/TACO-20250119T094850Z-001/TACO/data/annotations.json'
    no_Of_Classes = 60
    
    with open(ANNOTATION_FILE) as jsonFile:
        data = json.load(jsonFile)
        
    categories = data['categories']
    
    print('Building label map from examples')

    labelmap = string_int_label_map_pb2.StringIntLabelMap()
    for idx,category in enumerate(categories):
        item = labelmap.item.add()
        # label map id 0 is reserved for the background label
        item.id = int(category['id'])+1
        item.name = category['name']

    with open('/home/ryan/SEP/code/Reconstruction/labelmap.pbtxt', 'w') as f:
        f.write(text_format.MessageToString(labelmap))

    print('Label map witten to labelmap.pbtxt')



createLabelMap()