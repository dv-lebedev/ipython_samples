
import numpy as np
import pandas as pd
import math

test_prices = map(math.log, [100, 150, 125, 200, 175, 225, 300, 350])
x = ['a', 'b','c','d','e','f','g','h']

d = {
    'prices' : pd.Series(test_prices, index=x)
}

df  = pd.DataFrame(d)
df.plot()
