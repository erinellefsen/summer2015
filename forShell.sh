#!/bin/bash

COUNTER=1
while [[ $COUNTER -lt 5 ]]; 
do
    python2 saveVitals.py clusteredGraphs$COUNTER--0 $1 .0
    python2 saveVitals.py clusteredGraphs$COUNTER--20 $1 .2
    python2 saveVitals.py clusteredGraphs$COUNTER--40 $1 .4
    python2 saveVitals.py clusteredGraphs$COUNTER--60 $1 .6
    python2 saveVitals.py clusteredGraphs$COUNTER--80 $1 .8
    let COUNTER=COUNTER+1
done 



