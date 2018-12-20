
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

