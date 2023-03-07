#!/bin/sh

wget --content-disposition 'https://www.dropbox.com/sh/hsgby5aql3s7b69/AAD1DHaE04_zQp5QTsiUufwIa\?dl\=0'
unzip test_videos.zip -x / -d home/test_videos
wget --content-disposition https://www.dropbox.com/sh/6vtcwsa35b2ddt8/AABvTVkHogKL6s9WMxlnd3Kna?dl=0
unzip test_images.zip -x / -d home/test_images
rm test_videos.zip test_images.zip
