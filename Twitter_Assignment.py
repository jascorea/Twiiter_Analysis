from datetime import datetime,timedelta

numbertoconsider = int(input("Enter a number :"))

array = []
with open("./cricket.txt", "r", encoding="utf-8") as f:
    for line in f:
        array.append(line)

userData = []
my_dict_tweets = {}
my_dict_hourly_Tweets ={}

class TwitterUser:
    def __init__(self, name, time, followers, tweets):
        self.name = name
        self.time = time
        self.followers = followers
        self.tweets = tweets

    def __repr__(self):
        return repr((self.name,self.time, self.followers, self.tweets))

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.followers

for i in range(0, len(array)):
    data = array[i].split(" ")
    xfollowers = len(data) - 2
    xtweets = len(data) - 1
    excepitonFound = False

    try:
        timestamp = data[1]
        userObj = TwitterUser(data[0],timestamp[1:], int(data[xfollowers]), int(data[xtweets].replace("\n", "")))
        userData.append(userObj)
    except Exception as e:
        #print(e)
        excepitonFound = True

    if(not excepitonFound):
        try:
            x = my_dict_tweets[data[0]]
            count = x + 1
            my_dict_tweets = {**my_dict_tweets, **{data[0]: count}}
        except KeyError as e:
            my_dict_tweets = {**my_dict_tweets, **{data[0]: 1}}

noduplicates = list(set(userData))

for lx in range(0,len(userData)):
    twitteruser = userData[lx]

    if(not excepitonFound):
        try:

            try:
                timestamp = datetime.strptime(twitteruser.time, "%d/%b/%Y:%H:%M:%S")
            except Exception as e:
                ext = True
                #print('EEEEEEEEEEEEEEE')
                #print(e)

            xlist = my_dict_hourly_Tweets[timestamp.hour]
            xlist.append(twitteruser)
            my_dict_hourly_Tweets = {**my_dict_hourly_Tweets, **{timestamp.hour: xlist}}
        except KeyError as e:
            list = []
            my_dict_hourly_Tweets = {**my_dict_hourly_Tweets, **{timestamp.hour: list}}

sortedFollowerList = sorted(noduplicates, key=lambda twitter: twitter.followers, reverse=True)
sortedTwitterList = sorted(noduplicates, key=lambda twitter: twitter.tweets, reverse=True)
sortedTweetsTimelineList = sorted(my_dict_tweets.items(), key=lambda t: t[1],reverse=True)

mostfollowers = open("mostfollowers.txt", "w", encoding="utf-8")

for x in range(0, numbertoconsider):
    mostfollowers.write(sortedFollowerList[x].name + " " + str(sortedFollowerList[x].followers) + "\n")
    mostfollowers.flush()

most_re_tweets = open("mostretweets.txt", "w", encoding="utf-8")

for x in range(0, numbertoconsider):
    most_re_tweets.write(sortedTwitterList[x].name + " " + str(sortedTwitterList[x].tweets) + "\n")
    most_re_tweets.flush()

most_tweets_over_Timeline = open("Most_Tweets_Over_timeline.txt", "w", encoding="utf-8")

count = 0
for (twitteruser, tweets) in sortedTweetsTimelineList:
    most_tweets_over_Timeline.write(str(twitteruser) +" "+str(tweets)+"\n")
    most_tweets_over_Timeline.flush()
    count = count +1
    if(count == numbertoconsider):
        break

#print('###############################################################')

most_tweets_every_hour = open("most_tweets_every_hour.txt", "w", encoding="utf-8")

hour =1
for key,value in my_dict_hourly_Tweets.items():

    my_dict_hourly_tweets_loc = {}

    most_tweets_every_hour.write('hour' + " " + str(hour) + "\n")

    for xj in range(0,len(value)):
        twitteruser = value[xj]

        try:
            x = my_dict_hourly_tweets_loc[twitteruser.name]
            hourly_count = x + 1
            my_dict_hourly_tweets_loc = {**my_dict_hourly_tweets_loc, **{twitteruser.name: hourly_count}}
        except KeyError as e:
            my_dict_hourly_tweets_loc = {**my_dict_hourly_tweets_loc, **{twitteruser.name: 1}}

    sortedTweetsTimelineList_hourly = sorted(my_dict_hourly_tweets_loc.items(), key=lambda t: t[1], reverse=True)

    written_count =0
    for (twitteruser, tweets) in sortedTweetsTimelineList_hourly:
        most_tweets_every_hour.write(str(twitteruser) + " " + str(tweets) + "\n")
        most_tweets_over_Timeline.flush()
        written_count = written_count + 1
        if (written_count == numbertoconsider):
            break

    hour = hour +1
