#!/usr/bin/env python
# coding: utf-8

# In[1]:



#This function extracts today's match links
def hrefing(rawFixtures):
    #counter
    num = 0
    #list for storing the href wbelinks retrieved
    todayFixtures = []

    while num < len(rawFixtures):
        #assign variable name to a table data item inside rawFixture(rawFixtures contains many tables data) of html data
        subsub= rawFixtures[num]
        #select 'a' tags 
        atags = subsub.find_all('a')
        #select the href links
        hrefLinks = [l.get('href') for l in atags]
        #select href link bearing '/squads/'
        hrefLinks = [l for l in hrefLinks if '/squads/'in l]
        #complete href link into weblink
        hrefLinks = ["https://fbref.com"+l for l in hrefLinks]
        #append these weblinks to a list called todayFixtures 
        todayFixtures.append(hrefLinks)
        #add count
        num+=1
        
    return (todayFixtures)



#This function pairs elements in a list
def pairer(fixtureLinks):
    MatchPairs=[]
    #perform code for all items in fixtureLinks
    for item in fixtureLinks:
        #append list pair into matchpairs list if length of list item is already a pair
        if len(item) == 2:
            MatchPairs.append(item)
            
        #append list pair in match pair list if length of list item is bigger than a pair and a total even number 
        elif len(item) > 2 and len(item)%2 == 0:
            #As long as the number of list item is greater than 1;  move the first and second items of the list element into matchpairs list
            while len(item) > 1:
                #pick the first and second item on list item and assign it to the variable called  first element
                firstElement=item[0:2]
                #append first element to match pair then removes contents of first element from list item                
                MatchPairs.append(firstElement)
                item.pop(0)
                item.pop(0)
        # skips any scenario that doesn't fall into the previous two conditions 
        else:
            continue
    
    return MatchPairs



#This function pairs elements in a list
def h2hsingular(h2h_links):
    h2h_links1=[]
    #perform code for all items in h2h_Links
    for item in h2h_links:
        #append list pair into matchpairs list if length of list item is already a pair
        if len(item) == 1:
            h2h_links1.append(item)
            
        #append list pair in match pair list if length of list item is bigger than a pair and a total even number 
        elif len(item) < 1:
            x='pass'
            h2h_links1.append(x)
        else:            
            #As long as the number of list item is greater than 1;  move the first and second items of the list element into matchpairs list
            while len(item) >= 1:
                #pick the first and second item on list item and assign it to the variable called  first element
                firstElement=item[0]
                #append first element to match pair then removes contents of first element from list item                
                h2h_links1.append(firstElement)
                item.pop(0)

    
    return h2h_links1



def all_strings(link_list):
#list to be returned
    new_linklist=[]
    #counter
    num=0
    #check if elements in link_list are strings, if not convert to string
    for a in link_list:
        #if element is a list, append the list's element into new_linklist
        if type(a) == list:
            x=link_list[num][0]
            new_linklist.append(x)
        #if element is a string, append the string into new_linklist
        elif type(a)== str:
            new_linklist.append(a)
        #if element neither a string or a list append 'pass' to new_linklist
        else:
            new_linklist.append('pass')
        #count 
        num+=1
    
    return new_linklist




def hrefing_h2h(rawFixtures):
    #counter
    num = 0
    #href list
    h2h_List = []
    while num < len(rawFixtures):
        #assign variable name to a table data item inside rawFixtures (rawFixtures contains many tables data) of html data
        subsub= rawFixtures[num]
        #select 'a' tags 
        atags = subsub.find_all('a')
        #select the href link
        hrefLinks = [l.get('href') for l in atags]
        #select href link bearing '/stathead/'
        hrefLinks = [l for l in hrefLinks if '/stathead/'in l]
        hrefLinks = ["https://fbref.com"+l for l in hrefLinks]
        h2h_List.append(hrefLinks)
        num+=1
    return (h2h_List)






