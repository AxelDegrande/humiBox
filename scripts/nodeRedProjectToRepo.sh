#!/usr/bin/env/ bash

echo "========================================="
echo " COPYING NODERED PROJECT HUMIBOX TO REPO "
echo "========================================="

SOURCE="$HOME/.node-red/projects/humiBoxProject/"
DESTINATION="$HOME/Projects/humiBox/nodeRED/"

sudo cp -r "$SOURCE" "$DESTINATION"

echo "Deleting README.md"

sudo rm "$DESTINATION/humiBoxProject/README.md"

echo "Deleting .gitignore"

sudo rm "$DESTINATION/humiBoxProject/.gitignore"

echo "Deleting .git/ directory in nodeRED project."

sudo rm -rf "$DESTINATION/humiBoxProject/.git/"

echo "Deleting credentials."

sudo rm "$DESTINATION/humiBoxProject/flows_cred.json"
sudo rm "$DESTINATION/humiBoxProject/.flows_cred.json.backup"

echo "Deleting backups."

sudo rm "$DESTINATION/humiBoxProject/.flows.json.backup"

echo "Done"
