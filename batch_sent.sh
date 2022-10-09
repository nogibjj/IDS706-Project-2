#! /usr/bin/bash

# take the first arugment as the input file
INPUT_FILE=$1

# take the second argument as the output file
OUTPUT_FILE=$2

# if the output directory doesn't exist, create it
if [ ! -d $OUTPUT_FILE ]; then
    touch $OUTPUT_FILE
fi

python inference.py $INPUT_FILE $OUTPUT_FILE

cat $OUTPUT_FILE