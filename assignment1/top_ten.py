import sys
import json


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    for line in sent_file:
     term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
     scores[term] = int(score)  # Convert the score to an integer.
    count =0;
    scoreOfTweet = 0
    for li in tweet_file:
     data = json.loads(li);
     if "text" in data.keys():
       words = data["text"].encode('utf-8').split(" ");
       for word in words:
        if word in scores.keys():
         scoreOfTweet = scoreOfTweet + int(scores[word])
     print scoreOfTweet
     scoreOfTweet = 0
         
if __name__ == '__main__':
    main()
