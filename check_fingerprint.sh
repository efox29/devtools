#!/bin/bash

if [[ $# -gt 0 ]]
then
        
    MYEXT=${1##*.}  
    if [[ $MYEXT = "pem" || $MYEXT = "crt" ]]
    then
        openssl x509 -in $1 -noout -sha256 -fingerprint   
    else
        echo "Need pem or crt to fingerprint"
    fi

    # 
else
    echo "Missing Path to certificate"
fi