import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

f = open("surveysays.csv", "r")
df = pd.read_csv("surveysays.csv")

""" sns.set(style = "dark")
sns.lineplot(y="How many Transformers movies have you seen? ", x="Age", markers = True, color = "orange",  data=df)
plt.xlim(15, 85) """

#sns.regplot(y="How many Transformers movies have you seen? ", x="Age", data=df)


""" dfnoDK1 = (df["Gender"] != "DK/REF")
dfnoDK2 = (df["Do you think it is acceptable or unacceptable to urinate in the shower?"] != "DK/REF")
dfnoDK3 = dfnoDK1 & dfnoDK2
(sns.boxplot( x = "Gender", y = "Age", hue = "Do you think it is acceptable or unacceptable to urinate in the shower?", data = df[dfnoDK3], color = "yellow"))  """

df1824 = df['Age Range'] == ("18-24")
df2534 = df['Age Range'] == ("25-34")
df1834 = df1824 | df2534

df3544 = df['Age Range'] == ("35-44")
df4554 = df['Age Range'] == ("45-54")
df3554 = df3544 | df4554

df5564 = df['Age Range'] == ("55-64")

df65 = df['Age Range'] == ("65+")




plt.subplot(2,2,1)
plt.title("Ages 18-34")
plt.ylim(0, 212)
plt.xlim(0, 300)
(sns.histplot(x = 'How many books, if any, have you read in the past year?', data = df[df1834], kde = False, bins= 60))
plt.subplot(2,2,2)
plt.title("Ages 35-54")
plt.ylim(0, 390)
plt.xlim(0, 300)
(sns.histplot( x = 'How many books, if any, have you read in the past year?', data = df[df3554], kde = False,  bins= 60))
plt.subplot(2,2,3)
plt.title("Ages 55-64")
plt.ylim(0, 207)
plt.xlim(0, 300)
(sns.histplot( x = 'How many books, if any, have you read in the past year?', data = df[df5564], kde = False,  bins= 42))
plt.subplot(2,2,4)
plt.title("Ages 65+")
plt.ylim(0, 185)
plt.xlim(0, 300)
(sns.histplot( x = 'How many books, if any, have you read in the past year?', data = df[df65], kde = False,  bins= 60))



""" dfnoDK = (df["What is your marital status?"] != "DK/REF")
plt.subplot(2,1,1)
sns.stripplot(x = "What is your marital status?", y = "Age", data = df[dfnoDK])
plt.subplot(2,1,2)
sns.violinplot(x = "What is your marital status?", y = "Age",data = df[dfnoDK]) """

""" dfnoDK1 = (df["Do you believe in ghosts?"] != "DK/REF")
dfnoDK2 = (df["Do you believe that climate change is real and caused by people, real but not caused by people, or not real at all?"] != "DK/REF")
noDK = dfnoDK1 & dfnoDK2
sns.barplot(y = "Income", x = "Age Range", hue = "Do you believe in ghosts?", order = ["18-24","25-34","35-44","45-54","55-64","65+" ],data = df[noDK])
  """



#sns.histplot(x ='Age Range', data = df)
plt.show()
#ideas
#peeing in shower by gender - men percent yes percent no vs women percent yes percent no
#books vs that true false question vs trump yes no

#for i in range(2,32):
 #   line = f.readline()
  #  q = line.split(",")
   # smartandsad = q[26]
    #peeing = q[27]
    #if smartandsad == "smartandsad":
     #   smartandsad = ""


#set_xscale("log")