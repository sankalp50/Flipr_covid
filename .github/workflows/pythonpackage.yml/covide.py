import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d_trx=pd.read_excel("C:\\Users\\SANKALP\\Downloads\\train_covid.xlsx")
d_trx.head()

people_ID	Region	Gender	Designation	Name	Married	Children	Occupation	Mode_transport	cases/1M	...	HBB	d-dimer	Heart rate	HDL cholesterol	Charlson Index	Blood Glucose	Insurance	salary	FT/month	Infect_Prob
0	1	Bhubaneshwar	Female	Mrs	mansi	YES	1.0	Farmer	Public	2	...	93.0	233.0	82.0	58.0	27	7	3600000.0	1300000	2.0	49.135010
1	2	Bhubaneshwar	Female	Mrs	riya masi	YES	2.0	Farmer	Walk	2	...	56.0	328.0	89.0	68.0	5	6	1600000.0	400000	1.0	51.147880
2	3	Bhubaneshwar	Female	Mrs	sunita	NO	1.0	Cleaner	Public	2	...	137.0	213.0	77.0	43.0	40	6	3400000.0	900000	1.0	73.224000
3	4	Bhubaneshwar	Female	Mrs	anjali @ babli	YES	1.0	Driver	Car	2	...	167.0	275.0	64.0	60.0	27	7	700000.0	2300000	1.0	48.779225
4	5	Bhubaneshwar	Female	Mrs	champa karketta	NO	2.0	Manufacturing	Car	2	...	153.0	331.0	71.0	64.0	32	7	3200000.0	1100000	1.0	87.868800
5 rows × 28 columns

d_try=d_trx[["Infect_Prob"]]
d_trx= d_trx.drop(d_trx[["Infect_Prob"]],axis=1)

d_tex=pd.read_excel("C:\\Users\\SANKALP\\Downloads\\Test_dataset.xlsx")
d_tex.head()

people_ID	Region	Gender	Designation	Name	Married	Children	Occupation	Mode_transport	cases/1M	...	Platelets	HBB	d-dimer	Heart rate	HDL cholesterol	Charlson Index	Blood Glucose	Insurance	salary	FT/month
0	5942	Delhi	Female	Mrs	smt rekha prajapat	YES	2	Driver	Public	4	...	153	196	240	85	53	17	3	3900000	1300000	1
1	18664	Delhi	Male	Mr	nirmal	YES	2	Legal	Walk	4	...	95	138	241	81	61	2	5	1800000	1300000	1
2	5603	Delhi	Female	Mrs	pinky	YES	2	Sales	Car	4	...	40	166	236	88	47	24	3	5000000	2000000	2
3	5649	Delhi	Female	Mrs	pooja @aafrin	YES	2	Sales	Car	4	...	78	83	211	87	52	13	6	3100000	600000	2
4	5099	Delhi	Female	Mrs	anjali	YES	2	Business	Car	4	...	109	207	312	94	68	39	5	2300000	1500000	1
5 rows × 27 columns

d_to=pd.concat([d_trx,d_tex],axis=0)

d_to.isnull().sum()

people_ID                    0
Region                       0
Gender                       0
Designation                  0
Name                        52
Married                      0
Children                   311
Occupation                 747
Mode_transport               3
cases/1M                     0
Deaths/1M                    0
comorbidity                226
Age                          0
Coma score                   0
Pulmonary score              0
cardiological pressure      97
Diuresis                   716
Platelets                  924
HBB                         16
d-dimer                   1114
Heart rate                1114
HDL cholesterol             35
Charlson Index               0
Blood Glucose                0
Insurance                 1090
salary                       0
FT/month                   723
dtype: int64
type(d_to)
pandas.core.frame.DataFrame
d_to["Children"].value_counts()
2.0    8457
1.0    8335
0.0    8109
Name: Children, dtype: int64
d_to["Children"]=d_to["Children"].fillna(2.0)
d_to["Diuresis"].value_counts()
390.0    105
415.0     97
169.0     96
129.0     96
276.0     94
142.0     94
401.0     92
376.0     92
344.0     92
198.0     91
256.0     91
329.0     91
436.0     90
326.0     89
328.0     89
223.0     89
437.0     87
229.0     87
194.0     87
414.0     86
403.0     86
354.0     86
434.0     85
356.0     85
268.0     85
172.0     85
227.0     85
197.0     85
184.0     84
178.0     84
        ... 
