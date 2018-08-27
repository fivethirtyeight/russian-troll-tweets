# 3 million Russian troll tweets

This data was used in the FiveThirtyEight story [Why We’re Sharing 3 Million Russian Troll Tweets](https://fivethirtyeight.com/features/why-were-sharing-3-million-russian-troll-tweets/).

This directory contains data on nearly 3 million tweets sent from Twitter handles connected to the Internet Research Agency, a Russian "troll factory" and a defendant in [an indictment](https://www.justice.gov/file/1035477/download) filed by the Justice Department in February 2018, as part of special counsel Robert Mueller's Russia investigation. The tweets in this database were sent between February 2012 and May 2018, with the vast majority posted from 2015 through 2017.

FiveThirtyEight obtained the data from Clemson University researchers [Darren Linvill](https://www.clemson.edu/cbshs/faculty-staff/profiles/darrenl), an associate professor of communication, and [Patrick Warren](http://pwarren.people.clemson.edu/), an associate professor of economics, on July 25, 2018. They gathered the data using custom searches on a tool called Social Studio, owned by Salesforce and contracted for use by Clemson's [Social Media Listening Center](https://www.clemson.edu/cbshs/centers-institutes/smlc/).

The basis for the Twitter handles included in this data are the [November 2017](https://democrats-intelligence.house.gov/uploadedfiles/exhibit_b.pdf) and [June 2018](https://democrats-intelligence.house.gov/uploadedfiles/ira_handles_june_2018.pdf) lists of Internet Research Agency-connected handles that Twitter [provided](https://democrats-intelligence.house.gov/news/documentsingle.aspx?DocumentID=396) to Congress. This data set contains every tweet sent from each of the 2,752 handles on the November 2017 list since May 10, 2015. For the 946 handles newly added on the June 2018 list, this data contains every tweet since June 19, 2015. (For certain handles, the data extends even earlier than these ranges. Some of the listed handles did not tweet during these ranges.) The researchers believe that this includes the overwhelming majority of these handles’ activity. The researchers also removed 19 handles that remained on the June 2018 list but that they deemed very unlikely to be IRA trolls.

In total, the nine CSV files include 2,973,371 tweets from 2,848 Twitter handles. Also, as always, caveat emptor -- in this case, tweet-reader beware: In addition to their own content, some of the tweets contain active links, which may lead to adult content or worse.

The Clemson researchers used this data in a working paper, [Troll Factories: The Internet Research Agency and State-Sponsored Agenda Building](http://pwarren.people.clemson.edu/Linvill_Warren_TrollFactory.pdf), which is currently under review at an academic journal. The authors’ analysis in this paper was done on the data file provided here, limiting the date window to June 19, 2015, to Dec. 31, 2017.

The files have the following columns:

Header | Definition
---|---------
`external_author_id` | An author account ID from Twitter 
`author` | The handle sending the tweet
`content` | The text of the tweet
`region` | A region classification, as [determined by Social Studio](https://help.salesforce.com/articleView?id=000199367&type=1)
`language` | The language of the tweet
`publish_date` | The date and time the tweet was sent
`harvested_date` | The date and time the tweet was collected by Social Studio
`following` | The number of accounts the handle was following at the time of the tweet
`followers` | The number of followers the handle had at the time of the tweet
`updates` | The number of “update actions” on the account that authored the tweet, including tweets, retweets and likes
`post_type` | Indicates if the tweet was a retweet or a quote-tweet
`account_type` | Specific account theme, as coded by Linvill and Warren
`retweet` | A binary indicator of whether or not the tweet is a retweet
`account_category` | General account theme, as coded by Linvill and Warren
`new_june_2018` | A binary indicator of whether the handle was newly listed in June 2018
`alt_external_id` | Reconstruction of author account ID from Twitter, derived from `article_url` variable and the first list provided to Congress
`tweet_id` | Unique id assigned by twitter to each status update, derived from `article_url`
`article_url` | Link to original tweet. Now redirects to "Account Suspended" page
`tco1_step1` | First redirect for the first http(s)://t.co/ link in a tweet, if it exists
`tco2_step1` | First redirect for the second http(s)://t.co/ link in a tweet, if it exists
`tco3_step1` | First redirect for the third http(s)://t.co/ link in a tweet, if it exists

If you use this data and find anything interesting, please let us know. Send your projects to oliver.roeder@fivethirtyeight.com or [@ollie](https://twitter.com/ollie).

The Clemson researchers wish to acknowledge the assistance of the Clemson University Social Media Listening Center and Brandon Boatwright of the University of Tennessee, Knoxville.

#### Updates

- Split data into several small files. [[issue](https://github.com/fivethirtyeight/russian-troll-tweets/issues/2)]
- Fix double encoding. [[issue](https://github.com/fivethirtyeight/russian-troll-tweets/issues/5)]
- Data update from researchers at Clemson U. [[PR](https://github.com/fivethirtyeight/russian-troll-tweets/pull/28)]