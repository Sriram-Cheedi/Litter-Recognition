# Code partially from https://www.kaggle.com/code/bouweceunen/garbage-detection-with-tensorflow/notebook
# Code to recreate label map from the TACO data set

import json
from google.protobuf import text_format
from object_detection.protos import string_int_label_map_pb2


def createLabelMap(ANNOTATION_FILE, OUT_FILE):
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

    with open(OUT_FILE, 'w') as f:
        f.write(text_format.MessageToString(labelmap))

    print('Label map witten to labelmap.pbtxt')



if __name__ == "__main__":
    # Requires path to .json file
    IN_PATH = "" 
    OUT_PATH = ""
    reconstruct(IN_PATH, OUT_PATH)
