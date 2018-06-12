
# coding: utf-8

# # Project: Investigate a Dataset (Gapminder: Exploring Socio-Economic Behaviours!)
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# I first came across Gapminder in 2010 when I checked out Hans Rosling's TED talk "The seemingly impossible is possible". Watching that talk changed the way I looked at data ever since that day. <br>
# 
# This project is split into 2 very different topics: <br>
# Case-1:  __Oil Economics__ ( Reservoir Size, Production, Consumption and Gross Net Income Trends)<br>
# Case-2:  __Smoking Behaviours__ among different society classes.<br>
# 
# For the __Case-1__, I will explore:<br>
# 1. Which nations are top consumers, producers and owners of proven oil reservoirs?<br>
# 2. Distribution of consumption ratio (Consume/Produce) with production trends. <br>
# 3. How nations Gross Net Income (GNI)based on their consumption trend (exporter/importer)?<br>
# 
# For the __Case-2__, I will explore:<br>
# 1. Comparision between female and male smokers across all countries.<br>
# 2. How does the smoking population split among various groups of society (lower,lower_middle,lower_upper,higher)<br>
# 3. Relationships between per capita income and smoking behaviours<br>
# 4. Does life expectancy changes with income, if yes then how big is gap among lowest and highest classes?<br>
# 
# 

# In[1]:


# Importing libraries to be used
get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# <a id='wrangling'></a>
# # Data Wrangling
# 
# 
# ## General Properties

# ### Loading the excel files

# All excel files are loaded using pandas 'read_excel' version. Short notes are provided at end of each line providing context of data.

# In[2]:


# Load the data
oil_prod = pd.read_excel('Oil Production.xlsx', sheet_name = 'Data') #total production of oil
oil_proven = pd.read_excel('Oil Proved reserves.xlsx',sheet_name = 'Data') # total proven reserves of oil
oil_consume = pd.read_excel('Oil Consumption.xlsx',sheet_name = 'Data') #consumtion of oil
gni = pd.read_excel('indicatorGNItotalPPP.xlsx',sheet_name = 'Data') # Total gross net income converted to international dollars using purchasing power parity rates.
gnipc =pd.read_excel('indicatorGNIpercapitaATLAS.xlsx',sheet_name = 'Data') # Gross net income per capita, Atlas method (current US$) 
life_exp = pd.read_excel('indicator life_expectancy_at_birth.xlsx',sheet_name = 'Data') # Life expectancy in years
smk_female = pd.read_excel ('indicator_prevalence of current tobacco use among adults (%) female.xlsx',sheet_name = 'Data') #female smokers in %
smk_male = pd.read_excel ('indicator_prevalence of current tobacco use among adults (%) male.xlsx',sheet_name = 'Data') #male smokers in %               


# 
# ### Exploring the data and its properties prior to cleaning

# ##  Case-1: Oil Reservoir,Production & Consumption trends. Also how GNI of oil producing nations appears.

# #### Utilizing the head, info, dtypes and histograms to get a good idea of dataset and plan accordingly for cleaning the data.

# In[3]:


# Checking the first 5 rows for each dataset
oil_prod.head()
# Expected to see a lot of null values, as many countries are not oil producers


# #### Since all the files have 1st column named with file description, replacing the column 1 name with country name

# In[4]:


#Replacing the column 1 name with country name
oil_prod = oil_prod.rename(columns={oil_prod.columns[0]: 'Country'}) 
oil_proven = oil_proven.rename(columns={oil_proven.columns[0]: 'Country'}) 
oil_consume = oil_consume.rename(columns={oil_consume.columns[0]: 'Country'}) 
gni = gni.rename(columns={gni.columns[0]: 'Country'}) 


# Checking the data types and empty cells for each column

# In[5]:


oil_prod.info()


# Quick view histogram analysis

# In[6]:


#Exploring data with histogram.
oil_prod.hist(bins= 20, figsize= (10,10));
#production data is right skewed, most nations are non-oil producing.


