
#This code creates the dataset from Corpus.csv which is downloadable from the
#internet well known dataset which is labeled manually by hand. But for the text
#of tweets you need to fetch them with their IDs.
import tweepy

# Twitter Developer keys here
# It is CENSORED
consumer_key = 'jJsJ5nbvgmiqTNj9kEFlQH97x'
consumer_key_secret = '5FtNQi4yDuwwSS8exRIXlN9PFR88jHzhdS2dcFI1deK1CRg4lO'
access_token = '2966544399-4FwEe1ZtBwxVBmcoGn2Trln8wiPTbTnwcAkAAWc'
access_token_secret = 'LNiBng3H7LodLAFaTVkKxi3jA1LcYjL1XF4qT74qBv3gS'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# This method creates the training set
def createTrainingSet(corpusFile, targetResultFile):
    import csv
    import time

    counter = 0
    corpus = []

    with open(corpusFile, 'r') as csvfile:
        lineReader = csv.reader(csvfile, delimiter=',', quotechar="\"")
        for row in lineReader:
            corpus.append({"annotator_id": row[2], "label": row[1], "tweet_id": row[0]})

    sleepTime = 2
    trainingDataSet = []

    for tweet in corpus:
        try:
            tweetFetched = api.get_status(tweet["tweet_id"])
            print("Tweet fetched" + tweetFetched.text)
            tweet["text"] = tweetFetched.text
            trainingDataSet.append(tweet)
            time.sleep(sleepTime)

        except:
            print("Inside the exception - no:2")
            continue

    with open(targetResultFile, 'w') as csvfile:
        linewriter = csv.writer(csvfile, delimiter=',', quotechar="\"")
        for tweet in trainingDataSet:
            try:
                linewriter.writerow([tweet["tweet_id"], tweet["text"], tweet["label"], tweet["annotator_id"]])
            except Exception as e:
                print(e)
    return trainingDataSet

# Code starts here
# This is corpus dataset
corpusFile = "/home/bartek/Documents/portfolio/twitter_sentiment/Twitter sentiment for 15 European languages/Polish_Twitter_sentiment.csv"
# This is my target file
targetResultFile = "/home/bartek/Documents/portfolio/twitter_sentiment/targetResultFile.csv"
# Call the method
resultFile = createTrainingSet(corpusFile, targetResultFile)
