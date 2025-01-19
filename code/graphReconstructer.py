# Code to reconstruct the frozen graph detection from our incomplete .pb file
# Inspired and borrowed from https://www.kaggle.com/code/bouweceunen/garbage-detection-with-tensorflow/notebook
import os
import tensorflow as tf

# Reconstructs frozen graph from .pb file
def reconstruct(PATH_TO_INPB, PATH_OUT):
    if not os.path.isfile(PATH_TO_INPB):
        print("Error: %s not found" % PATH_TO_INPB)

    print("Reconstructing Tensorflow model")
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.compat.v1.GraphDef()
        with tf.io.gfile.GFile(PATH_TO_INPB, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
    print("Success!")
    
    with detection_graph.as_default():
        tf.io.write_graph(
            detection_graph.as_graph_def(),
            logdir=os.path.dirname(PATH_OUT),
            name=os.path.basename(PATH_OUT),
            as_text=False
        )
        
    print("Graph successfully saved at %s" % PATH_OUT)
    
    return detection_graph



if __name__ == "__main__":
    # Requires path to incomplete pb file
    IN_PATH = "/home/ryan/SEP/code/Reconstruction/TACO-20250119T094850Z-001/TACO/ssd_mobilenet_v2_taco_2018_03_29.pb" 
    OUT_PATH = "/home/ryan/SEP/code/Reconstruction/TACO-20250119T094850Z-001/TACO/reconstructed_TACO_graph.pb"
    reconstruct(IN_PATH, OUT_PATH)
    
