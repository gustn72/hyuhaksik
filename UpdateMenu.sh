#!/bin/sh
RootDir="/volume1/web/dj"
LOG="${RootDir}/log/UpdateMenu.log"
echo 'UpdateMenu!!!'
run_time=`date`
echo "Run time - $run_time" >> ${LOG}

python3 ${RootDir}/hyuhaksik/bstest.py>>${LOG}
echo "If you have any issue check log - $LOG"
echo 'UpdateMenu Finished'
