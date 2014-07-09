import sys
import json


def main():
    tweet_file = open(sys.argv[1])
    freq = {}
    totalWords = 0.0;
    for li in tweet_file:
     data = json.loads(li);
     if "text" in data.keys():
       line = ' '.join(data["text"].encode('utf-8').split())
       words = line.split(" ")
       for word in words:
        if word in freq.keys():
         freq[word]= freq[word]+1.0
        else:
         freq[word]=1.0
        totalWords= totalWords+1.0
    for k in freq.keys():
     print k+" "+str(freq[k]/totalWords)  

  
if __name__ == '__main__':
    main()
