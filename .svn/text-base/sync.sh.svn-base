#!/bin/bash

#kill python process
ps -ef | grep "python.*8001" | grep -v 'grep' | awk '{print $2}' | xargs kill -9

#delete nohup,session file
rm -f ./nohup.out
#rm -f ./sessions/*

#update svn
svn up

#restart python
if [ "nohup" == "$1" ];then    
  nohup python ./code.py 8001 &
else    
  python ./code.py 8001
fi

exit
