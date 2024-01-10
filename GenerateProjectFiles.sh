#!/bin/bash

python ./RunProject.py -e "../FlaxEngine/Binaries/Editor/Win64/Development/FlaxEditor.exe" -- -genProjectFiles

echo "Waiting for 10 seconds to open editor..."
sleep 10

