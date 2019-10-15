
# coding: utf-8

# In[1]:


import quandl
import pandas as pd


# In[2]:


df1 = pd.read_excel(r'/Users/kirstentai/Dropbox/MARK3085/Case_2/testconv_1.xlsx')


# In[3]:


#list of total impressions from real ad
impr_list_1 = df1['tot_impression'].tolist()
#print (impr_list_1)


# In[4]:


#list of days of wk from real ad

day_list_1 = df1['mode_impr_day'].tolist()


# In[5]:


#list of tot impressions and days of the week with most impressions from real ad

wk_list_1 = df1.loc[:,'tot_impression':'mode_impr_day']
print(wk_list_1)


# In[49]:


wk_list_1['combine'] = wk_list_1[['tot_impression', 'mode_impr_day']].values.tolist()
print(wk_list_1)


# In[50]:


week_impr_1 = wk_list_1['combine'].tolist()
print(week_impr_1)


# In[53]:


df2 = pd.read_excel(r'/Users/kirstentai/Dropbox/MARK3085/Case_2/control_ad.xlsx')


# In[54]:


#list of total impressions from control ad
impr_list_2 = df2['tot_impression'].tolist()


# In[140]:


#list of days of wk from control ad

day_list_2 = df2['mode_impr_day'].tolist()
print(day_list_2)


# In[55]:


#list of tot impressions and days of the week with most impressions from control ad
wk_list_2 = df2.loc[:,'tot_impression':'mode_impr_day']
print(wk_list_2)


# In[58]:


wk_list_2['combine'] = wk_list_2[['tot_impression', 'mode_impr_day']].values.tolist()
print(wk_list_2)


# In[59]:


week_impr_2 = wk_list_2['combine'].tolist()
print(week_impr_2)


# In[168]:


#dataframe adjusted to time limit
dfT1 = pd.read_excel(r'/Users/kirstentai/Dropbox/MARK3085/Case_2/real_time.xlsx')


# In[169]:


#list of total impressions from real ad
impr_list_T1 = dfT1['tot_impression'].tolist()


# In[170]:


#list of hours from real ad

hour_list_1 = dfT1['mode_impr_hour'].tolist()


# In[176]:


#list of tot impressions and hour with most impressions from real ad

impr_hour_table1 = dfT1.loc[:,'tot_impression':'mode_impr_hour']


# In[180]:


impr_hour_table1['combine'] = impr_hour_table1[['tot_impression', 'mode_impr_hour']].values.tolist()


# In[207]:


#2D list of [impressions,hour] for real ad
hour_impr_1 = impr_hour_table1['combine'].tolist()


# In[197]:


dfT2 = pd.read_excel(r'/Users/kirstentai/Dropbox/MARK3085/Case_2/control_time.xlsx')


# In[198]:


#list of total impressions from control ad
impr_list_T2 = dfT2['tot_impression'].tolist()


# In[199]:


#list of hours from control ad

hour_list_2 = dfT2['mode_impr_hour'].tolist()


# In[202]:


#list of tot impressions and hour with most impressions from control ad

impr_hour_table2 = dfT2.loc[:,'tot_impression':'mode_impr_hour']


# In[203]:


impr_hour_table2['combine'] = impr_hour_table2[['tot_impression', 'mode_impr_hour']].values.tolist()


# In[206]:


#2D list of [impressions,hour] for control
hour_impr_2 = impr_hour_table2['combine'].tolist()


# In[99]:


#count rows. counter for iterating through 'combine'
def row_count(df):
    total_rows = 0
    total_rows = df.shape[0]
    return total_rows


# In[ ]:


# counts how many conversions there are in a range (start to end) of total impressions.
def counter(list,start,end):
    how_many = 0
    for n in list:
        if n >= start and n <= end:
            how_many += 1
    return how_many


# In[91]:


# counts how many conversions there are in a day of the week (1mon - 7sun)
def day_count(dayList,day):
    how_many = 0
    i = 0
    for i in dayList:
        
        if i == day:
                how_many += 1
    
    return how_many


# In[209]:


# counts how many conversions there are in an hour
def hour_count(hourList,hour):
    how_many = 0
    i = 0
    for i in hourList:
        
        if i == hour:
                how_many += 1
    
    return how_many


# In[ ]:


# sums how many total impressions there are on a range (start to end)
def sum_ads(list,start,end):
    sum = 0
    for n in list:
        if n >= start and n <= end:
            sum = sum + n
    return sum


# In[109]:


# sums how many total impressions there are on a day of the wk

def sum_day(df,combineList,day):
    sum = 0
    n = 0
    while n < row_count(df):
        if combineList[n][1] == day:
            sum = sum + combineList[n][0]
        n += 1
    return sum


# In[210]:


# sums how many total impressions there are on an hour
def sum_hour(dfT,combineList,hour):
    sum = 0
    n = 0
    while n < row_count(dfT):
        if combineList[n][1] == hour:
            sum = sum + combineList[n][0]
        n += 1
    return sum


# In[212]:


hour_count(hour_list_1,10)/sum_hour(dfT1,hour_impr_1,10)


# In[329]:


#conversion rate as a function of the no. of ads displayed
def conversion_rate(list,start,end):
    conv_rate = 0
    sum = sum_ads(list,start,end)
    if sum != 0:
        conv_rate = (counter(list,start,end)/sum_ads(list,start,end))*100
    else:
        return "invalid, 0 impressions"
    return round(conv_rate,3)


# In[121]:


#conversion rate as a function of the day of the wk w max impr
def wk_conversion_rate(df,dayList,wkImprList,day):
    conv_rate = 0
    sum = sum_day(df,wkImprList,day)
    if sum != 0:
        conv_rate = (day_count(dayList,day)/sum_day(df,wkImprList,day))*100
    else:
        return "invalid: 0"
    return round(conv_rate,3)


