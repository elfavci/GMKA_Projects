
"""
#SERIES:
pandas_series = pd.Series() #Series([], dtype: float64)
---
#data
numbers = [20,30,40,50]
pandas_series = pd.Series(numbers)
print(pandas_series)
0    20
1    30
2    40
3    50
dtype: int64
---
letters = ['a','b','c','d']
pandas_series = pd.Series(letters)
print(pandas_series)
0    a
1    b
2    c
3    d
dtype: object
---
letters = ['a','b','c',30]
pandas_series = pd.Series(letters)
print(pandas_series)
0     a
1     b
2     c
3    30
dtype: object
---
scalar = 5
pandas_series = pd.Series(scalar)
print(pandas_series)
0    5
dtype: int64
---
pandas_series = pd.Series(10,[0,1,2,3,4])
print(pandas_series)
0    10
1    10
2    10
3    10
4    10
dtype: int64
---
dictionary = {"a":12,"b":13,"c":24,"d":45}
pandas_series = pd.Series(dictionary)
print(pandas_series)
a    12
b    13
c    24
d    45
dtype: int64
---
random_numbers = np.random.randint(10,100,6)
pandas_series = pd.Series(random_numbers)
print(pandas_series)
0    16
1    63
2    99
3    52
4    54
5    97
dtype: int32
---
pandas_series = pd.Series([20,30,40,50],["a","b","c","d"])
print(pandas_series)
a    20
b    30
c    40
d    50
dtype: int64
---
pandas_series = pd.Series([20,30,40,50],["a","b","c","d"])
print(pandas_series["a"]) 20
---
pandas_series = pd.Series([20,30,40,50],["a","b","c","d"])
result =pandas_series[:2]
print(result)
a    20
b    30
dtype: int64
---
pandas_series = pd.Series([20,30,40,50],["a","b","c","d"])
result =pandas_series[-2:]
print(result)
c    40
d    50
dtype: int64
---
pandas_series = pd.Series([20,30,40,50],["a","b","c","d"])
result =pandas_series[["a","b","c"]]
print(result)
a    20
b    30
c    40
dtype: int64
---
pandas_series = pd.Series([20,30,40,50],["a","b","c","d"])
result =pandas_series.ndim 1
pandas_series = pd.Series([20,30,40,50],["a","b","c","d"])
pandas_series.dtype #int64
pandas_series.shape #(4,)
pandas_series.sum() #140
pandas_series.max() #50
result =pandas_series.min() #20
print(result)
---
pandas_series = pd.Series([20,30,40,50])
result =pandas_series +pandas_series
print(result)
0     40
1     60
2     80
3    100
dtype: int64

result = pandas_series+50
0     70
1     80
2     90
3    100
dtype: int64

result = np.sqrt(pandas_series)
0    4.472136
1    5.477226
2    6.324555
3    7.071068
dtype: float64

result = pandas_series>=50
0    False
1    False
2    False
3     True
dtype: bool

result = pandas_series%2 == 0
0    True
1    True
2    True
3    True
dtype: bool
---
opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 =pd.Series([40,30,20,10],["astra","corsa","grandland","insignia"])

total = opel2018 +opel2019
print(total)
print(total["astra"])
astra        60.0
corsa        60.0
grandland     NaN
insignia     20.0
mokka         NaN
dtype: float64
60.0
---
s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])
data = dict(apples =s1,oranges =s2)
df = pd.DataFrame(data)
print(df)
   apples  oranges
0       3        0
1       2        3
2       0        7
3       1        2
---
df = pd.DataFrame()
print(df)
Empty DataFrame
Columns: []
Index: []
---
df =pd.DataFrame([["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]])
print(df)
        0   1
0   Ahmet  50
1     Ali  60
2  Yağmur  70
3   Çınar  80
---
listed =[["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]]
df = pd.DataFrame(listed,index = [1,2,3,4],columns=["Name","Grade"])
print(df)
     Name  Grade
1   Ahmet     50
2     Ali     60
3  Yağmur     70
4   Çınar     80
---
dict ={"name":["ahmet","ali","yağmur","çınar"],"grade":[50,60,70,80]}
df = pd.DataFrame(dict)
print(df)
     name  grade
0   ahmet     50
1     ali     60
2  yağmur     70
3   çınar     80
---
dict_list = [
    {"name":"ahmet","grade":50},
    {"name":"ali","grade":60},
    {"name":"yağmur","grade":70},
    {"name":"çınar","grade":80}
]
df= pd.DataFrame(dict_list,index = ["212","234","455","545"])
print(df)
       name  grade
212   ahmet     50
234     ali     60
455  yağmur     70
545   çınar     80

"""

