#!/bin/bash

echo
echo "Testing ..."
python -m pytest server.py
sleep 1

echo
echo "Helping ..."
python server.py -h
sleep 1

echo
echo "Server starting ..."
python server.py
#python server.py &
