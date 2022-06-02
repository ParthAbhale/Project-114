import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("data.csv")
value_y = df["Chance of Admit"].to_list()
value_x = df["GRE Score"].to_list()

m,c = 0.01 , -2.5
y = []

x = float(input("Enter your score: "))
Y = m*x+c

print("Your chances are {}".format(Y))

for x in value_x:
    y_value = m*x+c
    y.append(y_value)


fig = px.scatter(x = value_x, y = value_y)
fig.update_layout(shapes=[
    dict(type = 'line', 
        y0 = min(y),y1 = max(y),
        x0 = min(value_x),x1 = max(value_x))
])
fig.show()