#this function takes in home & away team href links, for internet testing.  
def home_away1(a):
    #import libraries for time & datetime
  
    #retrieve homeTeam page html and assign it to the variable name called homeTeam
    homeTeam=requests.get(a) 
    #wait for 4 seconds
    homeDF = pd.read_html(homeTeam.text, match='Venue')[0]
    homeDF=homeDF[['Date','Comp', 'Venue', 'Result', 'GF', 'GA', 'Opponent']]
    #matchDay = str(date.today())
    #from homeDF, pick row which has the Date column data equal to today's date, assign that row to a new dataframe homeDF1
    homeDF1 = homeDF[homeDF['Date'] == matchDay]
    #reset the index column of homeDF1 to 0    
    homeDF1 = homeDF1.reset_index(drop=True)
    #retrieve the data under row = '0' and column = 'Comp'. then assign this value to a variable name called compName
    compName=homeDF1.loc[0,'Comp']    
    #In homeDF, drop all rows except where the 'Comp' column is equal to compName
    homeDF = homeDF[homeDF['Comp'] == compName]
    homeName = a.split('/')[-1].replace('-Stats','').replace('-',' ')
    homeDF1 = homeDF.dropna(subset = ['Result'])
    homeDF1 = homeDF1[homeDF1['Venue'] == 'Home']
    homeDF1 = homeDF1.tail(5)
    homeDF1 = homeDF1.reset_index(drop=True)
    homeDF1['GF'] = homeDF1['GF'].astype(int)
    homeDF1['GA'] = homeDF1['GA'].astype(int)
    homeDF1['Point'] = (homeDF1['GF'] != 0).astype('int')
    homeDF11 = homeDF1.tail(2)
    homeDF11 = homeDF11.reset_index(drop=True)
    homeDF11['Point'] = (homeDF11['GA'] != 0).astype('int')
    homeDF11 = homeDF1.tail(2)
    homeDF11 = homeDF11.reset_index(drop=True)
    homeDF11['Point'] = (homeDF11['GA'] != 0).astype('int')
    home_GF = sum(homeDF1['Point'])
    home_GA = sum(homeDF11['Point'])

    x= [homeDF, homeName, compName, home_GF, home_GA]
    return x
    
#this function    
def home_away2(b):
    #import libraries for time & datetime
      
    #retrieve homeTeam page html and assign it to the variable name called homeTeam
    
    
    #retrieve awayTeam page html and assign it to the variable name called awayTeam
    awayTeam=requests.get(b) 
    
    #using pandas, read homeTeam html and retrieve the match fixtures table in it (match fixture table is the only table with 'Venue'column), and assign table to dataframe name called homeDF
    
    #in homeDF, drop all columns except the specified ones
    
    #using pandas, read awayTeam html and retrieve the match fixtures table in it (match fixture table is the only table with 'Venue'column), and assign table to dataframe name called awayDF
    awayDF = pd.read_html(awayTeam.text, match='Venue')[0]
    #in awayDF, drop all columns except the specified ones
    awayDF=awayDF[['Date','Comp', 'Venue', 'Result', 'GF', 'GA', 'Opponent']]
    
    #set variable matchDay as the string version of today's date
    #matchDay = str(date.today())
    #from homeDF, pick row which has the Date column data equal to today's date, assign that row to a new dataframe homeDF1
    awayDF1 = awayDF[awayDF['Date'] == matchDay]
    #reset the index column of homeDF1 to 0    
    awayDF1 = awayDF1.reset_index(drop=True)
    #retrieve the data under row = '0' and column = 'Comp'. then assign this value to a variable name called compName
    compName=awayDF1.loc[0,'Comp']    
    #In homeDF, drop all rows except where the 'Comp' column is equal to compName
    
    #In awayDF, drop all rows except where the 'Comp' column is equal to compName
    awayDF = awayDF[awayDF['Comp'] == compName]
    
    #from home team href link, retrieve club name and assign to a variable called homeName
    
    #from away team href link, retrieve club name and assign to a variable called awayName
    awayName = b.split('/')[-1].replace('-Stats','').replace('-',' ')
    #arrange homeDF, awayDF, awayName, compName in described order and put in a list called x  
    awayDF2 = awayDF.dropna(subset = ['Result'])
    awayDF2 = awayDF2[awayDF2['Venue'] == 'Away']
    awayDF2 = awayDF2.tail(5)
    awayDF2 = awayDF2.reset_index(drop=True)
    awayDF2['GF'] = awayDF2['GF'].astype(int)
    awayDF2['GA'] = awayDF2['GA'].astype(int)
    awayDF2['Point'] = (awayDF2['GA'] != 0).astype('int')
    awayDF12 = awayDF2.tail(2)
    awayDF12 = awayDF12.reset_index(drop=True)
    awayDF12['Point'] = (awayDF12['GF'] != 0).astype('int')
    away_GA = sum(awayDF2['Point'])
    away_GF = sum(awayDF12['Point'])
    x= [awayDF, awayName, away_GA, away_GF]
    return x


