import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import requests as req
import lxml.html

from matplotlib import pyplot as plt


url="https://en.wikipedia.org/wiki/2002_Kenyan_general_election#:~:text=Elected%20President&text=Mwai%20Kibaki%20of%20the%20National,Simeon%20Nyachae%20of%20FORD%E2%80%93People."

results=req.get(url)

# print(results.text)
doc=BeautifulSoup(results.text,'lxml')

# print(doc.prettify())soup.find('table', { 'class' : 'table table-striped' })

#table=doc.find_all('table')[5]

table = doc.find('table', { 'class' : 'wikitable' })

headers = []

for i in table.find_all('th'):
    if( len(headers) <3):
        title = i.text
        headers.append(title)

columnValues=[]
for tr_data in table.find_all('tr'):
    _r =[]
    for x in tr_data.find_all('td'):
        if(x !=''):
            _r.append(x.text)
    if((len(_r)!=0) & (_r !='')):
        columnValues.append(_r)


# cleaning the data and removing Empty array elements
count=0
for individual in columnValues:
    if(len(individual)<1):
        columnValues.pop(count)
        count+=1

    else:
        innercount=0
        for j in individual:
            if (len(j)<1):
                individual.pop(innercount)
            innercount+=1
print(headers)
# print(columnValues)


# writing a new array of only the presidential results 

presidentResults=[]
for i in columnValues:
    if(len(presidentResults)<5):
        presidentResults.append(i)

#  getting only the first three colums from each candidate array
cleanPresResults=[]
for candData in presidentResults:
    reserve=candData
    reserve1=[]

    for item in reserve: 
        index=0
        if len(reserve1)<3:
            reserve1.append(item)
            index+=1
    cleanPresResults.append(reserve1)




dataframe=pd.DataFrame(cleanPresResults,columns=headers)
print(dataframe)
print(type(headers))
# print(dataframe)



# converting datatype of the votes column
dataframe['Votes']=dataframe['Votes'].str.replace(',','')
dataframe['Votes'].apply(pd.to_numeric)


# show datatypes of all collums


print('The changed datatype of Votes prints:')
print(dataframe)

#  sorting by the first categorical column.
# ///////////////////////////////////////////////


print(dataframe.dtypes)



# ploting using the two columns Candidate and the number of votes guthered
# first Plot

plt.pie(dataframe["Votes"], labels=dataframe["Candidate"])

# showing using Matplotlib as an Image
plt.show()

# second Analysed result in perty popularyty

plt.pie(dataframe["Votes"], labels=dataframe["Party"])
plt.show()
#     pass

# print(presidentResults)