"""
#DATAFRAME FILTRELEME
data = np.random.randint(10,100,75).reshape(15,5) #15 satir 5 sutun random matris
df = pd.DataFrame(data,columns=["column1","column2","column3","column4","column5"])
print(df)
#result = df.columns
#result = df.head()
#result =df.head(10)
#result = df.tail()
#result = df.tail(10)
#print(result)
#result = df["column1"].head()

result =df.column1.head()
print(result)

resukt = df[["column1","column2"]].head(4)
print(resukt)


result = df[5:15][["column1","column2"]].head() #tail son 5 kaydi al
print(result)
   column1  column2
5       72       50
6       81       80
7       60       75
8       59       33
9       91       36
---
#result = df > 50
#result = df[df>50]
#result = df[df%2 == 0]
result = df["column1"]>50
---
#result = df[df["column1"]>50][["column1","column2"]]
result = df[(df["column1"]>50) & (df["column1"]<=70)]
---
result = df[(df["column1"]>50) | (df["column2"]>50)][["column1","column2"]]

print(result)
"""
"""
GROUPBY SORGULARI
import pandas as pd
import numpy as np

dataset = {
    "Departman":["Bilişim","İnsan Kaynakları","Üretim","Üretim","Bilişim","İnsan Kaynakları"],
    "Çalışan": ["Mustafa","Jale","Kadir","Zeynep","Murat","Ahmet"],
    "Maaş":[3000,3500,2500,4500,4000,2000]
    }
df = pd.DataFrame(dataset)
#print(df)

          Departman  Çalışan  Maaş
0           Bilişim  Mustafa  3000
1  İnsan Kaynakları     Jale  3500
2            Üretim    Kadir  2500
3            Üretim   Zeynep  4500
4           Bilişim    Murat  4000
5  İnsan Kaynakları    Ahmet  2000

DepGroup = df.groupby("Departman") #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000020889CA71F0>
#print(DepGroup)

x =DepGroup.sum()
print(x)

DepGroup = df.groupby("Departman").sum()
print(DepGroup)

                  Maaş
Departman             
Bilişim           7000
Üretim            7000
İnsan Kaynakları  5500

money = df.groupby("Departman").sum().loc["Bilişim"]
print(money)
Maaş    7000
Name: Bilişim, dtype: int64

money = int(df.groupby("Departman").sum().loc["Bilişim"])
print(money) #7000

print(df.groupby("Departman").count())#her bir departmanda calisan kisi sayisini verir
                  Çalışan  Maaş
Departman                      
Bilişim                 2     2
Üretim                  2     2
İnsan Kaynakları        2     2
---
x = df.groupby("Departman").max()
print(x)
#stringte alfabetik siraya gore maximum deger dizer
                  Çalışan  Maaş
Departman                      
Bilişim           Mustafa  4000
Üretim             Zeynep  4500
İnsan Kaynakları     Jale  3500
---
x = df.groupby("Departman").min()["Maaş"]["Bilişim"] #3000
print(x)
x = df.groupby("Departman").min()["Maaş"]
Departman
Bilişim             3000
Üretim              2500
İnsan Kaynakları    2000
Name: Maaş, dtype: int64  
---
average = df.groupby("Departman").mean()
print(average)
                    Maaş
Departman               
Bilişim           3500.0
Üretim            3500.0
İnsan Kaynakları  2750.0
---
average = df.groupby("Departman").mean()["Maaş"]["İnsan Kaynakları"]
print(average) #2750.0
"""

