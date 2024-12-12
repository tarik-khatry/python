#import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#scores = pd.read_csv('scoresE.csv')
#finds the male with max marks in maths
#print(scores[scores['Gender'] == 'male']['MathScore'].max())  

#grading of students above 85 and between 75 to 85
#print(scores[scores['MathScore']>85].shape[0])
#print(scores[scores['MathScore'].between(75,85)].shape[0])

#finds students Female having score between 75 and 85 
#print(scores[(scores['MathScore'].between(75,85)) &  (scores['Gender']=='female') ].shape[0])

#above Average student numbers  
'''subject = ["MathScore","ReadingScore",'WritingScore']
for sub in subject:
    print("average in ", sub)
    avg = scores[sub].mean()
    print("male: ",scores[(scores['Gender'] == 'male') & (scores[sub]>avg)].shape[0])
    print("female: ",scores[(scores['Gender'] == 'female') & (scores[sub]>avg)].shape[0])
'''
#displaying index of groups
#print(scores.groupby('Gender').groups)

#Finding average and displaying their index 
'''subject = ["MathScore","ReadingScore",'WritingScore']
for sub in subject:
    print("average in ", sub)
    avg = scores[sub].mean()
    print(scores[scores[sub]>avg].groupby('Gender').groups)
'''
#matplotlib
'''x =np.array([2,4,5,7])
y =['akibda','ayanya','nabdya','tarkya']
plt.pie(x,labels=y,startangle=90)
plt.show()'''


