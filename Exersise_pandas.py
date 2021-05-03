import pandas as pd

sal = pd.read_csv('salaries.csv')
print(sal)
'''
            Id       EmployeeName  ...         Agency  Status
0            1     NATHANIEL FORD  ...  San Francisco     NaN
1            2       GARY JIMENEZ  ...  San Francisco     NaN
2            3     ALBERT PARDINI  ...  San Francisco     NaN
3            4  CHRISTOPHER CHONG  ...  San Francisco     NaN
4            5    PATRICK GARDNER  ...  San Francisco     NaN
...        ...                ...  ...            ...     ...
148649  148650      Roy I Tillery  ...  San Francisco     NaN
148650  148651       Not provided  ...  San Francisco     NaN
148651  148652       Not provided  ...  San Francisco     NaN
148652  148653       Not provided  ...  San Francisco     NaN
148653  148654          Joe Lopez  ...  San Francisco     NaN

[148654 rows x 13 columns]
'''

print(sal.head())
'''
   Id       EmployeeName  ...         Agency  Status
0   1     NATHANIEL FORD  ...  San Francisco     NaN
1   2       GARY JIMENEZ  ...  San Francisco     NaN
2   3     ALBERT PARDINI  ...  San Francisco     NaN
3   4  CHRISTOPHER CHONG  ...  San Francisco     NaN
4   5    PATRICK GARDNER  ...  San Francisco     NaN

[5 rows x 13 columns]
'''

print(sal['BasePay'].mean())
#66325.4488404877

print(sal.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 148654 entries, 0 to 148653
Data columns (total 13 columns):
 #   Column            Non-Null Count   Dtype  
---  ------            --------------   -----  
 0   Id                148654 non-null  int64  
 1   EmployeeName      148654 non-null  object 
 2   JobTitle          148654 non-null  object 
 3   BasePay           148045 non-null  float64
 4   OvertimePay       148650 non-null  float64
 5   OtherPay          148650 non-null  float64
 6   Benefits          112491 non-null  float64
 7   TotalPay          148654 non-null  float64
 8   TotalPayBenefits  148654 non-null  float64
 9   Year              148654 non-null  int64  
 10  Notes             0 non-null       float64
 11  Agency            148654 non-null  object 
 12  Status            0 non-null       float64
dtypes: float64(8), int64(2), object(3)
memory usage: 14.7+ MB
None
'''

print(sal['OvertimePay'].max())
#245131.88

#Job title of JOSEPH DRISCOLL
print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])
'''
24    CAPTAIN, FIRE SUPPRESSION
Name: JobTitle, dtype: object
'''


#name of highest paid person (including benefits)
print(sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].max()])
'''
   Id    EmployeeName  ...         Agency  Status
0   1  NATHANIEL FORD  ...  San Francisco     NaN

[1 rows x 13 columns]
'''

#Average (mean) BasePay of all employees per year
print(sal.groupby('Year').mean()['BasePay'])
'''
Year
2011    63595.956517
2012    65436.406857
2013    69630.030216
2014    66564.421924
Name: BasePay, dtype: float64
'''

#Unique job titles
print(sal['JobTitle'].nunique())
#2159

#5 most common jobs
print(sal['JobTitle'].value_counts().head(5))
'''
Transit Operator                7036
Special Nurse                   4389
Registered Nurse                3736
Public Svc Aide-Public Works    2518
Police Officer 3                2421
Name: JobTitle, dtype: int64
'''

#Job titles represented by only one person in 2013
print(sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1))
#202

#how many people have word chief in their job title
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False

print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))      
#627
