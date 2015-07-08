#!/bin/bash
#Parameters: Directory name, P_low, P_high


ACCU=50
while [[ $ACCU -lt 100 ]];
do
    python2 saveVitals.py clusteredGraphs--$ACCU $1 .$ACCU $2 $3
    let ACCU=ACCU+1
done
