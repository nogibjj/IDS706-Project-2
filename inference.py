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
    
    data_trunc = {}
    data_trunc["sentence"] = din
    data_trunc["sentiment"] = dout

    with open(output_file, 'a') as f:
        f.write(json.dumps(data_trunc)+'\n')
