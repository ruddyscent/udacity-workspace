#!/bin/sh

rm -rf home/{test_videos,test_images,camera_cal}

wget --content-disposition "https://www.dropbox.com/sh/tz39skinvugl8ja/AABZ928NBekhVqxKvITvWdLla?dl=0"
unzip test_videos.zip -x / -d home/test_videos

wget --content-disposition "https://www.dropbox.com/sh/emi5i89cspnxpcg/AAAr32itorGRcarTzgMiWYvXa?dl=0"
unzip test_images.zip -x / -d home/test_images

wget --content-disposition "https://www.dropbox.com/sh/2e6bhz0th77cq6b/AADLkzY_UG0qqPX5rmWGVcYja?dl=0"
unzip camera_cal.zip -x / -d home/camera_cal

rm {test_videos,test_images,camera_cal}.zip