410.0     60
318.0     60
316.0     60
166.0     60
274.0     59
448.0     59
309.0     59
335.0     59
196.0     59
138.0     58
300.0     58
170.0     58
202.0     57
210.0     57
176.0     57
322.0     57
342.0     57
438.0     56
321.0     56
449.0     55
447.0     54
118.0     54
352.0     53
204.0     53
325.0     53
429.0     53
133.0     52
341.0     52
333.0     50
397.0     49
Name: Diuresis, Length: 341, dtype: int64
d_to["Diuresis"]=d_to["Diuresis"].fillna(d_to["Diuresis"].mean())
d_to["FT/month"].value_counts()
2.0    8226
0.0    8137
1.0    8126
Name: FT/month, dtype: int64
d_to["FT/month"]=d_to["FT/month"].fillna(2.0)
d_to["HBB"].value_counts()
167.0    160
195.0    159
115.0    158
51.0     157
38.0     156
159.0    155
21.0     154
184.0    153
163.0    152
60.0     152
82.0     152
100.0    151
138.0    150
130.0    150
74.0     149
41.0     148
56.0     148
194.0    148
186.0    147
96.0     147
99.0     147
136.0    146
110.0    146
133.0    145
103.0    145
161.0    145
152.0    145
162.0    145
154.0    145
102.0    144
        ... 
54.0     120
73.0     120
188.0    120
125.0    119
101.0    119
173.0    119
176.0    118
190.0    118
124.0    118
25.0     118
105.0    118
155.0    118
203.0    117
196.0    117
93.0     117
120.0    117
132.0    116
78.0     115
160.0    115
139.0    115
116.0    114
151.0    114
164.0    114
198.0    114
107.0    112
90.0     112
61.0     111
69.0     109
146.0    108
32.0     107
Name: HBB, Length: 191, dtype: int64
d_to["HBB"]=d_to["HBB"].fillna(d_to["HBB"].mean())
d_to["HDL cholesterol"].value_counts()
61.0    749
45.0    746
57.0    743
38.0    742
41.0    730
67.0    728
64.0    724
66.0    718
60.0    718
63.0    717
59.0    717
51.0    713
62.0    708
56.0    708
39.0    708
44.0    706
37.0    699
65.0    698
47.0    698
53.0    697
58.0    696
43.0    696
49.0    696
40.0    694
42.0    686
36.0    682
48.0    680
70.0    675
46.0    675
68.0    672
35.0    672
52.0    665
50.0    663
69.0    659
54.0    659
55.0    640
Name: HDL cholesterol, dtype: int64
d_to["HDL cholesterol"]=d_to["HDL cholesterol"].fillna(d_to["HDL cholesterol"].mean())
d_to["Heart rate"].value_counts()
57.0     512
82.0     500
61.0     499
95.0     498
76.0     497
74.0     497
63.0     497
56.0     496
83.0     493
90.0     493
96.0     491
62.0     490
84.0     489
60.0     488
87.0     488
73.0     488
75.0     487
50.0     486
78.0     486
89.0     483
77.0     482
67.0     481
91.0     480
66.0     477
80.0     475
94.0     472
54.0     471
70.0     470
81.0     470
65.0     469
58.0     466
92.0     464
98.0     463
55.0     463
51.0     462
59.0     459
71.0     459
99.0     457
79.0     457
100.0    455
53.0     455
72.0     453
68.0     453
97.0     453
64.0     453
93.0     449
85.0     441
52.0     436
88.0     434
69.0     432
86.0     429
Name: Heart rate, dtype: int64
d_to["Heart rate"]=d_to["Heart rate"].fillna(d_to["Heart rate"].mean())
d_to.isnull().sum()
people_ID                    0
Region                       0
Gender                       0
Designation                  0
Name                        52
Married                      0
Children                     0
Occupation                 747
Mode_transport               3
cases/1M                     0
Deaths/1M                    0
comorbidity                226
Age                          0
Coma score                   0
Pulmonary score              0
cardiological pressure      97
Diuresis                     0
Platelets                  924
HBB                          0
d-dimer                   1114
Heart rate                   0
HDL cholesterol              0
Charlson Index               0
Blood Glucose                0
Insurance                 1090
salary                       0
FT/month                     0
dtype: int64
d_to=d_to.drop(d_to[["Name"]],axis=1)
d_to["Occupation"].value_counts()

