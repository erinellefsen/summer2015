#!/bin/bash

COUNTER=1
while [[ $COUNTER -lt 10 ]]; 
do
    python2 saveVitals.py clusteredGraphs$COUNTER--0 $1 .0
    python2 saveVitals.py clusteredGraphs$COUNTER--20 $1 .2
    python2 saveVitals.py clusteredGraphs$COUNTER--40 $1 .4
    python2 saveVitals.py clusteredGraphs$COUNTER--60 $1 .6
    python2 saveVitals.py clusteredGraphs$COUNTER--80 $1 .8
    echo $COUNTER
    let COUNTER=COUNTER+1
done 


python2 saveVitals.py clusteredGraphs$COUNTER--0 $1 .0
python2 saveVitals.py clusteredGraphs$COUNTER--2 $1 .02
python2 saveVitals.py clusteredGraphs$COUNTER--4 $1 .04
python2 saveVitals.py clusteredGraphs$COUNTER--6 $1 .06
python2 saveVitals.py clusteredGraphs$COUNTER--8 $1 .08
python2 saveVitals.py clusteredGraphs$COUNTER--10 $1 .10
python2 saveVitals.py clusteredGraphs$COUNTER--12 $1 .12
python2 saveVitals.py clusteredGraphs$COUNTER--14 $1 .14
python2 saveVitals.py clusteredGraphs$COUNTER--16 $1 .16
python2 saveVitals.py clusteredGraphs$COUNTER--18 $1 .18
python2 saveVitals.py clusteredGraphs$COUNTER--20 $1 .20
python2 saveVitals.py clusteredGraphs$COUNTER--22 $1 .22
python2 saveVitals.py clusteredGraphs$COUNTER--24 $1 .24
python2 saveVitals.py clusteredGraphs$COUNTER--26 $1 .26
python2 saveVitals.py clusteredGraphs$COUNTER--28 $1 .28
python2 saveVitals.py clusteredGraphs$COUNTER--30 $1 .30
python2 saveVitals.py clusteredGraphs$COUNTER--32 $1 .32
python2 saveVitals.py clusteredGraphs$COUNTER--34 $1 .34
python2 saveVitals.py clusteredGraphs$COUNTER--36 $1 .36
python2 saveVitals.py clusteredGraphs$COUNTER--38 $1 .38
python2 saveVitals.py clusteredGraphs$COUNTER--40 $1 .40
python2 saveVitals.py clusteredGraphs$COUNTER--42 $1 .42
python2 saveVitals.py clusteredGraphs$COUNTER--44 $1 .44
python2 saveVitals.py clusteredGraphs$COUNTER--46 $1 .46
python2 saveVitals.py clusteredGraphs$COUNTER--48 $1 .48
python2 saveVitals.py clusteredGraphs$COUNTER--50 $1 .40
python2 saveVitals.py clusteredGraphs$COUNTER--52 $1 .52
python2 saveVitals.py clusteredGraphs$COUNTER--54 $1 .54
python2 saveVitals.py clusteredGraphs$COUNTER--56 $1 .56
python2 saveVitals.py clusteredGraphs$COUNTER--58 $1 .58
python2 saveVitals.py clusteredGraphs$COUNTER--60 $1 .60
python2 saveVitals.py clusteredGraphs$COUNTER--62 $1 .62
python2 saveVitals.py clusteredGraphs$COUNTER--64 $1 .64
python2 saveVitals.py clusteredGraphs$COUNTER--66 $1 .66
python2 saveVitals.py clusteredGraphs$COUNTER--68 $1 .68
python2 saveVitals.py clusteredGraphs$COUNTER--70 $1 .70
python2 saveVitals.py clusteredGraphs$COUNTER--72 $1 .72
python2 saveVitals.py clusteredGraphs$COUNTER--74 $1 .74
python2 saveVitals.py clusteredGraphs$COUNTER--76 $1 .76
python2 saveVitals.py clusteredGraphs$COUNTER--78 $1 .78
python2 saveVitals.py clusteredGraphs$COUNTER--80 $1 .80
python2 saveVitals.py clusteredGraphs$COUNTER--82 $1 .82
python2 saveVitals.py clusteredGraphs$COUNTER--84 $1 .84
python2 saveVitals.py clusteredGraphs$COUNTER--86 $1 .86
python2 saveVitals.py clusteredGraphs$COUNTER--88 $1 .88
python2 saveVitals.py clusteredGraphs$COUNTER--90 $1 .90
python2 saveVitals.py clusteredGraphs$COUNTER--92 $1 .92
python2 saveVitals.py clusteredGraphs$COUNTER--94 $1 .94
python2 saveVitals.py clusteredGraphs$COUNTER--96 $1 .96
python2 saveVitals.py clusteredGraphs$COUNTER--98 $1 .98



