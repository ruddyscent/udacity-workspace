#!/bin/sh

rm -rf home/data

wget --content-disposition "https://www.dropbox.com/sh/zv53z6nj7mixxu0/AABh4zo8P_Qc4aAjafotaXj3a?dl=0"
unzip data.zip -x / -d home/data

rm data.zip
