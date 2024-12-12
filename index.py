import pandas as pd

scores = pd.read_csv('scoresE.csv')
#finds the male with max marks in maths
#print(scores[scores['Gender'] == 'male']['MathScore'].max())  

print(scores[scores['MathScore']>85].shape[0])
print(scores[scores['MathScore'].between(75,85)].shape[0])