#!/usr/bin/env/ bash

echo "========================================="
echo " COPYING NODERED PROJECT HUMIBOX TO REPO "
echo "========================================="

SOURCE="$HOME/.node-red/projects/humiBoxProject/"
DESTINATION="$HOME/Projects/humiBox/nodeRED/"

sudo cp -r "$SOURCE" "$DESTINATION"

echo "Deleting README.md"

sudo rm "$DESTINATION/humiBoxProject/README.md"

echo "Deleting .git/ directory in nodeRED project."

sudo rm -rf "$DESTINATION/humiBoxProject/.git/"

echo "Done"
