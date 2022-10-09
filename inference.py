import os
import json
from transformers import pipeline

def analytics_emo(x):
    data = classifier(x)[0]
    return data

if __name__ == "__main__":
    din = os.sys.argv[1]
    output_file = os.sys.argv[2]

    classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion", top_k=1)
    dout = analytics_emo(din)

    f2 = open(output_file, "w")
    # read the input data
    with open(din, "r") as f:
        line = f.readline()
        while line:
            dout = analytics_emo(line)    
            data_trunc = {}
            data_trunc["sentence"] = line
            data_trunc["sentiment"] = dout
            f2.write(json.dumps(data_trunc)+'\n')
            line = f.readline()
    f2.close()

        
