#!/bin/sh
PATH=/bin:/usr/bin:/sbin:/usr/sbin:/usr/local/bin
cd `dirname $0`
sh rtcd_p/unInstall.sh
sh rtcdControl/unInstall.sh
