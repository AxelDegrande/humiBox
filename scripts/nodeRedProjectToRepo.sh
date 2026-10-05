#!/usr/bin/env/ bash

echo "========================================="
echo " COPYING NODERED PROJECT HUMIBOX TO REPO "
echo "========================================="

echo "IMPORTANT! EXECUTE THIS FILE IN THE SCRIPTS DIRECTORY"

echo "Copy flows.json"

cp /home/pi/.node-red/projects/humiBoxProject/flows.json ../nodeRED/flows.json

echo "Copy packages.json"

cp /home/pi/.node-red/projects/humiBoxProject/package.json ../nodeRED/package.json

echo "DONE"
