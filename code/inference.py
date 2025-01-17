# Dependency Requirements:
# Dependencies from Colab (tf, keras, protobuf etc)
# Distro
# sudo apt-get dist-upgrade
# ------------------------------------
# Tensorflow
# sudo apt-get install libatlas-base-dev (needed for tf)
# pip3 install tensorflow (version from colab)
# sudo pip3 install pillow lxml jupyter matplotlib cython
# sudo apt-get install python-tk
# ------------------------------------
# OpenCV
# sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
# sudo apt-get install libavcodec-dev libavformat-dev libwscale-dev lib4l-dev
# sudo apt-get install libxvidcore-dev libx264-dev
# sudo apt-get install qt4-dev-tools
# sudo apt-get libatlas-base-dev
# pip3 install opencv-python


# Unsure
# They install the tensorflow models github
# and point the python path at it
# Then they install a .tar.gz model from the model library and get the .pb files from there

# Import packages and utilities
import os
import cv2
import tensorflow as tf
from picamera2 import Picamera2

MODEL = 'ssd_mobilenet_v2_taco_2018_03_29.pb'
MODELPATH = 'PATH_TO_PB_MODEL'
DATAPATH = 'PATH_TO_TACO/data'

# Reconstruct frozen graph from .pb model
def reconstruct(pb_path):
    if not os.path.isfile(pb_path):
        print("Error: %s not found" % pb_path)

    print("Reconstructing Tensorflow model")
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.compat.v1.GraphDef()
        with tf.io.gfile.GFile(pb_path, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
    print("Success!")
    return detection_graph

# Reconstruct label pbtxt file from TACO data
def labelMap(data_path):
    ANNOTATIONS_FILE = os.path.join(DATAPATH, 'annotations.json')
    noOfClasses = 60
    
    with open(ANNOTATIONS_FILE) as json_file:
        data = json.load(json_file)
        
    classes = data['categories']
    
    #Building label map from examples
    
    lblMap = string_int_label_map_pb2.StringIntLabelMap()
    for idx, category in enumerate(classes):
        item = labelMap.item.add()
        # label map id 0 is reserved for the background label
        item.id = int(category['id'])+1
        item.name = category['name']
        
    with open('./labelmap.pbtxt', 'w') as f:
        #WORKING HERE
        return

        
    return

# Extracts the object from the image
def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
#Below has been commented out, if you want to print each sighting of an object to the console you can uncomment below     
#print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects: 
                objectInfo.append([box,className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    
    return img,objectInfo



# Need to reconstruct frozen graph from .pb
# Need to create label file from TACO labels
# Ensures frozen graph has been recreated and label map available
def initialise():
    frozenGraph = reconstruct(MODELPATH)
    classNames = labelMap(DATAPATH)
    
    
    
    return


if __name__ == '__main__':
    initialise()
    
    # Start the PiCam
    picam = Picamera2()
    picam.configure(picam.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
    picam.start()
    
    # Loop that determines what happens when an object is detected
    while True:
        # Gets an image from the PiCam
        img = picam.capture_array("main")
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        # Performs detection on the image and extracts the object
        res, info = getObjects()
        # Shows labelled image on screen
        cv2.imshow("Detection Output", img)
        
        # Waits 200 milliseconds to check for escape input 
        kill = cv2.waitKey(200)
        if kill == 27: # Esc key kills process
            picam.stop()
            cv2.destroyAllWindows()
            break
        
    
    
    
    
# TWO OPTIONS
# 1) Adapt code found at link
# 2) Adapt prewritten code and take frames and pass into detect


# I HAVE
# pb model (need reconstruct method)
# labels to create a txtpb