Researcher       2820
Sales            2769
Legal            2737
Farmer           2704
Clerk            2698
Cleaner          2697
Driver           2693
Manufacturing    2683
Business         2664
Name: Occupation, dtype: int64

d_to["Occupation"]=d_to["Occupation"].fillna("Researcher")
d_to["Mode_transport"].value_counts()

Car       8435
Walk      8402
Public    8372
Name: Mode_transport, dtype: int64

d_to["Mode_transport"]=d_to["Mode_transport"].fillna("Car")
d_to["comorbidity"].value_counts()

Diabetes                  6316
Hypertension              6242
Coronary Heart Disease    6241
None                      6187
Name: comorbidity, dtype: int64

d_to["comorbidity"]=d_to["comorbidity"].fillna("Diabetes")
d_to["cardiological pressure"].value_counts()

Stage-01    6348
Normal      6341
Elevated    6243
Stage-02    6183
Name: cardiological pressure, dtype: int64

d_to["cardiological pressure"]=d_to["cardiological pressure"].fillna("Stage-01")
d_to["Platelets"].value_counts()

60.0     213
125.0    208
83.0     206
155.0    205
133.0    202
53.0     195
27.0     194
124.0    192
62.0     190
93.0     189
49.0     188
88.0     188
97.0     187
30.0     186
122.0    185
77.0     184
59.0     183
51.0     183
104.0    181
108.0    181
63.0     181
29.0     181
22.0     180
37.0     180
141.0    179
134.0    179
140.0    179
43.0     178
90.0     177
89.0     177
        ... 
84.0     153
121.0    153
15.0     153
158.0    152
111.0    152
153.0    152
72.0     152
105.0    151
79.0     151
145.0    151
149.0    151
35.0     150
136.0    150
86.0     149
130.0    149
76.0     148
48.0     147
131.0    147
85.0     146
75.0     146
118.0    146
41.0     144
139.0    144
152.0    143
38.0     143
115.0    143
156.0    143
18.0     140
45.0     137
112.0    134
Name: Platelets, Length: 146, dtype: int64
d_to["Platelets"]=d_to["Platelets"].fillna(d_to["Platelets"].mean())
d_to["d-dimer"].value_counts()
243.0    195
214.0    191
207.0    188
342.0    185
232.0    184
337.0    184
266.0    181
202.0    179
210.0    179
327.0    179
251.0    179
241.0    178
224.0    178
201.0    178
262.0    176
318.0    176
220.0    175
306.0    175
345.0    174
258.0    174
304.0    173
295.0    173
276.0    173
216.0    173
336.0    173
331.0    171
236.0    171
231.0    171
307.0    170
294.0    170
        ... 
283.0    148
235.0    148
309.0    147
246.0    147
324.0    147
346.0    147
209.0    147
250.0    147
247.0    147
288.0    147
259.0    147
211.0    145
313.0    145
274.0    144
203.0    144
206.0    143
284.0    143
238.0    143
225.0    143
290.0    143
240.0    142
334.0    142
316.0    142
299.0    141
315.0    141
248.0    141
282.0    140
205.0    139
213.0    137
226.0    127
Name: d-dimer, Length: 151, dtype: int64
d_to["d-dimer"]=d_to["d-dimer"].fillna(d_to["d-dimer"].mean())
d_to["Insurance"].value_counts()
4000000.0    575
2400000.0    536
2200000.0    536
2300000.0    531
600000.0     529
4700000.0    525
2600000.0    523
4300000.0    518
1400000.0    518
2500000.0    515
2100000.0    515
3300000.0    514
1100000.0    512
3200000.0    512
1300000.0    512
2000000.0    511
300000.0     510
3000000.0    510
4600000.0    509
2800000.0    508
3800000.0    506
1000000.0    505
3100000.0    504
3600000.0    504
2900000.0    504
800000.0     503
400000.0     502
4900000.0    500
3400000.0    500
2700000.0    499
1900000.0    498
1700000.0    496
3500000.0    493
3900000.0    493
4400000.0    489
5000000.0    489
1600000.0    488
4500000.0    487
900000.0     484
1800000.0    483
700000.0     482
3700000.0    482
1200000.0    481
4100000.0    475
4200000.0    473
4800000.0    465
500000.0     460
1500000.0    458
Name: Insurance, dtype: int64
d_to["Insurance"]=d_to["Insurance"].fillna(d_to["Insurance"].mean())
d_to.isnull().sum()
people_ID                 0
Region                    0
Gender                    0
Designation               0
Married                   0
Children                  0
Occupation                0
Mode_transport            0
cases/1M                  0
Deaths/1M                 0
comorbidity               0
Age                       0
Coma score                0
Pulmonary score           0
cardiological pressure    0
Diuresis                  0
Platelets                 0
HBB                       0
d-dimer                   0
Heart rate                0
HDL cholesterol           0
Charlson Index            0
Blood Glucose             0
Insurance                 0
salary                    0
FT/month                  0
dtype: int64
d_to=d_to.drop(d_to[["Name"]],axis=1)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-178-4ea421f5ad0c> in <module>()
----> 1 d_to=d_to.drop(d_to[["Name"]],axis=1)

