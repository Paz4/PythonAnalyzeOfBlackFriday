
# coding: utf-8

# In[ ]:
from Libraries import *

##reading the data 
df = pd.read_csv('BlackFriday.csv')

def draw_pie_diagram(name):
    print(name)
    name.plot(kind='pie')
    plt.axis('equal')
    plt.show()

def draw_pie_diagram_advanced(name, lst=[], exp=None):
    print(name)
    if exp != None:
           exp = exp
    fig1, ax1 = plt.subplots(figsize=(12,7))
    ax1.pie(name, explode=exp, labels=lst, autopct='%1.1f%%', shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')  
    plt.tight_layout()
    plt.legend()
    plt.show()