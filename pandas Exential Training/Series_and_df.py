import pandas as pd 

oo = pd.read_csv('pandas Exential Training/olympics.csv', skiprows = 4)
oo.head(3)
# print(oo)
print(oo.City.Athlete[:3])
