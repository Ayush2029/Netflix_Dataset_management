#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Library used: pandas,numpy,seaborn,matplotlib,time,warning
#pandas: Pandas is used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.
#numpy: NumPy is used for the computation and processing of the multidimensional and single dimensional array elements.
#seaborn: Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
#matplotlib: Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
#time: The time module in python is an inbuilt module that needs to be imported when dealing with dates and times in python. It explains the use of various time-related functions that are defined in the time module in python along with the multiple code examples to help the users understand the topic better.
#warning: Warning is different from error in a program. If error is encountered, Python program terminates instantly. Warning on the other hand is not fatal. It displays certain message but program continues. Warnings are issued to alert the user of certain conditions which aren't exactly exceptions.
#Warning messages are displayed by warn() function defined in 'warning' module of Python's standard library. Warning is actually a subclass of Exception in built-in class hierarchy.
#Warnings Filters: The warnings filter controls whether warnings are ignored, displayed, or turned into errors (raising an exception).
#To access data from the CSV file, we require a function read_csv() from Pandas that retrieves data in the form of the data frame.
#The shape property returns a tuple containing the shape of the DataFrame.
#The info() method prints information about the DataFrame.
#The column() method is used to display all column names in data frame.
# The describe() method returns description of the data in the DataFrame.
# parameters in describe() : percentile, include, exclude, datetime_is_numeric
# here include='object' shows summary statistics of object columns whereas if we write nt.describe(), it shows general information based on all columns in form of single column.
# Pandas duplicated() method helps in analyzing duplicate values only. It returns a boolean series which is True only for Unique elements.
# sum is use to calculate num of duplicate value as boolean series may contain only two values as true and false. thus it may add values with false type to it.
# The isna() function is used to detect missing values and sum with it is used to find total num of missing values.
# The lstrip() method removes any leading characters 


# In[7]:


import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
import time


# In[8]:


import warnings
warnings.simplefilter('ignore')


# In[9]:


print("\033[1m"+"Checking and displaying structure of data file"+"\033[0m") # This sequence is used to print text in bold letter


# In[10]:


n = int(input("Enter Value Of No. of Data To Be Displayed: "))
nt = pd.read_csv('/Users/ayush/Desktop/netflix_titles.csv')
nt.head(n)


# In[11]:


nt.shape


# In[28]:


nt.info()


# In[29]:


nt.columns


# In[30]:


nt.describe()


# In[31]:


nt.describe(include = 'object')


# In[32]:


nt.duplicated().sum()


# In[33]:


print("\033[1m"+"*Conclusion:"+"\033[0m")
print("-The dataset has 8807 rows, 12 columns.")
print("-id and description columns are useless so we can drop them.")
print("-We have null values so we need to clean the dataset.")
print("-There is no full duplicates in the dataset.")


# In[34]:


print("\033[1m"+"Cleaning dataset"+"\033[0m")


# In[35]:


nt['country'].isna().sum()


# In[36]:


nt['country'] = nt['country'].fillna(nt['country'].mode()[0]) #Fills missing value gap with mode value of country
nt['country'] = nt['country'].astype(str)   # converts column datatype to string
nt['country'] = nt['country'].apply(lambda x : x.split(', ')[0]) 
#This line of code uses the apply() function to apply a lambda function to each element in the 'country' column. 
#The lambda function splits each value using the ', ' delimiter and keeps only the first part (before the first comma). 
#This is useful if the 'country' column contains multiple countries separated by commas, and you want to extract only the first country.
#Overall, these operations help in cleaning and preprocessing the 'country' column, ensuring it contains the most frequent value for missing data, converting all values to strings, and extracting the primary country in cases where multiple countries are listed in a single entry.


# In[37]:


nt['country'].value_counts()   #Find's the value count of each unique value in the given Series object.


# In[38]:


nt['rating'].unique() #shows unique values from the column


# In[39]:


nt['rating'].value_counts()   # shows values and its count from rating column


# In[40]:


nt['rating'] = nt['rating'].replace({'74 min' : np.nan, '84 min' : np.nan, '66 min': np.nan
                                    , 'TV-Y7-FV' : 'TV-Y7'})  # replacing not existing perfect num with nan and some other value using replace attribute
