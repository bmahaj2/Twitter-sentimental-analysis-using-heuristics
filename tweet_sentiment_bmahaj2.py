import sys
import json
#import operator####################################################c

def main():
    sent_file = open(sys.argv[1],"r")
    tweet_file = open(sys.argv[2])
    #TODO: Implement
   # sentiment_f=open(sent_file,'r')
    scores={}
    contents = sent_file.readlines()
    #print(contents)
   # for line in contents:
    #    print(line)
     #   break
     
    for line in contents:
        term,score=line.split("\t")
        scores[term]=float(score)
    #print(scores)
    #print()
    tweet_text=[]
    
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
        x=str(Tweet_obj['text'].strip().replace("\n",""))
        #for i in range(len(x)):
        tweet_text.append(x.strip().lower())
        #for i in range(len(x)):
            
        
#####################################################################################
    
    d=dict()#############################################c
    for i in range(len(tweet_text)):###############################c
        sum=0########################################c
        for word in scores:
            if word in tweet_text[i] and len(word.strip().split(" "))>1:
                sum+=scores[word]
            
        y=tweet_text[i].split(" ")#############################c
        for z in range(len(y)):####################c
            if y[z] in scores:#########################c
                sum+=scores[y[z]]###################c
            else:#####################c
                sum+=0###################c
        
        d[tweet_text[i]]=sum###################c
    
  ############################################################################     
    #print(d)
    #sorted_d= sorted(d.items(), key=operator.itemgetter(1,0), reverse=True)#############################c
    #for i in range(10):##################################################c
        #print(sorted_d[i][1],":",sorted_d[i][0])###########################c
    
    
    #for i in range(len(sorted_d)-10,len(sorted_d)):#######################################c
       # print(sorted_d[i][1],":",sorted_d[i][0])########################################c
        
    d3=[]
    

        
    d3=sorted(d, key=d.__getitem__, reverse=True)
    #print(d3)
    for i in range(10):
        print(str(d[d3[i]])+": "+d3[i])
        
        
    for g in range(len(d3)-1,len(d3)-11,-1):
        print(str(d[d3[g]])+": "+d3[g])
    

        
    
   # sorted_d2=sorted(d.items(), key=operator.itemgetter(1,0))
  # for i in range(10):
   #    print(sorted_d2[i][1],":",sorted_d2[i][0])
    #print(sorted_d2)
    #for item in sorted_d:
     #   print(type(item))
                
            
        
        
   # print(tweet_text[0][1])
    #print(tweet_text[0][2])
    
    #print("seperated_words")        

if __name__ == '__main__':
    main()
