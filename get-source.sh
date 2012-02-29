#!/bin/sh
p=closure-stylesheets
fn=$p
svn=http://$p.googlecode.com/svn/trunk
dl="https://code.google.com/p/$p/downloads/list?can=2&colspec=Filename"

set -x
set -e

html() {
	if [ -z "$html" ]; then
		html=$(lynx -width 1200 -dump -nolist "$dl")
	fi
	echo "$html" | tee debug.log
}

date=$(html | perl -ne '/'$fn'-(\d+).+jar/and print $1 and exit')
test -n "$date"

echo "Release: $date"

exit 1

d=$p-$date
if [ ! -d "$d" ]; then
	svn export -q $svn@$rev $p-$date
fi

t=$d.tar.bz2
if [ ! -f "$t" ]; then
	tar -cjf $t --exclude-vcs $d
fi
