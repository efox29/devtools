#!/bin/bash

if [[ $# -gt 0 ]]
then
    
    # MYFILE_EXT= $MYFILE#*.
    MYEXT=${1##*.}  
    if [[ $MYEXT = "pem" ]]
    then
        openssl x509 -in $1 -noout -text
    elif [[ $MYEXT = "csr" ]]
    then
        openssl req -text -noout -verify -in $1
    fi
    # 
else
    echo "Missing Path to certificate"
fi