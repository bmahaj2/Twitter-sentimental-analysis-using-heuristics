import sys
import csv
#import operator###############################################################c
from _operator import itemgetter

def main():
    sent_file = open(sys.argv[1],"r")
    csv_file = open(sys.argv[2])
    file_reader = csv.reader(csv_file)
    #TODO: Implement
    scores={}
    contents = sent_file.readlines()
    #print(contents)
   # for line in contents:
    #    print(line)
     #   break
     
    for line in contents:
        term,score=line.split("\t")
        scores[term]=float(score)
    #print(type(scores['vexation']))
        
    #print(scores)
    #print(scores)
    #print()
    
    d={}
    count_dic={}
   # with open('names.csv') as csvfile:
    reader = csv.DictReader(csv_file)
    #print(type(reader))
    for row in reader:
        if row['user_name'] in count_dic:
            count_dic[row['user_name']]+=1
        else:
            count_dic[row['user_name']]=1
        if row['user_name'] in d:
           # d[row['user_name']]+=row['tweet']
            d[row['user_name']]=d[row['user_name']]+" "+row['tweet']
        else:
            d[row['user_name']]=row['tweet']
            
    #print(count_dic)
        #print(type(row['user_name']))
        #print(row['user_name'], row['tweet'])
    #print(type(d['BryanCranston']))
    #print(type(d))
   # for row in reader:
    #    print("ehhh")
    
    d2={}
    for key in d:
        if key in count_dic:
            total_tw=count_dic[key]
     #   print(total_tw)
            
        #reader2 = csv.DictReader(csv_file)
        #Tweet_count=0
        #for row in reader2:
         #   if row['user_name']==key:
          #      Tweet_count+=1
            #else:
             #   print("haha")
        #print(Tweet_count)   
            
        sum=0
        tweet_words=d[key].split(" ")
        for i in range(len(tweet_words)):
            if tweet_words[i] in scores:
                sum+=scores[tweet_words[i]]
                #print(tweet_words[i])
                #sum+=scores["'"+tweet_words+"'"]
            #print(type(scores[tweet_words]))
            else:
                sum=sum+0
        average=(sum/total_tw)
        
        d2[key]=average   
        
    #print(d2)  
    
    #sorted_d2= sorted(d2.items(), key=operator.itemgetter(1,0), reverse=True)#######################c
    #print(type(sorted_d2))
    #for i in range(len(sorted_d2)):##############################c
     #   print(sorted_d2[i][1],":",sorted_d2[i][0])   ##################################c
     
    #sortii=sorted(d2.iteritems(), key=itemgetter(1), reverse=True)
    #print(type(sortii))
    d3=[]
    d3=sorted(d2, key=d2.__getitem__, reverse=True)
    #print(d3)
    #print(type(d3))
    for item in d3:
        print(str(d2[item])+" : "+item)
        #print(item)
    #print(d2)
        
        
        
        
        
        
        
        

if __name__ == '__main__':
    main()