#retrieve homeGenResult predictor value from df (homeDF) DataFrame
def genrlCleaner(df):
    #drop all rows that have None values
    df = df.dropna(subset = ['Result'])
    df = df.reset_index(drop=True)
    #retrieve number of rows remaining
    x = int(df.shape[0])
    #if number of rows is less than or equal to 5, 
    if x <= 5:
        pass
    #if no of rows is greater than 5
    else:
        #drop all rows except last five rows 
        df=df.head(5)
    #create a reference dictionary where W=1, D=0.5, L=0
    d = {'W': 1,'D': 0.5,'L': 0}
    #replace the W, D, and L's in the 'Result' column with numbers based on the reference dictionary d
    df['Result']=df['Result'].map(d)
    #find the sum of the numbers in 'Result' column and assign the variable name v
    v = float(df['Result'].sum())
    
    return v    

        
def homeCleaner(df):
    df = df.dropna(subset = ['Result'])
    df = df.reset_index(drop=True)
    df = df[df['Venue']== 'Home']
    x = int(df.shape[0])
    if x <= 5:
        pass
    else:
        df = df.head(5)
    d={'W': 1,'D': 0.5,'L': 0}
    df['Result']=df['Result'].map(d)
    v=float(df['Result'].sum())
    return v    
            
def awayCleaner(df):
    df=df.dropna(subset = ['Result'])
    df = df.reset_index(drop=True)
    df= df[df['Venue']== 'Away']
    x = int(df.shape[0])
    if x<= 5:
        pass
    else:
        n=x-5
        df=df.head(5)
    d={'W': 0,'D': 0.5,'L': 1}
    df['Result']=df['Result'].map(d)
    v=float(df['Result'].sum())
    return v    



def h2hFormer(z,homeName):
    #get html page
    h2hpg = requests.get(z)
    #get h2h table
    h2h_table = pd.read_html(h2hpg.text, match = 'Head-to-Head Matches Table')[0]
    #drop all columns except specified ones
    h2h_table = h2h_table[['Home', 'Date','Score','Away']]
    #convert  'score' column data into strings
    h2h_table['Score'] = [str(l) for l in h2h_table['Score']] 
    #drop all columns where 'score' is NaN
    h2h_table = h2h_table[h2h_table['Score']!= 'nan']          
    #drop all rows except first two
    h2h_table = h2h_table.head(2)
    #reset index
    h2h_table = h2h_table.reset_index(drop=True)
    try:
        h2h_table.loc[0, 'Home']
    except:
        x = [0, 'NaN']
    else:
        if h2h_table.loc[0,'Home'] == h2h_table.loc[h2h_table.shape[0] - 1,'Home']:
            result=[]
            num002 = 0
            for a in h2h_table['Score']:
                if '(' in a:
                    hs = int(h2h_table.loc[num002,'Score'][4])
                    As = int(h2h_table.loc[num002,'Score'][6])
                    gd = hs - As
                    result.append(gd)
                else:
                    hs = int(h2h_table.loc[num002,'Score'][0])
                    As = int(h2h_table.loc[num002,'Score'][2])
                    gd = hs - As
                    result.append(gd)   
                num002+=1
            num003 = 0
            for b in result:
                if b > 0:
                    result[num003] = 1
                elif b < 0:
                    result[num003] = 0
                else:
                    result[num003] = 0.5
                num003+=1
            hn = h2h_table.loc[0, 'Home']
            result = sum(result)
            
        else:
            result=[]
            if '(' in h2h_table.loc[0,'Score']:
                hs = int(h2h_table.loc[0, 'Score'][4])
                As = int(h2h_table.loc[0, 'Score'][6])
                gd = hs - As
                result.append(gd)
            else:
                hs = int(h2h_table.loc[0, 'Score'][0])
                As = int(h2h_table.loc[0, 'Score'][2])
                gd = hs - As
                result.append(gd)
            if '(' in h2h_table.loc[1,'Score']:
                hs = int(h2h_table.loc[1, 'Score'][6])
                As = int(h2h_table.loc[1, 'Score'][4])
                gd = hs - As
                result.append(gd)
            else: 
                hs = int(h2h_table.loc[1, 'Score'][2])
                As = int(h2h_table.loc[1, 'Score'][0])
                gd = hs - As
                result.append(gd)
            num004 = 0
            for c in result:
                if c > 0:
                    result[num004] = 1
                elif c < 0:
                    result[num004] = 0
                else:
                    result[num004] = 0.5
                num004+=1
            result = sum(result)
            hn = h2h_table.loc[0, 'Home']
           
        if hn in homeName:
            pass
        else:
            result = 2 - result

        h2hgoalist = []
        num005 = 0
        for a in h2h_table['Score']:
            if '(' in a:
                hs = int(h2h_table.loc[num005,'Score'][4])
                As = int(h2h_table.loc[num005,'Score'][6])
                goal = hs + As
                h2hgoalist.append(goal)
            else:
                hs = int(h2h_table.loc[num005,'Score'][0])
                As = int(h2h_table.loc[num005,'Score'][2])
                goal = hs + As
                h2hgoalist.append(goal)
            num005+=1
        num006 = 0
        for b in h2hgoalist:
            if b == 0 or b == 1:
                h2hgoalist[num006] = 0
            else:
                h2hgoalist[num006] = 1
            num006 += 1
        h2h_goals = sum(h2hgoalist)  


        
    x =  [result, hn, h2h_goals]
    return x   

















