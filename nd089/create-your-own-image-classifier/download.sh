#!/bin/sh

rm -rf home/flowers

wget --content-disposition "https://www.dropbox.com/sh/9pk4zwsmutrutdd/AADPAhvzCoe_KN23jtHz61FZa?dl=0"
unzip flowers.zip -x / -d home/flowers

rm flowers.zip
