import codecs
import csv
import sqlite3
import os
import re
import time

#   Read IRAhandle_tweets_1.csv through IRAhandle_tweets_9.csv
#   and generate sqlite database IRAhandle_tweets.db
#
# fields are the same, noting
#   'content' is unicode;
#   'publish_date' and 'harvested_date' are reformatted to yyyy/mm/dd hh:mm
#    so that string compares will work.
#   'publish_time' is added; this is publish_date converted to seconds.
#     I'm assuming the times in the csv are all UTC (pending issue #9)
#   'external_author_id' field is a mix of large integers, and large
#    floats like 8.90000000000e+17
#     Have left it as text.
#
# Indices are added on: author, region, language, publish_time, and account_type.
# This typically takes a few minutes to run.
#
# NOTE: Resulting db file is about 1.1GB (it will be smaller if you remove indices).
# However, sqlitebrowser uses nearly 5GB of RAM just to open it. Apparently sqlitebrowser is
# not well designed to cope with large databases...
# 

re_date = re.compile(r"\s*(\d+)/(\d+)/(\d+)\s+(\d+):(\d+)\s*")

base_time = time.mktime( (1970,1,2, 0,0,0, 0,0,0)) - 24*3600

# convert m/d/yyyy hh:mm to yyyy/mm/dd hh:mm and optionally to  time-since-1970-UTC
def convert_date( dstrng, tz= 0, only_reformat=False):
    m = re_date.match( dstrng )
    if m is None:
        raise ValueError("bad time string %s" %dstrng)
    mm,dd,yy,thh,tmm = [ int(x,10) for x in m.groups()]
    newstring = "%d/%02d/%02d %02d:%02d" %( yy,mm,dd,thh,tmm)
    if only_reformat:
        return newstring
		
    toff = time.mktime( (yy,mm,dd, thh, tmm, 0, 0, 0, 0) ) -base_time + 3600*tz
    return newstring,int(round(toff))
#
# read the CSV file, make sqlite database
#
def copy_to_db( infilenames, outfilename):
    try:
        os.unlink(outfilename)
    except OSError:
        pass

    conn = sqlite3.connect(outfilename)
    
    c = conn.cursor()
    c.execute( "pragma encoding='UTF-8';")
    # Create table
    c.execute('''CREATE TABLE tweets (
        external_author_id	text,
        author  text,
        content text,
        region  text,
        language text,
        publish_date text,
        publish_time integer,
        harvested_date text,
        following integer,
        followers integer,
        updates integer,
        post_type text,
        account_type text,
        retweet integer,
        account_category text,
        new_june_2018 integer)''')
    c.execute("CREATE INDEX tweet_author ON tweets( author )")
    c.execute("CREATE INDEX tweet_region ON tweets( region )")
    c.execute("CREATE INDEX tweet_language ON tweets( language )")
    c.execute("CREATE INDEX tweet_time ON tweets( publish_time )")
    c.execute("CREATE INDEX tweet_account_type ON tweets( account_type )")


    fields = ("external_author_id author content region language publish_date publish_time "
        "harvested_date following followers updates post_type account_type retweet "
        "account_category new_june_2018").split()

    cmd = "INSERT INTO tweets VALUES (" + ("?,"*len(fields))[:-1] + ")"

    n = 0
    for fn in infilenames:
        with open(fn) as csvfile:
            reader = csv.DictReader( csvfile)
            for rec in reader:
                rec['publish_date'],rec['publish_time'] = convert_date( rec['publish_date'])
                rec['harvested_date'] = convert_date( rec['harvested_date'],only_reformat=True)
                rec['content'] = codecs.decode( rec['content'],'utf_8')
                c.execute( cmd, [ rec[x] for x in fields] )
                n += 1
    conn.commit()
    print "%d records copied to %s" % (n, outfilename )

infnames = [ "IRAhandle_tweets_%d.csv" % k for k in range(1,10)] 

copy_to_db(infnames,"IRAhandle_tweets.db")

 
