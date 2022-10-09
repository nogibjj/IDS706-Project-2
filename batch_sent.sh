#! /usr/bin/bash

# take the first arugment as the input file
INPUT_FILE=$1

# take the second argument as the output file
OUTPUT_FILE=$2

# if the output directory doesn't exist, create it
if [ ! -d $OUTPUT_FILE ]; then
    touch $OUTPUT_FILE
fi

# go through each line in the input file and print it
while read line; do
    # ret=$(curl http://localhost:7860/api/analytics --data-raw "{\"data\":[$line]}" -X POST -H 'Content-Type: application/json')
    python inference.py "$line" $OUTPUT_FILE
    # python write_output.py "$ret" $OUTPUT_FILE "$line"
done < $INPUT_FILE

cat $OUTPUT_FILE