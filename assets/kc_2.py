import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# read in data with pandas and store as object
lures = pd.read_excel('LURES.xlsx', sheet_name = 'LURES')
lures
# object class
type(lures)
# Data classes in data frame
lures.dtypes
#scatterplot/ xy plot
#Matplotlib takes 1d objects
#numpy array (np.array) or pandas series (pd.series) are recommended
QTY = lures['QUANTITY']
SALES = lures ['SALES']
#one variable of pd.DataFrame = pd.Series
type(QTY)
# Scatterplot with the generic plot function
plt.plot(QTY, SALES, 'o')
# Dedicated command
plt.scatter(QTY, SALES)
#simple customization: Size, title and Labels
plt.figure(figsize = (12, 6))
plt.scatter(QTY, SALES, marker = 's', color = 'orange')
plt.xlabel('Quantity')
plt.ylabel('Sales')
plt.title('Scatterplot of Sales vs Quantity')
plt.show()