#when to give a league link it returns the list of table standings in form of each team's page link 
def tableListing(leagueLink):
    all_leagues = allcompetitions()
    if leagueLink in all_leagues:
        Data = requests.get(leagueLink)  
        soup = bs.BeautifulSoup(Data.text)
        tables= soup.select('table.stats_table')
        x=list(tables)
        tablelist=x[0]
        tablelist=tablelist.find_all('a')
        tablelist=[str(l) for l in tablelist]
        tablelist=[l for l in tablelist if '/squads/' in l]
        tablelist=["https://fbref.com"+l.split('"')[1] for l in tablelist]
    else:
        tablelist=[]
        tablelist.append('pass')
        
    return tablelist


#rank the two team on the table
def teamRanker(tablelist,teamLink1,teamLink2):
    if 'pass' not in tablelist:
        tableRank1= tablelist.index(teamLink1)+1
        tableRank2= tablelist.index(teamLink2)+1
        tableNum= len(tablelist)
    else:
        tableRank1= 'pass'
        tableRank2= 'pass'
        tableNum= 'pass'
    return(tableRank1,tableRank2,tableNum)
    

#generates league table links
def leagueLkGenerator(rawFixtures):
    dw=[]
    da=[]
    #search in the table data for 'th' tags and append to list called dw. do this for all items in rawFIxtures
    for a in rawFixtures:
        b=a.find_all('th')
        dw.append(b)
    #search the table 'th' data in dw for all 'a' tags, and  append to list called da
    for a in dw:
        for b in a:
            c=b.find('a')
            if c == None:
                continue
            else:
                da.append(c)
    #convert da list content into strings
    da = [str(l) for l in da]
    #convert da list content in complete links
    competitionList = ["https://fbref.com"+l.split('"')[1] for l in da]
    
    return (competitionList)

#this functio pulls out all league competition Links
def allcompetitions(allCompLink):
    
    compPg= requests.get(allCompLink)

    soup=bs.BeautifulSoup(compPg.text)

    atag=soup.find_all('a')

    atag = list(atag)
    atag = [str(l) for l in atag]
    #atag = [l for l in atag if '/history/' in l]
    #atag = [l.split('"')[1] for l in atag]
    #atag = ['https://fbref.com'+ l for l in atag]
    #atag = [l.replace('history/','').replace('-Seasons','-Stats') for l in atag]
    #ataga = atag[:116]
    #atagx = ataga[32:]
    return atag



# In[2]:


#importing libraries
import csv
import pandas as pd
import requests
from datetime import date
import bs4 as bs
import time


# In[3]:


matchDay= str(input('INPUT DATE (YYYY-MM-DD): '))
#Download site data as html
url = "https://fbref.com/en/matches/"+matchDay

Data = requests.get(url)

#Parses site html data  
soup = bs.BeautifulSoup(Data.text)


# In[4]:


#Select all tables named 'stats_table' and append to a list named 'rawFixtures'
rawFixtures = soup.select('table.stats_table')

#get the href links of each team in fixtures
fixtureLinks = hrefing(rawFixtures)
#pair team href links according to their exact match fixtures
fixtureLinks = pairer(fixtureLinks)


#retrieves league link for each match fixture in the today's matches page
competitionList= leagueLkGenerator(rawFixtures)

#retrieve all available h2h hrefLinks from each fixture
h2h_links = hrefing_h2h(rawFixtures)
#arrange each h2hlink as single elements
h2h_links = h2hsingular(h2h_links)
#convert all elements within the list into string object
h2h_links = all_strings(h2h_links)

num1 = 0
for fixture in fixtureLinks:
    fixture.append(h2h_links[num1])
    fixture.append(competitionList[num1])
    num1+=1


# In[5]:




columns = ['HOME', 'AWAY','COMP','GOAL_PERCENT','WIN_PERCENT','HOME_FORM','AWAY_FORM','HOME_GEN_FORM','H2HOME_NAME','H2H_FORM','HOME_GF','AWAY_GA', 'HOME_GA','AWAY_GF','H2H_GOALS']
with open('Match Analysis {x}.csv'.format(x=matchDay), 'w') as file:
    writer = csv.writer(file)
    writer.writerow(columns)


# In[9]:


#retrieve home and away DataFrames, home and away names, and competition name and append to corresponding list


#do this block of code for each element pair in fixtureLinks0
print(str(len(fixtureLinks))+' Potential Fixtures\n\n')

num000 = int(input('Input fixture number to start from: '))
num001 = num000 - 1
for fixture in fixtureLinks[num001:]:
    #retrieve home: DataFrame, Name and Competition name and assign to variables
    homeDF = (home_away1(fixture[0])[0])
    homeName = (home_away1(fixture[0])[1])   #MAIN
    compName = (home_away1(fixture[0])[2])   #MAIN
    home_GF = (home_away1(fixture[0])[3])   #MAIN
    home_GA = (home_away1(fixture[0])[4])   #MAIN

    time.sleep(1)
    #retrieve Away: DataFrame and Name, and assign to variables
    awayDF = (home_away2(fixture[1])[0])    
    awayName = (home_away2(fixture[1])[1])   #MAIN 
    away_GA = (home_away2(fixture[1])[2])   #MAIN 
    away_GF = (home_away2(fixture[1])[3])   #MAIN 

    time.sleep(1)
    #g
    h2hResult = h2hFormer(fixture[2], homeName)[0]       #MAIN
    h2hHomeName = h2hFormer(fixture[2], homeName)[1]   #MAIN
    h2hgoals = h2hFormer(fixture[2], homeName)[2]   #MAIN

    homeResult = homeCleaner(homeDF)          #MAIN

    awayResult = awayCleaner(awayDF)          #MAIN

    homeGenResult = genrlCleaner(homeDF)           #MAIN


    GOAL_PERCENT = ((home_GF+away_GA+home_GA+away_GF+h2hgoals)/16)*100
    WIN_PERCENT = (((((2*homeResult)+(2*awayResult)+homeGenResult)/25)+(0.125*h2hResult))/1.25)*100
    records = [homeName, awayName,compName,GOAL_PERCENT,WIN_PERCENT, homeResult,awayResult,homeGenResult,h2hHomeName,h2hResult,home_GF,away_GA, home_GA,away_GF,h2hgoals]
    with open('Match Analysis {x}.csv'.format(x=matchDay), 'a') as file:
        writer = csv.writer(file)
        writer.writerow(records)
    print(f"Fixture Number {num000} Extracted")
    num000+=1
    num001+=1

mainDF = pd.read_csv(f'Match Analysis {matchDay}.csv')
print (mainDF)


# In[ ]:





# In[ ]:




