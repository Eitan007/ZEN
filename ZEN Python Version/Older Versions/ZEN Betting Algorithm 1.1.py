#!/usr/bin/env python
# coding: utf-8

# # FUNCTIONS

# In[10]:



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
    x= homeDF, homeName, compName
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
    x= awayDF, awayName
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

def goals_home_away_Performance(link1, link2):
    homepg = requests.get(link1)
    awaypg = requests.get(link2)
    DF1 = pd.read_html(homepg.text, match='Venue')[0]
    DF2 = pd.read_html(awaypg.text, match='Venue')[0]

    DF1 = DF1[['Date','Comp', 'Venue', 'Result', 'GF', 'GA', 'Opponent']]
    DF2 = DF2[['Date','Comp', 'Venue', 'Result', 'GF', 'GA', 'Opponent']]

    DF1 = DF1[DF1['Comp'] == num45]
    DF2 = DF2[DF2['Comp'] == num45]
    
    DF1 = DF1.dropna(subset = ['Result'])
    DF2 = DF2.dropna(subset = ['Result'])
    
    DF1 = DF1[DF1['Venue'] == 'Home']
    DF2 = DF2[DF2['Venue'] == 'Away']

    DF1 = DF1.tail(5)
    DF2 = DF2.tail(5)

    DF1 = DF1.reset_index(drop=True)
    DF2 = DF2.reset_index(drop=True)

    DF1['GF'] = DF1['GF'].astype(int)
    DF2['GF'] = DF2['GF'].astype(int)

    DF1['GA'] = DF1['GA'].astype(int)
    DF2['GA'] = DF2['GA'].astype(int)

    DF1['Point'] = (DF1['GF'] != 0).astype('int')
    DF2['Point'] = (DF2['GA'] != 0).astype('int')

    DF11 = DF1.tail(2)
    DF11 = DF11.reset_index(drop=True)
    DF11['Point'] = (DF11['GA'] != 0).astype('int')

    DF12 = DF2.tail(2)
    DF12 = DF12.reset_index(drop=True)
    DF12['Point'] = (DF12['GF'] != 0).astype('int')

    home_Score = sum(DF1['Point'])
    away_Concede = sum(DF2['Point'])
    home_Concede = sum(DF11['Point'])
    away_Score = sum(DF1['Point'])
    return home_Score, away_Concede, home_Concede, away_Score














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




# # LIBRARIES

# In[14]:


#importing libraries
import pandas as pd
import requests
from datetime import date
import bs4 as bs
import time


# # GET SITE DATA

# In[16]:



matchDay= str(input('INPUT DATE (YYYY-MM-DD): '))
#Download site data as html
url = "https://fbref.com/en/matches/"+matchDay

Data = requests.get(url)

#Parses site html data  
soup = bs.BeautifulSoup(Data.text)


# # GET ALL TODAY'S FIXTURES 

# In[17]:


#Select all tables named 'stats_table' and append to a list named 'rawFixtures'
rawFixtures = soup.select('table.stats_table')

#get the href links of each team in fixtures
fixtureLinks = hrefing(rawFixtures)
#pair team href links according to their exact match fixtures
fixtureLinks = pairer(fixtureLinks)
#In order to preserve the integrity of the main fixtureLinks, create dummy list called fixtureLinks0, that will be used to run subsequent codes
fixtureLinks0 = fixtureLinks

#retrieves league link for each match fixture in the today's matches page
competitionList= leagueLkGenerator(rawFixtures)

#retrieve all available h2h hrefLinks from each fixture
h2h_links = hrefing_h2h(rawFixtures)
#arrange each h2hlink as single elements
h2h_links = h2hsingular(h2h_links)
#convert all elements within the list into string object
h2h_links = all_strings(h2h_links)


# # GET DATA FOR EACH TEAM IN TODAY'S FIXTURES 

# In[18]:


#retrieve home and away DataFrames, home and away names, and competition name and append to corresponding list
homeDFlist=[]
awayDFlist=[]
homeNamelist=[]  #MAJOR
awayNamelist=[]  #MAJOR
compNamelist=[] #MAJOR
print('\n\n')
#do this block of code for each element pair in fixtureLinks0
print(str(len(fixtureLinks0))+' Potential Fixtures\n\n')
for a in fixtureLinks0:
    list_groupH=home_away1(a[0])
    homeDFlist.append(list_groupH[0])
    homeNamelist.append(list_groupH[1])
    compNamelist.append(list_groupH[2])
    list_groupA=home_away2(a[1])
    awayDFlist.append(list_groupA[0])
    awayNamelist.append(list_groupA[1])
    #remove the first element pair form the fixtureLinks0 list, print number of element left in fixtureLinks0
    #print(list_groupH[1] + ' vs ' + list_groupA[1])
    time.sleep(1)
    print('Fixture '+str(len(homeNamelist))+' extracted')
print('Home DataFrame = ' +str(len(homeDFlist)))
print('Away DataFrame = ' +str(len(awayDFlist)))
print('homeNamelist = ' +str(len(homeNamelist)))
print('awayNamelist = ' +str(len(awayNamelist)))
print('compNamelist = ' +str(len(compNamelist)))


# #  TRANSFER PERFORMANCE DATA INTO LISTS

# In[19]:


h2hHomeName = []  #MAJOR

#create predictor lists for all prediction parameters, later to be turned into columns of a final Dataframe
homeResult = []  #MAJOR
awayResult = []  #MAJOR
homeGenResult = []  #MAJOR
h2hResult = []  #MAJOR

homeStanding = []  #MAJOR
awayStanding = []  #MAJOR
tableNum = []  #MAJOR

#perform this for each dataframe within the list called homeDFlist
for a in homeDFlist:
#select the last 5 home matches in the dataframe, calculate the performance, and return the value as the variable homeValue
    homeValue=homeCleaner(a)
#append homeValue to its corresponding predictor list (homeResult)
    homeResult.append(homeValue)

#perform this for each dataframe within the list called awayDFlist    
for a in awayDFlist:
#select the last 5 away matches in the dataframe, calculate the performance, and return the value as the variable awayValue
    awayValue=awayCleaner(a)
#append awayValue to its corresponding predictor list (awayResult)
    awayResult.append(awayValue)

#perform this for each dataframe within the list called homeDFlist        
for a in homeDFlist:
#select the last 5 matches in the dataframe, calculate the performance, and return the value as the variable homeGen    
    homeGen=genrlCleaner(a)
#append homeGen to its corresponding predictor list (homeGenResult)
    homeGenResult.append(homeGen)
print(str(len(homeResult))+' homeResult SCORES CALCULATED')
print(str(len(awayResult))+' awayResult SCORES CALCULATED')
print(str(len(homeGenResult))+' homeGenResult SCORES CALCULATED')


# #  TRANSFER H2H DATA INTO LISTS

# In[20]:


h2hDFlist1 = []
print(str(len(h2h_links))+ ' H2H tables found\n\n')
for links in h2h_links:
    pg = requests.get(links)
    h2h_table = pd.read_html(pg.text, match = 'Head-to-Head Matches Table')[0]
    h2h_table = h2h_table[['Home', 'Date','Score','Away']]
    h2h_table['Score'] = [str(l) for l in h2h_table['Score']] 
    h2h_table = h2h_table[h2h_table['Score']!= 'nan']          
    h2h_table = h2h_table.head(2)
    h2h_table = h2h_table.reset_index(drop=True)
    h2hDFlist1.append(h2h_table)
    print('Transfered Tables = ' + str(len(h2hDFlist1)))
    time.sleep(1)
    


# ##### GET VALUE FOR H2H

# In[64]:


h2hResult = []   #MAJOR
h2hHomeName = []   #MAJOR
for df in h2hDFlist1:
    try:
        df.loc[0, 'Home']
    except:
        h2hResult.append(1000)
        h2hHomeName.append('pass')
    else:
        if df.loc[0,'Home'] == df.loc[df.shape[0] - 1,'Home']:
            result=[]
            num = 0
            for a in df['Score']:
                if '(' in a:
                    hs = int(df.loc[num,'Score'][4])
                    As = int(df.loc[num,'Score'][6])
                    gd = hs - As
                    result.append(gd)
                else:
                    hs = int(df.loc[num,'Score'][0])
                    As = int(df.loc[num,'Score'][2])
                    gd = hs - As
                    result.append(gd)
                num+=1
            num43 = 0
            for b in result:
                if b > 0:
                    result[num43] = 1
                elif b < 0:
                    result[num43] = 0
                else:
                    result[num43] = 0.5
                num43+=1
            hn = df.loc[0, 'Home']
            result = sum(result)
        else:
            result=[]
            if '(' in df.loc[0,'Score']:
                hs = int(df.loc[0, 'Score'][4])
                As = int(df.loc[0, 'Score'][6])
                gd = hs - As
                result.append(gd)

            else:
                hs = int(df.loc[0, 'Score'][0])
                As = int(df.loc[0, 'Score'][2])
                gd = hs - As
                result.append(gd)

            if '(' in df.loc[1,'Score']:
                hs = int(df.loc[1, 'Score'][6])
                As = int(df.loc[1, 'Score'][4])
                gd = hs - As
                result.append(gd)

            else: 
                hs = int(df.loc[1, 'Score'][2])
                As = int(df.loc[1, 'Score'][0])
                gd = hs - As
                result.append(gd)
            num42 = 0
            for c in result:
                if c > 0:
                    result[num42] = 1
                elif c < 0:
                    result[num42] = 0
                else:
                    result[num42] = 0.5
                num42+=1
            result = sum(result)
            hn = df.loc[0, 'Home']
        h2hResult.append(result)
        h2hHomeName.append(hn)

print(str(len(h2hResult)) + ' H2H SCORES CALCULATED')


# In[63]:


#numm = 0
#for score in h2hResult:
 #   if score == 0:
  #      rez = 0.5
   #     h2hResult[numm] = rez
    #elif score == 1000:
     #   rez = 'pass'
      #  h2hResult[numm] = rez
    #elif score > 0:
     #   rez = 1
      #  h2hResult[numm] = rez
    #elif score == 'pass':
     #   rez = 'pass'
      #  h2hResult[numm] = rez
    #else:
     #   rez = 0
      #  h2hResult[numm] = rez
    #numm+=1


# # TRANSFER 0VER 0.5 PERFORMANCE DATA INTO LISTS

# ######  H2H 

# In[93]:


h2h_goal_list = []   #MAJOR
for df in h2hDFlist1:
    gtlist = []
    num3 = 0
    for a in df['Score']:
        if '(' in a:
            hs = int(df.loc[num3,'Score'][4])
            As = int(df.loc[num3,'Score'][6])
            gt = hs + As
            gtlist.append(gt)
        else:
            hs = int(df.loc[num3,'Score'][0])
            As = int(df.loc[num3,'Score'][2])
            gt = hs + As
            gtlist.append(gt)
        num3 += 1
    num4 = 0
    for b in gtlist:
        if b == 0 or b == 1:
            gtlist[num4] = 0
        else:
            gtlist[num4] = 1
        num4 += 1
    h2hscore1 = sum(gtlist)
    h2h_goal_list.append(h2hscore1)
print('h2h Scores Calculated = '+str(len(h2h_goal_list)))


# ###### HOME SCORES IN LAST 5 MATCHES

# In[ ]:


home_GF = []
away_GA = []
home_GA = []
away_GF = []