~\Anaconda3\New folder\lib\site-packages\pandas\core\frame.py in __getitem__(self, key)
   1956         if isinstance(key, (Series, np.ndarray, Index, list)):
   1957             # either boolean or fancy integer index
-> 1958             return self._getitem_array(key)
   1959         elif isinstance(key, DataFrame):
   1960             return self._getitem_frame(key)

~\Anaconda3\New folder\lib\site-packages\pandas\core\frame.py in _getitem_array(self, key)
   2000             return self.take(indexer, axis=0, convert=False)
   2001         else:
-> 2002             indexer = self.loc._convert_to_indexer(key, axis=1)
   2003             return self.take(indexer, axis=1, convert=True)
   2004 

~\Anaconda3\New folder\lib\site-packages\pandas\core\indexing.py in _convert_to_indexer(self, obj, axis, is_setter)
   1229                 mask = check == -1
   1230                 if mask.any():
-> 1231                     raise KeyError('%s not in index' % objarr[mask])
   1232 
   1233                 return _values_from_object(indexer)

KeyError: "['Name'] not in index"
d_to.isnull().sum()
people_ID                 0
Region                    0
Gender                    0
Designation               0
Married                   0
Children                  0
Occupation                0
Mode_transport            0
cases/1M                  0
Deaths/1M                 0
comorbidity               0
Age                       0
Coma score                0
Pulmonary score           0
cardiological pressure    0
Diuresis                  0
Platelets                 0
HBB                       0
d-dimer                   0
Heart rate                0
HDL cholesterol           0
Charlson Index            0
Blood Glucose             0
Insurance                 0
salary                    0
FT/month                  0
dtype: int64
d_to.head()
people_ID	Region	Gender	Designation	Married	Children	Occupation	Mode_transport	cases/1M	Deaths/1M	...	Platelets	HBB	d-dimer	Heart rate	HDL cholesterol	Charlson Index	Blood Glucose	Insurance	salary	FT/month
0	1	Bhubaneshwar	Female	Mrs	YES	1.0	Farmer	Public	2	0	...	154.0	93.0	233.0	82.0	58.0	27	7	3600000.0	1300000	2.0
1	2	Bhubaneshwar	Female	Mrs	YES	2.0	Farmer	Walk	2	0	...	121.0	56.0	328.0	89.0	68.0	5	6	1600000.0	400000	1.0
2	3	Bhubaneshwar	Female	Mrs	NO	1.0	Cleaner	Public	2	0	...	124.0	137.0	213.0	77.0	43.0	40	6	3400000.0	900000	1.0
3	4	Bhubaneshwar	Female	Mrs	YES	1.0	Driver	Car	2	0	...	98.0	167.0	275.0	64.0	60.0	27	7	700000.0	2300000	1.0
4	5	Bhubaneshwar	Female	Mrs	NO	2.0	Manufacturing	Car	2	0	...	21.0	153.0	331.0	71.0	64.0	32	7	3200000.0	1100000	1.0
5 rows × 26 columns

