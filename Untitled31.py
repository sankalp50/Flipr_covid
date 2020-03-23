
# coding: utf-8

# In[138]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[139]:


d_trx=pd.read_excel("C:\\Users\\SANKALP\\Downloads\\train_covid.xlsx")


# In[140]:


d_trx.head()


# In[141]:


d_try=d_trx[["Infect_Prob"]]


# In[142]:


d_trx= d_trx.drop(d_trx[["Infect_Prob"]],axis=1)


# In[143]:


d_tex=pd.read_excel("C:\\Users\\SANKALP\\Downloads\\Test_dataset.xlsx")


# In[144]:


d_tex.head()


# In[145]:


d_to=pd.concat([d_trx,d_tex],axis=0)


# In[146]:


d_to.isnull().sum()


# In[147]:


type(d_to)


# In[148]:


d_to["Children"].value_counts()


# In[149]:


d_to["Children"]=d_to["Children"].fillna(2.0)


# In[150]:


d_to["Diuresis"].value_counts()


# In[151]:


d_to["Diuresis"]=d_to["Diuresis"].fillna(d_to["Diuresis"].mean())


# In[152]:


d_to["FT/month"].value_counts()


# In[153]:


d_to["FT/month"]=d_to["FT/month"].fillna(2.0)


# In[154]:


d_to["HBB"].value_counts()


# In[155]:


d_to["HBB"]=d_to["HBB"].fillna(d_to["HBB"].mean())


# In[156]:


d_to["HDL cholesterol"].value_counts()


# In[157]:


d_to["HDL cholesterol"]=d_to["HDL cholesterol"].fillna(d_to["HDL cholesterol"].mean())


# In[158]:


d_to["Heart rate"].value_counts()


# In[159]:


d_to["Heart rate"]=d_to["Heart rate"].fillna(d_to["Heart rate"].mean())


# In[160]:


d_to.isnull().sum()


# In[161]:


d_to=d_to.drop(d_to[["Name"]],axis=1)


# In[162]:


d_to["Occupation"].value_counts()


# In[163]:


d_to["Occupation"]=d_to["Occupation"].fillna("Researcher")


# In[164]:


d_to["Mode_transport"].value_counts()


# In[165]:


d_to["Mode_transport"]=d_to["Mode_transport"].fillna("Car")


# In[166]:


d_to["comorbidity"].value_counts()


# In[167]:


d_to["comorbidity"]=d_to["comorbidity"].fillna("Diabetes")


# In[168]:


d_to["cardiological pressure"].value_counts()


# In[169]:


d_to["cardiological pressure"]=d_to["cardiological pressure"].fillna("Stage-01")


# In[170]:


d_to["Platelets"].value_counts()


# In[171]:


d_to["Platelets"]=d_to["Platelets"].fillna(d_to["Platelets"].mean())


# In[172]:


d_to["d-dimer"].value_counts()


# In[173]:


d_to["d-dimer"]=d_to["d-dimer"].fillna(d_to["d-dimer"].mean())


# In[174]:


d_to["Insurance"].value_counts()


# In[175]:


d_to["Insurance"]=d_to["Insurance"].fillna(d_to["Insurance"].mean())


# In[176]:


d_to.isnull().sum()


# In[178]:


d_to=d_to.drop(d_to[["Name"]],axis=1)


# In[179]:


d_to.isnull().sum()


# In[180]:


d_to.head()


# In[181]:


d_to["Region"].value_counts()


# In[186]:


from sklearn.preprocessing import LabelEncoder
labelencoder_x=LabelEncoder()
d_to.values[:,1]=labelencoder_x.fit_transform(d_to.values[:,1])
d_to.values[:,2]=labelencoder_x.fit_transform(d_to.values[:,2])
d_to.values[:,3]=labelencoder_x.fit_transform(d_to.values[:,3])
d_to.values[:,4]=labelencoder_x.fit_transform(d_to.values[:,4])


# In[185]:


d_to.head()


# In[187]:


d_to= pd.get_dummies(d_to, prefix_sep='_', drop_first=True)


# In[188]:


d_to.head()


# In[190]:


d_to_tr=d_to.values[:10714,:]
d_to_te=d_to.values[10714:,:]


# In[201]:


#fitting dataset into Random Forest regression model
from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=200,random_state=0)
regressor.fit(d_to_tr,d_try)


# In[213]:


regressor.score(d_to_tr,d_try)


# In[209]:


#fitting dataset into decision tree regression model
from sklearn.tree import DecisionTreeRegressor
regressor_3=DecisionTreeRegressor(random_state=0)
regressor_3.fit(d_to_tr,d_try)


# In[216]:


regressor_3.score(d_to_tr,d_try)


# In[215]:


#predicting results from model
y_pred=regressor_3.predict(d_to_te)


# In[212]:


y_pred


# In[217]:


type(y_pred)


# In[218]:


a=np.asarray(y_pred)
np.savetxt("foo.csv", a, delimiter=",")

