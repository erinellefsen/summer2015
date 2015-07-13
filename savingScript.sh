#!/bin/bash
#Parameters: Directory name, P_low, P_high


ACCU=1
while [[ $ACCU -lt 50 ]];
do
    python2 saveVitals.py savedGraphs--$ACCU $1 .$ACCU $2 $3 $4
    let ACCU=ACCU+1
    echo "Graph Completed"
done
