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
       notFound=[]
       positiveWordsNum=0
       negativeWordsNum=0
       scoreOfTweet =0
       for word in words:
        if word in scores.keys():
         scoreOfTweet = scoreOfTweet + int(scores[word])
         if scores[word]>0:
          positiveWordsNum = positiveWordsNum +1
         elif scores[word]<0:
          negativeWordsNum = negativeWordsNum+1
        else:
         notFound.append(word)
       for uk in notFound:
        newScore = positiveWordsNum-negativeWordsNum+scoreOfTweet;
        print uk+" "+str(newScore)
         
if __name__ == '__main__':
    main()
