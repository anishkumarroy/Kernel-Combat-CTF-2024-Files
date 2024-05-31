#!/bin/bash

# Directory containing the images
directory="images/"

# Get the list of images in the directory
images=$(ls "$directory")

# Loop through each image and compare it with others
for image1 in $images; do
    for image2 in $images; do
        if [[ $image1 != $image2 ]]; then
            difference=$(diff -q "$directory/$image1" "$directory/$image2" 2>&1)
            if [[ -n $difference ]]; then
                echo "Difference found between $image1 and $image2"
            fi
        fi
    done
done