# In[214]:


#conversion rate as a function of the day of the wk w max impr
def hr_conversion_rate(dfT,hourList,hrImprList,hour):
    conv_rate = 0
    sum = sum_hour(dfT,hrImprList,hour)
    if sum != 0:
        conv_rate = (hour_count(hourList,hour)/sum_day(dfT,hrImprList,hour))*100
    else:
        return "invalid: 0"
    return round(conv_rate,3)


# In[223]:


#testing function
print(hr_conversion_rate(dfT2,hour_list_2,hour_impr_2,15),
      hr_conversion_rate(dfT2,hour_list_2,hour_impr_2,16),
      hr_conversion_rate(dfT2,hour_list_2,hour_impr_2,17),
      hr_conversion_rate(dfT2,hour_list_2,hour_impr_2,18),
      hr_conversion_rate(dfT2,hour_list_2,hour_impr_2,19),
      hr_conversion_rate(dfT2,hour_list_2,hour_impr_2,20),
      hr_conversion_rate(dfT2,hour_list_2,hour_impr_2,21),
    hr_conversion_rate(dfT2,hour_list_2,hour_impr_2,22),
      hr_conversion_rate(dfT2,hour_list_2,hour_impr_2,23))
      
      


# In[221]:


print( hr_conversion_rate(dfT1,hour_list_1,hour_impr_1,15),

hr_conversion_rate(dfT1,hour_list_1,hour_impr_1,16),

hr_conversion_rate(dfT1,hour_list_1,hour_impr_1,17),

hr_conversion_rate(dfT1,hour_list_1,hour_impr_1,18),

hr_conversion_rate(dfT1,hour_list_1,hour_impr_1,19),

hr_conversion_rate(dfT1,hour_list_1,hour_impr_1,20),
hr_conversion_rate(dfT1,hour_list_1,hour_impr_1,21),

hr_conversion_rate(dfT1,hour_list_1,hour_impr_1,22),

hr_conversion_rate(dfT1,hour_list_1,hour_impr_1,23))


# # def rate_list(list, start, end):
#     i = 0
#     while i < 18:
#         
#         rate = conversion_rate(list,start,end)
#         print(rate)
#         start = start + 100
#         end = end + 100
#         i+=1

# In[335]:


rate_list(impr_list_1,1,100)


# In[336]:


rate_list(impr_list_2,1,100)


# In[230]:


import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np


# In[235]:


count_range_1 = [count(impr_list_1,1,100),count(impr_list_1,101,200),count(impr_list_1,201,300),count(impr_list_1,301,400),count(impr_list_1,401,500),
             count(impr_list_1,501,600),count(impr_list_1,601,700),count(impr_list_1,701,800),count(impr_list_1,801,900),count(impr_list_1,901,1000),
             count(impr_list_1,1001,1100),count(impr_list_1,1101,1200),count(impr_list_1,1201,1300),count(impr_list_1,1301,1400),count(impr_list_1,1401,1500),
             count(impr_list_1,1501,1600), count(impr_list_1,1601,1700), count(impr_list_1,1701,1800)]
count_range_1


# In[276]:


count_range_A = [count(impr_list_1,101,200),count(impr_list_1,201,300),count(impr_list_1,301,400),
                count(impr_list_2,401,500),count(impr_list_2,501,600)]
count_range_A


# In[257]:


count_range_2 = [count(impr_list_2,1,100),count(impr_list_2,101,200),count(impr_list_2,201,300),count(impr_list_2,301,400),count(impr_list_2,401,500),
             count(impr_list_2,501,600),count(impr_list_2,601,700),count(impr_list_2,701,800),count(impr_list_2,801,900),count(impr_list_2,901,1000),
             count(impr_list_2,1001,1100),count(impr_list_2,1101,1200),count(impr_list_2,1201,1300),count(impr_list_2,1301,1400),count(impr_list_2,1401,1500),
             count(impr_list_2,1501,1600), count(impr_list_2,1601,1700), count(impr_list_2,1701,1800)]
count_range_2


# In[277]:


count_range_B = [count(impr_list_2,101,200),count(impr_list_2,201,300),count(impr_list_2,301,400),
                 count(impr_list_2,401,500),count(impr_list_2,501,600)
             ]
count_range_B


# In[141]:


start_val = [1,101,201,301,401,501,601,701,801,901,1001,1101,1201,1301,1401,1501,1601,1701]


# In[142]:


end_val = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800]


# In[168]:


def ranges(start):
    for i in start:
        print(i,'-',i + 99)


# In[271]:


x_axis = ranges(start_val)


# In[280]:


# data to plot
n_groups = 5
conv_1 = count_range_A
conv_0 = count_range_B

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8

rects1 = plt.bar(index, conv_1, bar_width,
alpha=opacity,
color='b',
label='conv_1')

rects2 = plt.bar(index + bar_width, conv_0, bar_width,
alpha=opacity,
color='g',
label='conv_0')

plt.xlabel('Impression ranges')
plt.ylabel('Impression counts per range')
plt.title('Comparison of Conversions from ads')
plt.xticks(index + bar_width, ('B', 'C', 'D','E','F'))
plt.legend()

#('A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R')

plt.tight_layout()
plt.show()


# In[194]:


x_label = x_axis
y_pos = 500
y_axis = impr_range

plt.bar(y_pos,y_axis, align='center', alpha=10)
#plt.xticks(y_pos, x_label)
plt.ylabel('Count')
plt.title('ranges')

plt.show()

