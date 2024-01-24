#!/bin/sh

rm -rf home/landmark_images

wget --content-disposition "https://www.dropbox.com/scl/fo/cxdfg43nkqb3odyj7f89u/h?rlkey=xw0ddz3itlbovp8oleuvk4bkg&dl=0"
unzip landmark_images.zip -x / -d home/landmark_images
rm landmark_images.zip
