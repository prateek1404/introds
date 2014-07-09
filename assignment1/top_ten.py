import sys
import json


def main():
    tweet_file = open(sys.argv[1])
    hashCount={}
    for li in tweet_file:
     data = json.loads(li);
     if "entities" in data.keys():
       entities = data['entities']
       if "hashtags" in entities.keys():
        hashtags = entities["hashtags"]
        for has in hashtags:
         if has["text"] in hashCount.keys():
          hashCount[has["text"]] = hashCount[has["text"]]+1
         else:
          hashCount[has["text"]]=1
    hashArray=[]     
    for h in hashCount.keys():
     if len(hashArray) ==0:
      hashArray.append({'name':h,'count':int(hashCount[h])})
     else:
      k=0
      while hashCount[h]<hashArray[k]['count'] and k<len(hashArray): 
       k = k+1
      hashArray.insert(k,{'name':h,'count':int(hashCount[h])})
    for x in range(0,10):
      print hashArray[x]['name'].encode('utf-8')+" "+str(hashArray[x]['count'])
if __name__ == '__main__':
    main()
