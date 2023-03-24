#!/bin/sh

rm -rf home/{event_data}

wget --content-disposition "https://www.dropbox.com/sh/4357vhm70xsdrjb/AACKunKpX4eGbNMa3woRoFMNa?dl=0"

unzip event_data.zip -x / -d home/event_data

rm event_data.zip
