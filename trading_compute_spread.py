import csv
import math
import pandas as pd


class Stock(object):   
    def __init__(self, ticker, quotes):
        self.ticker = ticker
        self.quotes = quotes        
      
    
def read(path):
    with open(path, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        return [(i[2], float(i[4])) for i in reader]
       
        
def create_Stock(ticker, path):
    return Stock(ticker, read(path))


def compute_spread(x, y):
    if len(x.quotes) != len(y.quotes):
        raise "Hell no!"
        
    result = [] 
    for i in range(0, len(x.quotes)):
        s = math.log(y.quotes[i][1]) - math.log(x.quotes[i][1]) 
        result.append((x.quotes[i][0], s))     
    return result
        
             


lkoh = create_Stock("LKOH", "LKOH.txt")
tatn = create_Stock("TATN", "TATN.txt")

spread = compute_spread(lkoh, tatn)

d = {
    'spread' : pd.Series([i[1] for i in spread])
}

get_ipython().magic('matplotlib inline')

df  = pd.DataFrame(d)
df.plot()
