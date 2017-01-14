import sys
import json
#import operator ######################################c

def main():
    sent_file=open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #with open(tweet_file) as tweets:
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

    
    lineTweet=[]
    place_list=[]
    text_list=[]
    for line in tweet_file:
        #print(line)
        #break
        Tweet_obj=json.loads(line) # this will load your data into a workable json object
        #print(Tweet_obj['place'])

        if Tweet_obj["lang"]=="en":
            x=str(Tweet_obj['place'])
            y=str(Tweet_obj['text'].strip().replace("\n",""))
            #z=x+"<>;'"+y
            #print(type(x))
            #for i in range(len(x)):
            place_list.append(x)
            text_list.append(y)
    #print(place_list[26])        
    #print(text_list[26])
    #print(len(place_list))
    #print(len(text_list))
    state_dic={"AL":"Alabama",
"AK":"Alaska",
"AZ":"Arizona",
"AR":"Arkansas",
"AS":"American Samoa",
"CA":"California",
"CO":"Colorado",
"CT":"Connecticut",
"DE":"Delaware",
"DC":"District of Columbia",
"FL":"Florida",
"GA":"Georgia",
"GU":"Guam",
"HI":"Hawaii",
"ID":"Idaho",
"IL":"Illinois",
"IN":"Indiana",
"IA":"Iowa",
"KS":"Kansas",
"KY":"Kentucky",
"LA":"Louisiana",
"ME":"Maine",
"MP":"Northern Mariana Islands",
"PR":"Puerto Rico",
"MT":"Montana",
"NE":"Nebraska",
"NV":"Nevada",
"NH":"New Hampshire",
"NJ":"New Jersey",
"NM":"New Mexico",
"NY":"New York",
"NC":"North Carolina",
"ND":"North Dakota",
"OH":"Ohio",
"OK":"Oklahoma",
"OR":"Oregon",
"MD":"Maryland",
"MA":"Massachusetts",
"MI":"Michigan",
"MN":"Minnesota",
"MS":"Mississippi",
"MO":"Missouri",
"PA":"Pennsylvania",
"RI":"Rhode Island",
"SC":"South Carolina",
"SD":"South Dakota",
"TN":"Tennessee",
"TX":"Texas",
"UT":"Utah",
"VT":"Vermont",
"VA":"Virginia",
"VI":"Virgin Islands",
"WA":"Washington",
"WV":"West Virginia",
"WI":"Wisconsin",
"WY":"Wyoming"}
    
    #print(state_dic)
    text_index_list=[]
    list2=[]        
    for item in place_list:
        if item!="None":
            list2.append(item)
            text_index_list.append(place_list.index(item))
    #print(text_index_list)
    #print(len(text_index_list))
    #print(len(place_list))
    #for ele in list2:
     #   print(ele)
    text_index_list2=[]
    selected_text=[]
    for i in text_index_list:
        selected_text.append(text_list[i])
        
    #print(selected_text)
        
        
    city_list=[]
    for ele in list2:        
        if ele.split("'country_code': '")[1].split("'")[0]=="US":
            #if ele.split("'place_type': '")[1].split("'")[0]!="poi":
            if ele.split("'place_type': '")[1].split("'")[0]=="admin" or ele.split("'place_type': '")[1].split("'")[0]=="city":
                text_index_list2.append(list2.index(ele))
                #print(ele)
                #print("place type =admin")
                if ele.split("'place_type': '")[1].split("'")[0]=="admin":
                    #print(ele.split("'full_name': '")[1].split(",")[0])
                    city_list.append(ele.split("'full_name': '")[1].split(",")[0])
                    #'full_name': 'Staten Island, NY',
                else:
                   
                    #print(ele.split("'full_name': '")[1].split("'",2)[0].split(",")[1].strip())
                    city_list.append(ele.split("'full_name': '")[1].split("'",2)[0].split(",")[1].strip())
    #print(city_list)
    #print(len(list2))
    #print(len(place_list))
    #rev_dic = { v:k for k,v in state_dic.iteritems()}
    #print(rev_dic)
    #print(type(rev_dic))
   # print(text_index_list2)
    
    selected_text2=[]
    for i in text_index_list2:
        selected_text2.append(selected_text[i])
        
    #for i in range(len(selected_text2)):    
     #   print(selected_text2[i])
    
    inv_dic = dict((v,k) for k,v in state_dic.items())
   # print(inv_dic)
    
    for i in range(len(city_list)):
        if city_list[i] in inv_dic:
            city_list[i]=inv_dic[city_list[i]]
            
    #print(city_list)
    count_dic={}
    map_dic=dict()
    for i in range(len(city_list)):
        if city_list[i] in count_dic:
            count_dic[city_list[i]]+=1
        else:
            count_dic[city_list[i]]=1
            
      #      count_dic[row['user_name']]+=1
       # else:
        #    count_dic[row['user_name']]=1
        
        #index1=city_list.index(city_list[i])
        if city_list[i] in map_dic:
            map_dic[city_list[i]]=map_dic[city_list[i]]+" "+selected_text2[i]
        else:
            map_dic[city_list[i]]=selected_text2[i]
            
    #print(map_dic)
    #print(count_dic)
    
    sttw_dic={}
    for key in map_dic:
        if key in count_dic:
            total_tw=count_dic[key]
        sum=0
        for word in scores:
            if word in map_dic[key] and len(word.strip().split(" "))>1:
                sum+=scores[word]
        
        tweet_words= map_dic[key].split(" ")
        for i in range(len(tweet_words)):
            if tweet_words[i] in scores:
                sum+=scores[tweet_words[i]]
            else:
                sum=sum+0
        average=(sum/total_tw)
        sttw_dic[key]=average
        
    #print(sttw_dic)
    
    d3=[]
    d3=sorted(sttw_dic, key=sttw_dic.__getitem__, reverse=True)
    #print(d3)
    #print(type(d3))
    for item in d3:
        print(str(sttw_dic[item])+" : "+item)
    


if __name__ == '__main__':
    main()
