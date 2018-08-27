#!/bin/sh

psql -e -d test -c "\\COPY (TABLE rustweets.tweets ORDER BY tweet_id) TO 'dump.csv' WITH ( HEADER true, FORMAT csv );"

split --verbose -C 100MB --numeric-suffixes --additional-suffix=.csv ./dump.csv rustweets_
rm -v dump.csv;

HEADER=$(head -n1 rustweets_00.csv)
for i in $(seq -w 1 11); do
	FILE="rustweets_$i.csv"
	mv "$FILE" /tmp/
	echo -n "$HEADER\n" > "$FILE"
	cat "/tmp/$FILE" >> "$FILE"
done;

mv -v rustweets* ../