num45 = 0
for (a,b) in fixtureLinks:  
    homepg = requests.get(a)
    awaypg = requests.get(b)
    DF1 = pd.read_html(homepg.text, match='Venue')[0]
    DF2 = pd.read_html(awaypg.text, match='Venue')[0]

    DF1 = DF1[['Date','Comp', 'Venue', 'Result', 'GF', 'GA', 'Opponent']]
    DF2 = DF2[['Date','Comp', 'Venue', 'Result', 'GF', 'GA', 'Opponent']]

    DF1 = DF1[DF1['Comp'] == compNamelist[num45]]
    DF2 = DF2[DF2['Comp'] == compNamelist[num45]]
    
    DF1 = DF1.dropna(subset = ['Result'])
    DF2 = DF2.dropna(subset = ['Result'])
    
    DF1 = DF1[DF1['Venue'] == 'Home']
    DF2 = DF2[DF2['Venue'] == 'Away']

    DF1 = DF1.tail(5)
    DF2 = DF2.tail(5)

    DF1 = DF1.reset_index(drop=True)
    DF2 = DF2.reset_index(drop=True)

    DF1['GF'] = DF1['GF'].astype(int)
    DF2['GF'] = DF2['GF'].astype(int)

    DF1['GA'] = DF1['GA'].astype(int)
    DF2['GA'] = DF2['GA'].astype(int)

    DF1['Point'] = (DF1['GF'] != 0).astype('int')
    DF2['Point'] = (DF2['GA'] != 0).astype('int')

    DF11 = DF1.tail(2)
    DF11 = DF11.reset_index(drop=True)
    DF11['Point'] = (DF11['GA'] != 0).astype('int')

    DF12 = DF2.tail(2)
    DF12 = DF12.reset_index(drop=True)
    DF12['Point'] = (DF12['GF'] != 0).astype('int')

    #home_Score = 
    #away_Concede = )
    #home_Concede = )
    #away_Score = )
    home_GF.append(sum(DF1['Point']))
    away_GA.append(sum(DF2['Point']))
    home_GA.append(sum(DF11['Point']))
    away_GF.append(sum(DF12['Point']))
    num45+=1
    print('Fixture '+str(len(home_GF))+ ' Goal Records Calculated' )
    time.sleep(2)


# In[41]:


#homeStanding 
#awayStanding 
#tableNum


#homeNamelist=[]  #MAJOR
#awayNamelist=[]  #MAJOR
#compNamelist=[] #MAJOR

#homeResult = []  #MAJOR
#awayResult = []  #MAJOR
#homeGenResult = []  #MAJOR
#h2hHomeName = []   #MAJOR
#h2hResult = []  #MAJOR

#home_GF
#away_GA
#home_GA
#away_GF
#h2h_goal_list


# In[ ]:


num78 = 0
for a in homeNamelist:
    try:
        h2hHomeName[num78][:3] not in a 
    except:
        h2hResult[num78] = 'Pass'
    else:
        if h2hHomeName[num78][:3] not in a:
            h2hResult[num78] = 2 - h2hResult[num78]
        else:
            pass
    num78+=1
        
        
    


# In[ ]:

#pd.set_option('max_columns', None)
_tbl = {'HOME': homeNamelist, 'AWAY': awayNamelist, 'COMP': compNamelist, 'HOME FORM': homeResult, 'AWAY FORM': awayResult, 'HOME GEN FORM': homeGenResult, 'h2h HOME': h2hHomeName, 'H2H FORM': h2hResult, 'HOME TO SCORE': home_GF, 'AWAY TO CONCEDE': away_GA, 'HOME TO CONCEDE': home_GA, 'AWAY TO SCORE': away_GF, 'H2H GOAL': h2h_goal_list }
mainDF = pd.DataFrame(_tbl)

mainDF['OVER 0.5 %'] = ((mainDF['HOME TO SCORE'] + mainDF['AWAY TO CONCEDE'] + mainDF['HOME TO CONCEDE'] + mainDF['AWAY TO SCORE'] + mainDF['H2H GOAL'])/16) * 100
mainDF['1X %'] = ((((2 * mainDF['HOME FORM'] + 2 * mainDF['AWAY FORM'] + mainDF['HOME GEN FORM'])/25) + (0.125 * mainDF['H2H FORM']))/1.25) * 100
cols = mainDF.columns.tolist()
cols = cols[:3] + cols[-2:] #+ cols[3:13]
mainDF1 =mainDF[cols]


# In[90]:


print(mainDF)
print('\n\n')
print (mainDF1)

