import pandas as pd
df=pd.read_csv('diabetes-dataset.csv')
print(df.head(5))
Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \
0            2      138             62             35        0  33.6   
1            0       84             82             31      125  38.2   
2            0      145              0              0        0  44.2   
3            0      135             68             42      250  42.3   
4            1      139             62             41      480  40.7   

   DiabetesPedigreeFunction  Age  Outcome  
0                     0.127   47        1  
1                     0.233   23        0  
2                     0.630   31        1  
3                     0.365   24        1  
4                     0.536   21        0  

df.shape
(2000, 9)

df.columns
Index(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'],
      dtype='object')

print(df['Glucose'])
0       138
1        84
2       145
3       135
4       139
       ... 
1995     75
1996    179
1997     85
1998    129
1999     81
Name: Glucose, Length: 2000, dtype: int64

df[['Age','Glucose']]
	Age	Glucose
0	47	138
1	23	84
2	31	145
3	24	135
4	21	139
...	...	...
1995	33	75
1996	36	179
1997	42	85
1998	26	129
1999	25	81
2000 rows × 2 columns

df['Glucose'].mean()
121.1825