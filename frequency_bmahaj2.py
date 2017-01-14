import sys
import json
#import operator ######################################c

def main():
    stopwords_file=open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #with open(tweet_file) as tweets:
    lineTweet=[]
    separated_words=[]
    for line in tweet_file:
        #print(line)
        #break
        Tweet_obj=json.loads(line) # this will load your data into a workable json object
        #print(type(Tweet_obj))
        #print(Tweet_obj)
        #break
        #for tweet in Tweet_obj:
            #lineTweet.append(line.strip())
            #print(tweet['text'].encode('utf-8'))
       # lineTweet.append((Tweet_obj['text'].strip().encode('utf-8')))
        if Tweet_obj["lang"]=="en":
            x=str(Tweet_obj['text'].strip().replace("\n","")).split(" ")
            for i in range(len(x)):
                separated_words.append(x[i].strip().lower())
    #print(separated_words)        
    #print(separated_words)
    #print(separated_words[0])
   # print("length of separated words")
    #print(len(separated_words))
    #print(separated_words)
    stopwords=[]
    for line2 in stopwords_file:
        stopwords.append(line2.strip())
   # print("stopwords")    
    #print(stopwords)
    d=dict()
    item_count=0
    ###################################################################################
    for item in stopwords:
        while item in separated_words:
            #print(item)
            separated_words.remove(item)
            #print("removed item")
           # print(item)
   # print("separted words after removing stopwords")  
    #print(len(separated_words))      
    #print(separated_words)
    ##########################################################################################
   # print("separated word rnage")
    #for i in range(len(separated_words)):
        #print(separated_words[i])
     #   for j in range(len(stopwords)):
      #      if(separated_words[i]==stopwords[j]):
       #         del separated_words[i]
    
    #print("words final")
    #print(separated_words)
    
        
    #haha=[]
    #for item in stopwords:
     #   list(filter((item).__ne__,separated_words))
    
    #print("separted words after removing stopwords")  
    #print(separated_words)    
    
    
    for key in separated_words:
        if key in d:
            d[key]+=1
        else:
            d[key]=1
    if '' in d:        
        del d['']
            #print(type(d[key]))
    #print("lenght of separetdwords")
    #print(type(len(separated_words)))
            
    #print(d)
    #sorted_d = sorted(d.items(), key=operator.itemgetter(1,0), reverse=True)
    #print("sorted dictionary")
    #print(sorted_d)
    #print(type(sorted_d))
    #print(sorted_d[0])
    
    dic_frequency=dict()
    for key in d:
        frequency=(d[key]/len(separated_words))
        dic_frequency[key]=frequency
    #print("dictionary of frequencies")
   # print(dic_frequency)
    
    #sorted_dic_frequency= sorted(dic_frequency.items(), key=operator.itemgetter(1,0), reverse=True)###########C
   # print("sorted dictionary of frequencies")
    #print(sorted_dic_frequency)
   # print(sorted_dic_frequency[0][0])
    #print(type(sorted_dic_frequency[0][0]))
    #print(sorted_dic_frequency[0][1])
    
    
    #print("items of soeted did list")
    #print(type(sorted_dic_frequency))
   # for i in range(len(sorted_dic_frequency)):#################################################c
        #print(sorted_dic_frequency[i][0]," ",sorted_dic_frequency[i][1])#########################c
        
    d3=[]
    d3=sorted(dic_frequency, key=dic_frequency.__getitem__, reverse=True)
    for item in d3:
        print(item+" "+str(dic_frequency[item]))
        #print(sorted_dic_frequency[i][1])
        #print(type(sorted_dic_frequency[i][0]))
        #print(type(sorted_dic_frequency[i][1]))
        #break
    #for p in sorted_dic_frequency:
        #print(str(p))
       # print(str(p).split(",")[0])
        #print(parts[0])
        #p.split(",")
        #print(p)
    
    #inputfile=sys.argv[3]
    #file=open(inputfile, 'w')
    #for p in sorted_dic_frequency:
     #   file.write(p)
        
            
            
     #   item_count+=1
    #print(item + str(item_count))
       # print(item)
    
        
    
        
        
    #print(lineTweet)
    #print(len(lineTweet))
    #first_item=lineTweet[0]
   # print(first_item)
            #csv_object.writerow(lineTweet)
   # contents=tweet_file.readlines()
    #for line in contents:
     #   print(line)
    #print(contents)
    #print(contents)
    ##for line in contents:
      ##  Tweet_obj= json.loads(line.strip().decode("utf-8"))
        ##for tweet in Tweet_obj: 
          ##  print((tweet['text'].strip().encode('utf-8')))
    #    print(line)
    ##print(type(tweet_file.readlines()))
   # Tweet_obj= json.loads(tweet_file.readlines().decode("utf-8"))////////////////////////////
        #json.stringify(Tweet_obj)
    #for tweet in Tweet_obj: ///////////////////
       # print((tweet['text'].strip().encode('utf-8')))
        #print(tweet)
        #lineTweet.append(line.strip())
        #print(tweet['text'].encode('utf-8'))
        #lineTweet.append((tweet['text'].strip().encode('utf-8')))
     
   # tweet=contents.split(',"text":"')[1].split('","source":"')[0]
    #print(tweet)
    #Tweet_obj= json.loads(contents.strip())
        #json.stringify(Tweet_obj)
    #for tweet in Tweet_obj:
        #lineTweet=[]
        #lineTweet.append(line.strip())
        #print(tweet['text'].encode('utf-8'))
     #   print(tweet['text'].strip())
        #csv_object.writerow(lineTweet)
    #TODO: Implement

if __name__ == '__main__':
    main()
