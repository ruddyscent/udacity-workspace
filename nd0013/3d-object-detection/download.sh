#!/bin/sh

rm -rf home/{dataset,results}

wget -O home/dataset --content-disposition "https://www.dropbox.com/sh/d4ahu5iqk2ozg5n/AABracy4CPze3MbT9qMM1_AQa?dl=0"

wget -O home/results --content-disposition "https://www.dropbox.com/sh/jyon55nrxk1ec4a/AAB5dlQRbTr_EvcOqT29GYa_a?dl=0"
