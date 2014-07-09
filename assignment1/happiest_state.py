import sys
import json
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    for line in sent_file:
     term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
     scores[term] = int(score)  # Convert the score to an integer.
    count =0;
    scoreOfTweet = 0
    locationScore={}
    for li in tweet_file:
     data = json.loads(li);
     if "user" in data.keys():
      locale =  data["user"]["location"].encode('utf-8').replace(" ","")
      if("," in locale):
        location = locale.split(",")[1]
      else:
       location = locale
      if location in states.keys(): 
       if "text" in data.keys():
         words = data["text"].encode('utf-8').split(" ");
         for word in words:
          if word in scores.keys():
           scoreOfTweet = scoreOfTweet + int(scores[word])
       if location in locationScore.keys():
        locationScore[location] = locationScore[location]+ scoreOfTweet
       else:
        locationScore[location]= scoreOfTweet
       scoreOfTweet = 0
    if len(locationScore.keys())!=0:
     largest = locationScore.keys()[0]
     for loc in locationScore.keys():
       if int(locationScore[largest])<int(locationScore[loc]):
        largest = loc
     print largest   
if __name__ == '__main__':
    main()