nt['rating'].unique()


# In[41]:


#compute the percentage of null values 
null_percent = nt.isnull().sum() * 100 / nt.shape[0]    #calculate null count for each column and divide by total dats of that column  and then multiply by 100 to find percentage of null value
null_percent.round(2).sort_values(ascending = False)  #sorts null percent value in descending and find value upto 2 decimal point


# In[42]:


nt['director'].isnull().sum()  #calculate num of blank field in director column


# In[43]:


nt['director'].value_counts()    #calculate count of each type of director


# In[44]:


nt['cast'].isnull().sum()  #calculate num of blank field in cast column


# In[45]:


nt['cast'].value_counts()    #calculate count of each type of cast


# In[46]:


#fill null values with new category
nt['director'].fillna('Unkown', inplace= True)
nt['cast'].fillna('Unkown', inplace= True)


# In[47]:


nt['cast'].isnull().sum()  #calculate num of blank field in cast column


# In[48]:


nt['cast'].value_counts()    #calculate count of each type of cast


# In[49]:


nt['director'].isnull().sum()  #calculate num of blank field in director column


# In[50]:


nt['director'].value_counts()    #calculate count of each type of director


# In[51]:


#fill null values with mode
mode_im = ['date_added','rating','duration']
for i in mode_im:
    nt[i] = nt[i].fillna(nt[i].mode()[0])


# In[52]:


# Two new columns with month and year is created with first word of date_added as month and last word as year
nt['month'] = nt['date_added'].apply(lambda x : x.lstrip().split(' ')[0])
nt['year'] = nt['date_added'].apply(lambda x : x.split(', ')[-1])


# In[53]:


nt.info()


# In[54]:


#drop useless columns
nt.drop(['show_id','date_added','description'],axis=1, inplace= True)
nt.isnull().sum()


# In[55]:


n = int(input("Enter no. of record to be displayed: "))
nt.head(n)


# In[56]:


print("\033[1m"+"Conclusion"+"\033[0m")
print("-I separated the countries in country column.")
print("-There are wrong values in rating column so i replce it with right values.")
print("-There are a lot of null values in director we impute the null values with unkown.")
print("-I used mode() to imp````ute null values with most frequent values in 'country','date_added','rating','duration'.")
print("-I added month and year columns to the data set.")
print("-finally the dataset now has no null values.")


# In[57]:


nt.shape


# In[58]:


print("\033[1m"+"Visualization"+"\033[0m")


# In[59]:


sns.countplot(x ='type', data = nt, palette="CMRmap")
plt.show()


# In[60]:


print("\033[1m"+"No.of viewers watching Movie is almost more than double of TV Show" +"\033[1m")


# In[174]:


sns.countplot(x ='type', hue = "release_year", data = nt,palette="Set2")
plt.legend([],[], frameon=False) #To hide legends 
plt.show()


# In[62]:


print("\033[1m"+"Max movies were released in 2017 with count>700 whereas Max TV Shows were released in 2020 with count almost 400" +"\033[1m")


# In[63]:


month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December']
df = nt.groupby('year')['month'].value_counts().unstack()[month_order]
#groups are made on basis of year and then for each month count is calculated.Whenever we use groupby function on 
#pandas dataframe with more than one aggregation function per column, the output is usually a multi-indexed column 
#where as the first index specifies the column name and the second column index specifies the aggregation function 
#name.


# In[70]:


fig,ax = plt.subplots(1,1,figsize = (12,8))
ax = sns.heatmap(df,cmap="Oranges_r")
plt.title('release denisty')
plt.show()


# In[75]:


print("\033[1m"+"Based on complete overview the best months to add new content are February and May, as these months have least releases among all the others" +"\033[1m")


# In[77]:


print("\033[1m"+"What is the most Genre in the data set movies / TV shows ?" +"\033[1m")


# In[79]:


#make a dataframe for movies only
movies = (nt['type'] == 'Movie')
movies_df = nt[movies]
movies_df.head(6)


# In[81]:


TV_Show = (nt['type'] == 'TV Show')
tv_df = nt[TV_Show]
tv_df.head(4)


# In[83]:


#genres for movies
#Here using movies_dataframe we split data using ',' whenever it occur and cut it and if it doesn't occur in generes we add it and give it fre as 1. the entire loop runs for collecting different such genere and calculate frequency of their occurence.
#g_m_df is a dataframe with list of diff genres and its No. of movie of such genre
genres = {}
for genre in movies_df['listed_in']:
    for i in genre.split(','):
        i= i.strip()
        if i not in genres:
            genres[i] =1
        else:
            genres[i] += 1
g_m_df = pd.DataFrame(list(genres.items()), columns= ['Genre', 'Number of Movies'])
g_m_df['Genre'].unique() # display of unique Genres


# In[84]:


g_m_df.sort_values(by = 'Number of Movies', ascending = False) #indexing is based on first occurence of such data and sort is applied on count of such no. of movie


# In[90]:


# The figsize() attribute can be used when you want to change the default size of a specific plot. figsize() takes two parameters- width and height (in inches). 
fig, ax = plt.subplots(figsize=(80, 20))
sns.barplot(x='Genre',y='Number of Movies',data=g_m_df.sort_values(by = 'Number of Movies', ascending = False),palette='crest_r')
plt.tick_params(labelsize=22) #tick_params() is used to change the appearance of ticks, tick labels, and gridlines.
plt.show()


# In[91]:


#genres for TV shows
#Here using TV Shows dataframe, we split data using ',' whenever it occur and cut it and if it doesn't occur in generes we add it and give it fre as 1. the entire loop runs for collecting different such genere and calculate frequency of their occurence.
#g_tv_df is a dataframe with list of diff genres and its No. of movie of such genre
genres2 = {}
for genre2 in tv_df['listed_in']:
    for i in genre2.split(','):
        if i not in genres2:
            genres2[i] =1
        else:
            genres2[i] += 1  
g_tv_df = pd.DataFrame(list(genres2.items()), columns= ['Genre', 'Number of TV show'])
g_tv_df['Genre'].unique() # display of unique Genres


# In[93]:


g_tv_df.sort_values(by = 'Number of TV show', ascending = False) #indexing is based on first occurence of such data and sort is applied on count of such no. of movie


# In[95]:


fig, ax = plt.subplots(figsize=(50, 20))
sns.barplot(y='Genre',x='Number of TV show',
            data=g_tv_df.sort_values(by = 'Number of TV show', ascending = False),
            palette='crest_r')
plt.tick_params(labelsize=25)
plt.show()


# In[96]:


print("\033[1m"+"We can see that most movie genre is International TV shows" +"\033[1m")


# In[98]:


print("\033[1m"+"In which year has been released largest number of movies/ TV Show?" +"\033[1m")


# In[101]:


pp = nt.groupby('release_year')['type'].value_counts().unstack(level=-1)


# In[103]:


fig, av = plt.subplots(1,1, figsize = (15,6))
ax = sns.lineplot(x='release_year', y='Movie', data=pp,linewidth = 3)
plt.tick_params(labelsize=9)
plt.show()


# In[105]:


fig, av = plt.subplots(1,1, figsize = (15,6))
ax = sns.lineplot(x='release_year', y='TV Show', data=pp,linewidth = 3)
plt.tick_params(labelsize=10)

plt.show()


# In[118]:


ig, ax = plt.subplots(figsize=(40, 20))
y = sns.countplot(x='release_year',data=nt,palette='crest_r', hue='type', order =nt['release_year'].value_counts().index[0:35])
plt.tick_params(labelsize=20)
y.legend(fontsize=80)
plt.show()
#here index[0:35] stats no. of years to be displayed on x axis of the graph


# In[121]:


print("\033[1m"+"for Movies in 2018" +"\033[1m")
print("\033[1m"+"for TV Shows in 2020" +"\033[1m")


# In[123]:


print("\033[1m"+"Which Country Has Released Most ?" +"\033[1m")


# In[127]:


ig, ax = plt.subplots(figsize=(50, 20))
y = sns.countplot(y='country',data=nt,palette='crest_r', order =nt['country'].value_counts().index[:25])
plt.tick_params(labelsize=50)
plt.show()
#here index[0:25] stats no. of country's to be displayed on y axis of the graph


# In[128]:


print("\033[1m"+"what is the content by Egyptians?" +"\033[1m")


# In[129]:


egp = nt[nt['country'] == 'Egypt'] # extract entire row data satisfying this condition
pd.DataFrame(dict(egp[['title', 'director']].items())) # dictionary creation with key as title and value as director item


# In[131]:


fig = plt.figure(figsize = (50,50))
ax =sns.countplot(y='director', data=egp,palette='crest_r')
plt.title('Egyptian directors on Netflix', fontsize=90)
plt.show()


# In[132]:


print("\033[1m"+"Youssif Chahine is the most popular egyptian director on netflix" +"\033[1m")


# In[134]:


print("\033[1m"+"What is the TV Show that has most seasons?" +"\033[1m")


# In[135]:


tv_df[['duration','title']].sort_values(by='duration', ascending =False)


# In[138]:


print("\033[1m"+"Grey's Anatomy is the TV Show that has most number of seasons." +"\033[1m")


# In[139]:


print("\033[1m"+"What is the most popular rating in movies/TV Shows?" +"\033[1m")


# In[140]:


fig, ax = plt.subplots(1,1,figsize=(15,5))
plt.tick_params(labelsize=14)
ax = sns.countplot(x='rating', data=nt, palette='crest_r', hue='type',order=nt['rating'].value_counts().index[0:18])
plt.legend(fontsize=20)
plt.show()


# In[143]:


print("\033[1m"+"For Movies and TV Shows TV-MA or Adults is the most popular rating." +"\033[1m")


# In[146]:


print("\033[1m"+"What is the range of duration to Movies/TV Shows?" +"\033[1m")


# In[147]:


#Replace min word && season word in the dataset with blankspace 
movies_df['duration'] = movies_df['duration'].str.replace("min", " ").str.replace("Season", " ").str.strip()
movies_df['duration'] = movies_df['duration'].astype('int32')


# In[148]:


#remove the 1 season movie
durayion_min = movies_df[movies_df['duration'] > 1]


# In[152]:


plt.figure(figsize=(35,30))
ax = sns.histplot(x= durayion_min['duration'], data=durayion_min, bins=50,palette ='crest_r')
plt.show()


# In[153]:


#clean duration column in tv shows dataframe
tv_df['duration'] = tv_df['duration'].str.replace("Seasons", " ").str.replace("Season", " ").str.strip()
tv_df['duration'] = tv_df['duration'].astype('int32')


# In[154]:


plt.figure(figsize=(30,10))
ax = sns.countplot(x= tv_df['duration'], data=tv_df,
                 palette ='crest_r')
plt.show()


# In[155]:


print("\033[1m"+"Most TV Shows are 1 season" +"\033[1m")


# In[169]:


sizes=nt['country'].value_counts()
z = np.zeros(748)
z[0] = 0.1
labels = []
for i in nt['country'].value_counts()[0:5].index:
    labels.append(i)
fig, ax = plt.subplots()
explode = (0.1, 0, 0, 0)
ax.pie(sizes[:5],explode=z[:5],labels = labels, radius = 2,shadow = True,
       textprops = {'fontsize':13}, colors=sns.color_palette('crest_r'))
plt.show()


# In[157]:


print("\033[1m"+"For Movies and TV Shows United States has released the most" +"\033[1m")


# In[161]:


print("\033[1m"+"Summmary" +"\033[1m")
print("- Based on the last complete year 2020 the best months to add new content are February and May.")
print("- The most movie genre is International Movies.")
print("- The most movie genre is International TV shows.")
print("- United States has releasd the most movies and Tv shows.")
print("- Movies duration range is between 90-100 mins.")
print("- Most tv-shows are 1 season.")
print("- For movies and tv shows TV-MA or Adults is the most popular rating.")


# In[164]:


print("---------------------------COMPLETE-------------------------------")

