#!/bin/sh

rm -rf home/{census,test_census}.csv

wget --content-disposition "https://www.dropbox.com/scl/fi/euzj73d1whlhgonfkvuds/test_census.csv?rlkey=c39zl072kr1l3ue79nr4yyzqn&dl=0" -P home

wget --content-disposition "https://www.dropbox.com/scl/fi/iqj0fyxaqne4g8mtoozdr/census.csv?rlkey=g45eh0aouj9jcriy1v0pjl61b&dl=0" -P home
