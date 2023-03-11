#!/bin/sh

rm -rf home/pet_images

wget --content-disposition "https://www.dropbox.com/sh/ouh2nsh8h8dxe1r/AADm1w1FymfdwNUl3JQnsFOHa?dl=0"
unzip pet_images.zip -x / -d home/pet_images

rm pet_images.zip