d_to["Region"].value_counts()
Chennai               2581
Bengaluru             2573
Chandigarh            2563
Delhi                 2538
Bhubaneshwar          2537
Pune                  2503
Thiruvananthapuram    2502
Kolkata               2483
Mumbai                2475
Hyderabad             2457
Name: Region, dtype: int64
from sklearn.preprocessing import LabelEncoder
labelencoder_x=LabelEncoder()
d_to.values[:,1]=labelencoder_x.fit_transform(d_to.values[:,1])
d_to.values[:,2]=labelencoder_x.fit_transform(d_to.values[:,2])
d_to.values[:,3]=labelencoder_x.fit_transform(d_to.values[:,3])
d_to.values[:,4]=labelencoder_x.fit_transform(d_to.values[:,4])
d_to.head()
people_ID	Region	Gender	Designation	Married	Children	Occupation	Mode_transport	cases/1M	Deaths/1M	...	Platelets	HBB	d-dimer	Heart rate	HDL cholesterol	Charlson Index	Blood Glucose	Insurance	salary	FT/month
0	1	Bhubaneshwar	Female	Mrs	YES	1.0	Farmer	Public	2	0	...	154.0	93.0	233.0	82.0	58.0	27	7	3600000.0	1300000	2.0
1	2	Bhubaneshwar	Female	Mrs	YES	2.0	Farmer	Walk	2	0	...	121.0	56.0	328.0	89.0	68.0	5	6	1600000.0	400000	1.0
2	3	Bhubaneshwar	Female	Mrs	NO	1.0	Cleaner	Public	2	0	...	124.0	137.0	213.0	77.0	43.0	40	6	3400000.0	900000	1.0
3	4	Bhubaneshwar	Female	Mrs	YES	1.0	Driver	Car	2	0	...	98.0	167.0	275.0	64.0	60.0	27	7	700000.0	2300000	1.0
4	5	Bhubaneshwar	Female	Mrs	NO	2.0	Manufacturing	Car	2	0	...	21.0	153.0	331.0	71.0	64.0	32	7	3200000.0	1100000	1.0
5 rows × 26 columns

d_to= pd.get_dummies(d_to, prefix_sep='_', drop_first=True)
d_to.head()
people_ID	Children	cases/1M	Deaths/1M	Age	Coma score	Diuresis	Platelets	HBB	d-dimer	...	Mode_transport_Walk	comorbidity_Diabetes	comorbidity_Hypertension	comorbidity_None	Pulmonary score_<200	Pulmonary score_<300	Pulmonary score_<400	cardiological pressure_Normal	cardiological pressure_Stage-01	cardiological pressure_Stage-02
0	1	1.0	2	0	68	8	441.000000	154.0	93.0	233.0	...	0	0	1	0	0	0	1	1	0	0
1	2	2.0	2	0	64	15	279.901984	121.0	56.0	328.0	...	1	1	0	0	0	0	0	0	0	1
2	3	1.0	2	0	19	13	416.000000	124.0	137.0	213.0	...	0	0	0	1	0	1	0	0	0	0
3	4	1.0	2	0	33	9	410.000000	98.0	167.0	275.0	...	0	0	0	0	1	0	0	0	1	0
4	5	2.0	2	0	23	7	390.000000	21.0	153.0	331.0	...	0	1	0	0	0	0	1	1	0	0
5 rows × 48 columns

d_to_tr=d_to.values[:10714,:]
d_to_te=d_to.values[10714:,:]
#fitting dataset into Random Forest regression model
from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=200,random_state=0)
regressor.fit(d_to_tr,d_try)
C:\Users\SANKALP\Anaconda3\New folder\lib\site-packages\ipykernel_launcher.py:4: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().
  after removing the cwd from sys.path.
RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=None,
           max_features='auto', max_leaf_nodes=None,
           min_impurity_decrease=0.0, min_impurity_split=None,
           min_samples_leaf=1, min_samples_split=2,
           min_weight_fraction_leaf=0.0, n_estimators=200, n_jobs=1,
           oob_score=False, random_state=0, verbose=0, warm_start=False)
regressor.score(d_to_tr,d_try)
0.90714848070436371
#fitting dataset into decision tree regression model
from sklearn.tree import DecisionTreeRegressor
regressor_3=DecisionTreeRegressor(random_state=0)
regressor_3.fit(d_to_tr,d_try)
DecisionTreeRegressor(criterion='mse', max_depth=None, max_features=None,
           max_leaf_nodes=None, min_impurity_decrease=0.0,
           min_impurity_split=None, min_samples_leaf=1,
           min_samples_split=2, min_weight_fraction_leaf=0.0,
           presort=False, random_state=0, splitter='best')
regressor_3.score(d_to_tr,d_try)
0.99999999999756017
#predicting results from model
y_pred=regressor_3.predict(d_to_te)
y_pred
array([ 52.74015982,  52.33375489,  51.28722182, ...,  44.93902673,
        45.47750199,  45.37496218])
type(y_pred)
numpy.ndarray
a=np.asarray(y_pred)
np.savetxt("foo.csv", a, delimiter=",")