"""
#CONCATENATE, JOIN AND MERGE
import pandas as pd
import numpy as np
dataset1 ={
    "A":["A1","A2","A3","A4"],
    "B":["B1","B2","B3","B4"],
    "C":["C1","C2","C3","C4"],
}
dataset2 = {
    "A":["A5","A6","A7","A8"],
    "B":["B5","B6","B7","B8"],
    "C":["C5","C6","C7","C8"],
}
df1 = pd.DataFrame(dataset1,index=[1,2,3,4])
df2 = pd.DataFrame(dataset2,index =[5,6,7,8])

print(pd.concat([df1,df2]))
print(pd.concat([df1,df2],axis=0)) #axis=1 olunca hatali toplama olur Nan olur.

    A   B   C
1  A1  B1  C1
2  A2  B2  C2
3  A3  B3  C3
4  A4  B4  C4
5  A5  B5  C5
6  A6  B6  C6
7  A7  B7  C7
8  A8  B8  C8

#JOIN:
dataset1 = {
    "A":["A1","A2","A3","A4"],
    "B":["B1","B2","B3","B4"],
}
dataset2 = {
    "X":["X1","X2","X3","X4"],
    "Y":["Y1","Y2","Y3","Y4"],
}
df1 = pd.DataFrame(dataset1,index = [1,2,3,4])
df2 = pd.DataFrame(dataset2,index =[1,2,3,4])
#print(df1)
#print(df2)
x = df1.join(df2)
print(x)

    A   B   X   Y
1  A1  B1  X1  Y1
2  A2  B2  X2  Y2
3  A3  B3  X3  Y3
4  A4  B4  X4  Y4

---#MERGE:
dataset1 = {
    "A":["A1","A2","A3"],
    "B":["B1","B2","B3"],
    "key":["K1","K2","K3"]
}
dataset2 = {
    "X":["X1","X2","X3","X4"],
    "Y":["Y1","Y2","Y3","Y4"],
    "key":["K1","K2","K3","K4"]
}

df1 = pd.DataFrame(dataset1, index = [1,2,3])
print(df1)
    A   B key
1  A1  B1  K1
2  A2  B2  K2
3  A3  B3  K3
df2 = pd.DataFrame(dataset2,index=[1,2,3,4])
print(df2)
    X   Y key
1  X1  Y1  K1
2  X2  Y2  K2
3  X3  Y3  K3
4  X4  Y4  K4

x = pd.merge(df1,df2)
print(x)
pd.merge(df1,df2,on="key")
    A   B key   X   Y
0  A1  B1  K1  X1  Y1
1  A2  B2  K2  X2  Y2
2  A3  B3  K3  X3  Y3
"""
"""
#DATAFRAMELERIN MULTINDEX ILE GRUPLANMASI

import numpy as np
import pandas as pd
from numpy.random import randn
outerIndex = ["group1","group1","group1","group2","group2","group2","group3","group3","group3"]
innerIndex = ["index1","index2","index3","index1","index2","index3","index1","index2","index3"]
#listed = list(zip(outerIndex,innerIndex))
#print(listed)

hierarchy = list(zip(outerIndex,innerIndex))
hierarchy = pd.MultiIndex.from_tuples(hierarchy)
#print(hierarchy)
df = pd.DataFrame(randn(9,3),hierarchy,columns=["column1","column2","column3"])
print(df)

                column1   column2   column3
group1 index1  0.983494  1.098548 -1.140541
       index2  0.677285  0.542739 -0.476668
       index3  0.324188  0.148227  0.007548
group2 index1  1.477971  0.168786  0.938614
       index2 -2.111837  0.772315 -0.553425
       index3 -1.822859 -0.317372 -0.938243
group3 index1 -1.204699  1.011523  1.347347
       index2 -0.498383 -0.113886 -1.313887
       index3  0.070537  1.208605  0.062982
      
print(df["column1"]) #column 1'i alir

group1  index1    0.983494
        index2    0.677285
        index3    0.324188
group2  index1    1.477971
        index2   -2.111837
        index3   -1.822859
group3  index1   -1.204699
        index2   -0.498383
        index3    0.070537
Name: column1, dtype: float64

print(df.loc["group1"]) #sadece grup 1'i alir

  column1   column2   column3
index1  0.983494  1.098548 -1.140541
index2  0.677285  0.542739 -0.476668
index3  0.324188  0.148227  0.007548

print(df.loc[["group1","group2"]])

                column1   column2   column3
group1 index1  0.983494  1.098548 -1.140541
       index2  0.677285  0.542739 -0.476668
       index3  0.324188  0.148227  0.007548
group2 index1  1.477971  0.168786  0.938614
       index2 -2.111837  0.772315 -0.553425
       index3 -1.822859 -0.317372 -0.938243



print(df.loc["group1"].loc["index1"])#["column1"]

column1    0.579897
column2    0.439771
column3    0.978414
Name: index1, dtype: float64


df.index.names =["groups","indexes"]
print(df)

groups indexes                              
group1 index1   0.200088  1.893261  0.727379
       index2   0.317190  0.428234 -0.496449
       index3   0.147925  1.526954  0.398753
group2 index1  -1.220905  0.323771  0.050386
       index2   0.740607  0.375956  1.267043
       index3   0.094916 -0.572362  0.635408
group3 index1  -0.748444 -1.306776 -0.050056
       index2   1.427405 -0.122478  0.099277
       index3   0.149774  1.052635 -0.839345

print(df.xs("group1").xs("index1").xs("column1")) #1.4824383692122822


         column1   column2   column3
groups                              
group1  1.370309 -0.263315 -0.298697
group2  1.150319 -0.354528  0.820722
group3 -1.281941 -1.746661  0.266776
"""
"""
#KAYIP VERILERLE UGRASMA (MISSING DATA):
import numpy as np
import pandas as pd
arr = np.array([[10,20,np.nan],[5,np.nan,np.nan],[21,np.nan,10]])
print(arr)

[[10. 20. nan]
 [ 5. nan nan]
 [21. nan 10.]]

df = pd.DataFrame(arr,index = ["index1","index2","index3"],columns=["column1","column2","column3"])
print(df)
print(df.dropna())

Empty DataFrame
Columns: [column1, column2, column3]
Index: []

print(df.dropna(axis=1))

        column1
index1     10.0
index2      5.0
index3     21.0

print(df.dropna(thresh=2))#bir indexte minumum not a number veri varsa o indexi silme

        column1  column2  column3
index1     10.0     20.0      NaN
index3     21.0      NaN     10.0

print(df.fillna(value = 1))

        column1  column2  column3
index1     10.0     20.0      1.0
index2      5.0      1.0      1.0
index3     21.0      1.0     10.0

print(df.sum().sum()) #66.0
#df.size() #kac veri oldugunu dondurur
print(df.isnull().sum()) #NaN sayisini verir

column1    0
column2    2
column3    2
dtype: int64


column1    36.0
column2    20.0
column3    10.0
dtype: float64

print(df.isnull().sum().sum()) #4 toplam NaN sayisini verir

def calculateMean(x):
    totalSum = x.sum().sum()
    totalNum = x.size -x.isnull().sum().sum()
    return totalSum/totalNum
result = df.fillna(value=calculateMean(df))
print(result)

        column1  column2  column3
index1     10.0     20.0     13.2
index2      5.0     13.2     13.2
index3     21.0     13.2     10.0
"""
"""
#DATAFRAME OPERASYONLARI:

import numpy as np
import pandas as pd
df = pd.DataFrame({
    "Column1":[1,2,3,4,5,6],
    "Column2":[100,100,200,300,300,100],
    "Column3":["Mustafa","Kamil","Emre","Ayşe","Murat","Zeynep"]
})
print(df)

   Column1  Column2  Column3
0        1      100  Mustafa
1        2      100    Kamil
2        3      200     Emre
3        4      300     Ayşe
4        5      300    Murat
5        6      100   Zeynep

#print(df.head(n =3))#head max 5 deger dondurur.

   Column1  Column2  Column3
0        1      100  Mustafa
1        2      100    Kamil
2        3      200     Emre

print(df["Column2"].unique()) #[100 200 300] sutun 2 deki unique degerleri dondurur
print(df["Column2"].nunique()) #unique deger sayisini verir
print(df["Column2"].value_counts())

100    3
300    2
200    1
Name: Column2, dtype: int64

print(df[df["Column1"]>=4]) ##tek df true false deger dondurur.

   Column1  Column2 Column3
3        4      300    Ayşe
4        5      300   Murat
5        6      100  Zeynep


result = df[(df["Column1"] >= 4) & (df["Column2"] == 300)]
print(result)

   Column1  Column2 Column3
3        4      300    Ayşe
4        5      300   Murat

def times3(x):
    return x*3
print(df["Column2"].apply(times3))
#or
df["Column2"].apply(lambda x:x*3)

0    300
1    300
2    600
3    900
4    900
5    300
Name: Column2, dtype: int64

print(df["Column2"].apply(lambda x : x*2))

0    200
1    200
2    400
3    600
4    600
5    200
Name: Column2, dtype: int64

print(df["Column3"].apply(len))

0    7
1    5
2    4
3    4
4    5
5    6
Name: Column3, dtype: int64

print(df.drop("Column3",axis = 1))

   Column1  Column2
0        1      100
1        2      100
2        3      200
3        4      300
4        5      300
5        6      100

print(df.columns) #Index(['Column1', 'Column2', 'Column3'], dtype='object')
print(df.index)#RangeIndex(start=0, stop=6, step=1)
print(len(df.index))#6
print(df.index.names)#[None]
"""
"""
import  pandas as pd
#PIVOT TABLE:
df = pd.DataFrame({
    "Month":["March","April","May","March","April","May","March","April","May"],
    "City":["Ankara","Ankara","Ankara","Istanbul","Istanbul","Istanbul","İzmir","İzmir","İzmir"],
    "Damp":[10,25,50,21,67,80,30,70,75]
})
#print(df)
pivot = df.pivot_table(index = "Month",columns="City",values="Damp")
print(pivot)

City   Ankara  Istanbul  İzmir
Month                         
April      25        67     70
March      10        21     30
May        50        80     75

pivot1 = df.pivot_table(index = "City",columns="Month",values="Damp")
print(pivot1)

Month     April  March  May
City                       
Ankara       25     10   50
Istanbul     67     21   80
İzmir        70     30   75
"""
"""
import pandas as pd

dataset = pd.read_csv("USvideos.csv")
print(dataset)

newdataset = dataset.drop(["video_id","trending_date"],axis=1)
print(newdataset)

#excel file reading => pip install openpyxl
excelset = pd.read_excel("excelfile.xlsx")
#print(excelset)
excelset["column5"] = ["Mustafa","Murat","Coşkun","Udemy"]
#print(excelset)

excelset.to_excel("excelfilenew.xlsx")
#pip install lxml
new =pd.read_html("https://www.contextures.com/xlsampledata01.html",header=0)
print(new)

lenght = len(new)
#print(lenght)

"""















































