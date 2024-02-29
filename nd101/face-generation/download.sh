#!/bin/sh

rm -rf home/processed_celeba_small

wget -O processed-celeba-small.zip --content-disposition "https://www.dropbox.com/scl/fi/p0mdh3mgfjs0qgecxwiaz/processed-celeba-small.zip?rlkey=6o2roxmldnlvrlai2wji4irr0&dl=0"
unzip processed-celeba-small.zip -d home/
rm processed-celeba-small.zip