# Describe to get overview of data

# In[7]:


oil_prod.describe()


# ##### Moving to 2nd Excel file

# In[8]:


oil_proven.head()
# Dashed out null values instead of NAN, need to clean this up.
# These are proven resources, contrary to production values resources might
# be available, but not viable to produce.


# Checking the data types and empty cells for each column

# In[9]:


oil_proven.info()


# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Quick view histogram analysis
# 

# In[10]:


#Exploring data with histogram.
oil_proven.hist(bins= 20, figsize= (10,10));
#right skewed data


# ##### Moving to 3rd Excel file

# In[11]:


oil_consume.head()
#Need to clean up dashed out values


# Checking the data types and empty cells for each column

# In[12]:


# Checking data info
oil_consume.info()

# Mixed data type and 2011 column doesn't have any data so cannot use that 
# year for analysis.


# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Quick view histogram analysis
# 

# In[13]:


#Exploring data with histogram.
oil_consume.hist(bins = 20, figsize= (10,8));
#right skewed data


# ##### Moving to 4th Excel file

# In[14]:


gni.head()
#large numeric values, will need to convert it into higher denomination


# Checking the data types and empty cells for each column

# In[15]:


# Checking data info
gni.info()
#1961-1979 data is empty
#2004 to 2009 has good data density, to be considered while selecting time range.


# Quick view histogram analysis

# In[16]:


#Exploring data with histogram.
gni.hist(bins= 20, figsize= (10,10));
#right skewed data, nothing a


# ##  Case- 2: Smoking trends among Men and Women, and how it relates to life expectancy.

# #### Utilizing the head, info, dtypes and histograms to get a good idea of dataset and plan accordingly for cleaning the data.

# In[17]:


life_exp.head()


# Checking the 2005 histogram for distrubution as this year will be used later for analysis.

# In[18]:


life_exp[2005].hist();


# In[19]:


life_exp.info()


# ##### Moving to 2nd Excel file

# In[20]:


smk_female.head()


# In[21]:


smk_female.info()


# Since the data is available for 3 years only, latest (2005) to be used for this analysis.

# ##### Moving to 3rd Excel file

# In[22]:


smk_male.head()


# In[23]:


smk_male.info()


# ##### Moving to 4th Excel file

# In[24]:


gnipc.head()


# Checking for number of null values

# In[25]:


gnipc['2005'].isnull().sum()


# In[26]:


gnipc.shape


# #### Since all the files have 1st column named with file description, replacing the column 1 name with country name

# In[27]:


#Replacing the column 1 name with country name
life_exp = life_exp.rename(columns={life_exp.columns[0]: 'Country'}) 
smk_male = smk_male.rename(columns={smk_male.columns[0]: 'Country'}) 
smk_female = smk_female.rename(columns={smk_female.columns[0]: 'Country'}) 
gnipc = gnipc.rename(columns={gnipc.columns[0]: 'Country'}) 


# # Data Cleaning (Selecting Year and removing the null values)

# Based on initial analysis of data type and null values in data, in this section we will proceed with further cleaning the data. For each of the sub data set, null values will be removed and time range of analysis will be set (depending on data available).

# ##  Case-1: Oil Reservoir,Production & Consumption trends. Also how GNI of oil producing nations appears.
# Since the latest available data for oil_proven (proven oil resources) is for 2008, let's focus on 2008 data. <br> Data below from 4 df's: <br>
#  >i)  oil_prod: Oil Produced <br>
#  >ii) oil_proven: Proven oil resources <br>
#  >iii)oil_consume: Oil consumed  <br>
#  >iv) gni: total gross net income converted to international dollars using PPP rates <br>

# ### oil_prod : Oil Produced in TOE

# Columns (Country and 2008(year)) are selected for analysis, null values dropped and renamed the column to prepare the data for merge later.

# In[28]:


# Selecting columns
oil_prod = oil_prod[['Country',2008]]

# Dropping null values

oil_prod = oil_prod.dropna()

#Renaming column

oil_prod.rename (columns={2008: 'oil_production'}, inplace = True)
oil_prod.head()


# As the value of oil produced is in toe, for better visualization converting from toe (tonne of equivalent) to mtoe(million tonne of equivalent)

# In[29]:


# Unit coversion
oil_prod['oil_production']= oil_prod['oil_production']*.0000001


# ### oil_proven : Proven oil resources in TOE

# Columns (Country and 2008(year)) are selected for analysis, null values dropped and renamed the column to prepare the data for merge later.

# In[30]:


# Selecting the country and specifying year
oil_proven = oil_proven[['Country',2008]]

# Dropping null values

oil_proven = oil_proven.dropna()

#renaming to prepare the data for merge later

oil_proven.rename (columns={2008: 'oil_proven'}, inplace = True)

oil_proven.head()


# As the value of oil reservoir is in toe, for better visualization converting from toe (tonne of equivalent) to mtoe(million tonne of equivalent)

# In[31]:


# Unit conversion
oil_proven['oil_proven'] = oil_proven['oil_proven']*.0000001


# ### oil_consume : Oil Consumed in TOE

# Columns (Country and 2008(year)) are selected for analysis, null values dropped and renamed the column to prepare the data for merge later.

# In[32]:


# Selecting the country and specifying year
oil_consume = oil_consume[['Country',2008]]

# Dropping null values

oil_consume = oil_consume.dropna()

#renaming to prepare the data for merge later

oil_consume.rename (columns={2008: 'oil_consume'}, inplace = True)
oil_consume.head()


# As the value of oil consumption is in toe, for better visualization converting from toe (tonne of equivalent) to mtoe(million tonne of equivalent)

# In[33]:


# Unit conversion
oil_consume['oil_consume'] = oil_consume['oil_consume']*.0000001


# ### gni_oil : total gross net income ($) converted to international dollars using PPP rates

# Columns (Country and 2008(year)) are selected for analysis, null values dropped and renamed the column to prepare the data for merge later.

# In[34]:


# Selecting the country and specifying year
gni_oil = gni.iloc[:,[0,48]]

# Dropping null values

gni_oil = gni_oil.dropna()

#renaming to prepare the data for merge later

gni_oil.rename (columns = {'2008' : 'gni_oil'}, inplace = True)
gni_oil.head()


# As the value of gni is in (\$) for better visualization converting from (\$) to million (m\$)

# In[35]:


# Unit conversion
gni_oil['gni_oil'] = gni_oil['gni_oil']*.0000001


# ### Merging the data for charts

# Cleaned up data is now merged using inner method. Also a consumption ratio is calculated, which will be used in next section for EDA. <br>
# Merged data will be stored under oil_trend_gni.

# In[36]:


oil_pro_merge = oil_proven.merge(oil_prod, how = 'inner', left_on = 'Country', right_on = 'Country')
oil_trend = oil_consume.merge(oil_pro_merge,how = 'inner', left_on = 'Country', right_on = 'Country')
oil_trend_gni = oil_trend.merge(gni_oil, how = 'inner', left_on = 'Country', right_on = 'Country')
oil_trend_gni ['consumption_ratio'] = oil_trend_gni['oil_consume']/oil_trend_gni['oil_production']
oil_trend_gni ['nation_category'] = np.where(oil_trend_gni['consumption_ratio'] < 1, 'exporter','importer')
oil_trend_gni.head(20)


# ##  Case- 2: Smoking trends among Men and Women, and how it relates to life expectancy.

# Create the bins and label the data into world bank classes based on GNI per capita. <br>
# Cleaning up GNI per capita data and renaming the column.

# In[37]:


# Bin and cut into classes
gnipc_df = gnipc[['Country', '2005']] 
gnipc_df = gnipc_df.dropna() 
bin_edges = [0, 1005, 3955, 12235, 50000]
bin_names = ['lower','lower_middle', 'upper_middle', 'higher']
gnipc_df['wb_class'] = pd.cut(gnipc_df['2005'], bin_edges, labels=bin_names)


# In[38]:


# Renaming the year column to income_pc for later analysis
gnipc_df.rename (columns={'2005': 'income_pc'}, inplace = True)


# Cleaning up Female smokers data and renaming the column for merging later.

# In[39]:


# selecting year 2005
smk_female_df = smk_female[['Country',2005]]

#dropping null values
smk_female_df = smk_female_df.dropna()

#renaming for later analysis
smk_female_df.rename (columns={2005: 'female_smoker'}, inplace = True)


# Cleaning up Male smokers data and renaming the column for merging later.

# In[40]:


# selecting year 2005
smk_male_df = smk_male[['Country',2005]]

#dropping null values
smk_male_df = smk_male_df.dropna()

#renaming for later analysis
smk_male_df.rename (columns={2005: 'male_smoker'}, inplace = True)


# Cleaning up Life expectancy data and renaming the column for merging later.

# In[42]:


# selecting year 2005
life_exp_df = life_exp[['Country',2005]]

#dropping null values
life_exp_df = life_exp_df.dropna()

#renaming for later analysis
life_exp_df.rename (columns={2005: 'life_expectancy'}, inplace = True)


# ### Merging the data for charts

# In[43]:


smk_cmb = smk_female_df.merge(smk_male_df, how = 'inner', left_on = 'Country', right_on = 'Country')
life_trend = life_exp_df.merge(smk_cmb, how = 'inner', left_on = 'Country', right_on = 'Country')
life_trend_gni = gnipc_df.merge(life_trend,how = 'inner', left_on = 'Country', right_on = 'Country')
life_trend_gni.head()


# ### Creating masks for filtering data based on class (low and higher)

# In[44]:


# Creating mask (low)
low= life_trend_gni.wb_class == 'lower'


# In[45]:


# Creating mask (higher)
higher = life_trend_gni.wb_class == 'higher'


# Checking mean of life expectancy difference between lower class and higher class.

# In[46]:


# Calculating mean using mask
life_trend_gni.life_expectancy[low].mean()


# In[47]:


# Calculating mean using mask
life_trend_gni.life_expectancy[higher].mean()


# <a id='eda'></a>
# # Exploratory Data Analysis
# 
# ### Research Question 1: Which Countries are highest producer, consumer and owner (proven reservoir) of oil and how these characteristic reflect on the Gross Net Income (gni)?

# #### Let's begin with how raw merged data looks in terms of oil consumption
# 

# In[48]:


sns.set_style("whitegrid")

ax = sns.barplot(x = "Country", y = 'oil_consume',data = oil_trend_gni );
ax.set_xticklabels(ax.get_xticklabels(), rotation=90);


# As it's clear that there are many small contributor's. In order to reach conclusions on defined problem statement,I will focus on Top 15 for each category.

# #### Top 15 oil consumer countries (oil_top_consumer)selected using .nlargest function

# In[49]:


# Sorting and limiting to top 15
oil_top_consumer = oil_trend_gni.sort_values('oil_consume').nlargest(15,'oil_consume')


# In[50]:


# Plot the values on bar chart
sns.set_style("whitegrid")
ax = sns.barplot(x = 'Country', y = 'oil_consume',data = oil_top_consumer );
ax.set_xticklabels(ax.get_xticklabels(), rotation=90);
ax.set_ylabel ('Consumption of Oil in MTOE')
ax.set_xlabel ('Countries')
ax.set_title("Top 15 Oil Consumer countries", size = 12);
sns.set(rc={'figure.figsize':(11.7,8.27)});


# *** 
#  Above chart clearly shows us that __US, China, India, Russia & Brazil__ are __top most oil consumers__ globally for year 2008.
# ***

# ### Top 15 oil producer countries (oil_top_producer)selected using .nlargest function

# In[51]:


# Sorting and limiting to top 15
oil_top_producer = oil_trend_gni.sort_values('oil_production').nlargest(15,'oil_production')


# In[52]:


# Plot the values on bar chart
sns.set_style("whitegrid")

ax = sns.barplot(x = "Country", y = 'oil_production',data = oil_top_producer);
ax.set_xticklabels(ax.get_xticklabels(), rotation=90);
ax.set_ylabel ('Production of Oil in MTOE')
ax.set_xlabel ('Countries')
ax.set_title("Top 15 Oil Producer countries", size = 12);
sns.set(rc={'figure.figsize':(11.7,8.27)});


# *** 
# Contrary to previous chart, Top producers are not same as Top consumers. <br>
# __Saudi Arabia, Russia, US, Iran and China__ are __top most oil producers__ globally for year 2008.
# ***

# ### Top 15 Proven oil reservoir countries (oil_top_proven)selected using .nlargest function

# In[53]:


# Sorting and limiting to top 15
oil_top_proven = oil_trend_gni.sort_values('oil_proven').nlargest(15,'oil_proven')


# In[54]:


# Plot the values on bar chart
sns.set_style("whitegrid")
ax = sns.barplot(x = "Country", y= 'oil_proven',data = oil_top_proven);
ax.set_xticklabels(ax.get_xticklabels(), rotation=90);
ax.set_ylabel ('Proven Oil Reservoir in MTOE')
ax.set_xlabel ('Countries')
ax.set_title("Top 15 Proven Oil Reservoir countries", size = 12);
sns.set(rc={'figure.figsize':(11.7,8.27)});


# *** 
# This chart shows us coutries with biggest proven reservoirs, however not all of them are biggest producers when compared to previous chart. <br>
# __Saudi Arabia & Iran__ are the only 2 in Top 5 that are common countries.<br>
# Rest __Kuwait, Venenzuela and UAE__ are among __top most proven oil reservoirs__ globally for year 2008.<br>
# 
# ***

# #### Exploring further relationships among factors

# Quick view of chart shows that we have outliers on x-axis (with a very big proven reservior), and y-axis (low proven reservoir but high consumption). 

# In[55]:


# Quick view scatter plot
oil_trend_gni.plot(y = 'consumption_ratio', x = 'oil_production', kind= 'scatter');


# In order to deal with this outlier, I filtered the df with multiple conditions.
# Similar result can be obtained with xlim, ylim but I want to use the same data in further analysis. Hence filter is created.

# #### Filter created to avoid plotting outliers

# In[56]:


#Filter applied
oil_trend_gni_filtered = oil_trend_gni[(oil_trend_gni['consumption_ratio'] <4) & (oil_trend_gni['gni_oil'] <400000)]


# Scatter chart after filter applied, now the spread appears to be better for analysis.

# In[57]:


# Scatter plot
sns.set_style("darkgrid")
oil_trend_gni_filtered.plot(x = 'consumption_ratio', y = 'oil_production', 
                            kind= 'scatter',title = 'Oil Production vs Consumption ratio');


# ***
# This is simple graphical representation of countries behavior with regards to Consumption ratio and production. <br>
# It is clear that with similar oil production levels, the consumption ratio is varying across countries. <br>
# ***

# ####  To analyze the behaviour of Nation's Gross Income based on their consumption.

# In[58]:


sns.lmplot (y= "gni_oil", x = "oil_consume", data = oil_trend_gni_filtered,
            hue="nation_category",col ="nation_category");


# #### From 2 charts above, below are the observations:
#    > Number of exporters are more than importers <br>
#      Slope for Importers GNI is higher than exporters. <br>
#      Since the countries are importing and consuming heavily, indicates that the infrastructure is developed and contributing to higher GNI.(Limitation: Need more supporting data to demostrate the relationship)<br> 
#      Majority of exporting nation has lower GNI and consumption concurrently, indicating they are relying on exports in other sectors from different countries. (Limitation: Need more supporting data to demostrate the relationship)
# 

# ### Research Question 2 : Smoking trends among Men and Women, how it relates to life expectancy and how these parameters vary with different class in society?

# ### Firstly let's compare the smoking trend among men and women 

# In[59]:


# Plotting the data
ax= sns.regplot(x= "male_smoker", y = "female_smoker", data = life_trend_gni)
ax.set_title("Male vs Female smokers", size = 12);


# ***
# Above chart indicates higher percentage of male smokers compared to the female smokers globally. In next few charts, more details will be explored.
# ***

# Next, let's explore how the smoking patterns vary among different class of society

# In[60]:


# Plot the split with class in society
sns.lmplot(x= "male_smoker", y = "female_smoker", data = life_trend_gni,
            hue="wb_class",col ="wb_class",col_wrap=2);


# ***
# #### Below are the observations:
#    > i.Female in lower class smoke less in most of the countries <br>
#     ii. In lower_middle class distribution starts to spread out and % of male smokers increase significantly<br>
#     iii. In upper middle women are smoking above average, and men are smoking slightly less than lower_middle.<br>
#     iv. Female in higer class smoke in most of countries, men on other hand have sligtely less % of smokers compared to all other classes.
# ***

# To visualize other correlations, let's utlize pairplots

# In[61]:


# Pair plots
sns.set(style="ticks")

sns.pairplot(life_trend_gni, hue="wb_class");


# ***
# #### Observations from Pairplots:
#    > i. Income distribution among classes is right skewed, mostly comprising of lower and lower_middle on left end.<br>
#      ii. Life expectancy among lower, lower_middle and upper_middle doesn't vary too much.<br>
#      iii.Lower and middle class females tend to smoke less generally (cluster on left lower end), whereas female from higher class and high income smoke in most of the cases.<br>
#      iv.Most of male smokers are from lower and middle section of society <br>
#      v. Life expectency is non linear to smoking percentages (make and female) 
#  ***

# Lastly, let's explore the data for certain class utilizing the masks created in previous section.

# In[62]:


# Histogram using masks
life_trend_gni.life_expectancy[low].hist(label = 'low', alpha = 0.5, bins = 10, figsize = (12,8))
life_trend_gni.life_expectancy[higher].hist(label = 'high', alpha = 0.5, bins = 10, figsize = (12,8))
plt.xlabel('Age in Years')
plt.ylabel('Number of Countries')
plt.title('Life Expectancy (Age) Distribution between Upper Class and Lower Class')
plt.legend( );


# ***
# #### Observations from Histogram:
#    > i. There is a clear relation between income and life expectancy <br>
#      ii. People with higher income (green) outlize the people with lowest income (blue) by average 20 years (mean calculated earlier).
#  ***

# <a id='conclusions'></a>
# ## Conclusions
# 
# Based on questions set in begining and analysis performed, below is my conclusion for each case.
# 
# __Case-1: Oil Economics__ 
#  > I found that the Nations with largest proven reservoirs are not always the one producing most. There could be several social/political/economical reasons for that, which were not covered as part of this analysis. <br>
#  > Similarly breaking the nations down into importer and exporter categories (based on consumption ratio) helps to understand the dynamics but need more data to establisht the facts. <br>
#  
#  __Case-2: Smoking Behaviours__
#  > With limited amount of data, I managed to explore the relationships among different sections of society as intended.
#  > One of the area not explored was correlating the findings to job sectors and working population for each country on top of sections of society.
#  > Using binning and cut function was instrumental in this analysis.
# 
# 
# ### Limitations
# 1. Inconsistency in data availability, for some datasets data was starting from 1965 and while others it was only limited to 3 years. <br>
# 2. During merging, had to make a choice either to have a lot of null values (Right/Left/Outer Join)or just go with Inner join (which I opted for) to get clean data. With this approach I had to sacrifice some of countries data.

# In[3]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'investigate-a-dataset-Gapminder_V3.ipynb'])

