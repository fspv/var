#!/bin/bash -x

# Example:
# time parallel -j 32 bash resize.sh "{}" < imgs_list.txt

minimumWidth=1024
minimumHeight=1024

imageWidth=$(identify -format "%w" "$1")
imageHeight=$(identify -format "%h" "$1")

if [ "$imageWidth" -gt "$minimumWidth" ] || [ "$imageHeight" -gt "$minimumHeight" ]; then
    mogrify -resize ''"$minimumWidth"x"$minimumHeight"'' -strip $1
fi
