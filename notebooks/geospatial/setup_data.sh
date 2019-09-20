#!/bin/bash
# Download the datasets used in the ML notebooks to correct relative_paths (../input/...)

set -e

if [ -d input ]
then
    exit 0
fi

mkdir -p input

DATASETS="alexisbcook/geospatial-learn-course-data"

for slug in $DATASETS
do
    name=`echo $slug | cut -d '/' -f 2`
    dest="input/$name"
    mkdir -p $dest
    kaggle d download -p $dest --unzip $slug
done