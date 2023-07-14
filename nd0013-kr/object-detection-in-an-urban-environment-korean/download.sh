#!/bin/sh

rm -rf home/data

wget --content-disposition "https://www.dropbox.com/sh/ewv4l9kjgubuwcj/AACF7HYEG4S5FJg-nPkFRSXya?dl=0"

unzip data.zip -x / -d home/data

rm data.zip
