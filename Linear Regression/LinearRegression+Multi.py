# ML_Homework1
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
# %matplotlib inline

def fit_linear(x,y):
    """
    Given vectors of data points (x,y), performs a fit for the linear model:
       yhat = w0 + w1*x, 
    The function returns w0, w1 and rsq, where rsq is the coefficient of determination.
    """
    # TODO complete the following code
    # w1 = ...
    # w0 = ...
    # rsq = ...
    xbar=np.mean(x)
    ybar=np.mean(y)
    sx=np.sum((x-xbar)**2)
    syx=np.sum((y-ybar)*(x-xbar))
    w1=syx/sx
    w0=ybar-w1*xbar
    yhat= w0 + w1*x
    rsq=1-((np.sum((y-yhat)**2))/(np.sum((y-ybar)**2)))
    return w0, w1, rsq


def compute_cost(x, y, w0, w1, N):
	#Write your code in place of None. Cost can be calculated using a single line of code
	cost=(np.sum((y-(w0 + (w1*x)))**2))/(2*N)
	return cost


def gradient_descent(x, y, learning_rate, w0, w1, N, num_iters):
    # In place of None, write the updated value of w0 in temp0 and of w1 in temp1
    for i in range(num_iters):
        temp0 = w0-((learning_rate/N)*(np.sum(w0+w1*x-y)))
        temp1 = w1-((learning_rate/N)*(np.sum((w0+w1*x-y)*x)))
        w0 =temp0
        w1= temp1
        if(i%100==0):
            # In place of None, call the cost you just coded above
            cost= (np.sum((y-(w0 + (w1*x)))**2))/(2*N)
            print("Cost")
            print(cost)
            print("w's")
            print(w0)
            print(w1) 
            
    return w0,w1 

def predict(x, w0, w1):
    predicted_y = w0 + (w1*x)
    return predicted_y

if __name__="__main__":


	# PART 1 --------------------------------------------------------------------------------------------------------
	names =[
	    'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 
	    'AGE',  'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'PRICE'
	]

	df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data',sep='\s+',names=names)
	print df.head(6)

	num_samples = df.shape[0]
	print "num_samples",num_samples

	num_attributes = df.shape[1]
	print "num_attributes",num_attributes

	# y=df["PRICE"].values
	y = np.array(df['PRICE'])
	print y

	# xxyy=df["PRICE"].values.mean().round(2)
	xxyy=np.mean(y).round(2)
	# xy=df["PRICE"].mean().round(2)
	xy=np.mean(y>40).round(2)

	print "The mean house price is ",xxyy," thousands of dollars."
	print "Only",xy,"percent are above $40k."

	x = np.array(df['RM'])
	print x

	# plt.plot(x,y,'o')
	# plt.xlabel('Number of Rooms',fontsize=16)
	# plt.ylabel('Price (In Thousands)',fontsize=16)
	# plt.grid(True)

	print(fit_linear(x,y))

	xp = np.array([4,9])
	w0,w1,rsq = fit_linear(x,y)
	yp = w0 + w1*xp

	plt.plot(x,y,'o')
	plt.plot(xp,yp,'-',linewidth=3)
	plt.xlabel('Number of Rooms',fontsize=16)
	plt.ylabel('Price (In Thousands)',fontsize=16)
	plt.grid(True)


	for i in df.columns[:-1]:
	    x = np.array(df[i])
	    rss = fit_linear(x, y)[2].round(3)
	    print i, rss

	# PART 2 --------------------------------------------------------------------------------------------------------
	import numpy as np
	import pandas as pd
	import matplotlib
	from matplotlib import pyplot as plt
	%matplotlib inline
	# After completing the code in this code cell, run this code cell before moving further.
	names =[
	    'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 
	    'AGE',  'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'PRICE'
	]

	# TODO
	df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data', sep='\s+', names=names)

	df1 = df.filter(["PRICE","RM"],axis=1)
	df2 = df1.dropna()
	# Check the shape of df2. It should be (506,2)
	print df2.shape

	x = np.array(df2["RM"])
	y = np.array(df2["PRICE"])
	# Check the shape of x and y vectors.
	print x.shape
	print y.shape

	x = x.reshape(x.shape[0],1)
	y = y.reshape(y.shape[0],1)

	print x.shape
	print y.shape

	N = x.shape[0]
	print N


	cost_verify= compute_cost(x, y, 0, 0, N)
	print(cost_verify)

	g=gradient_descent(x, y, 0.04, 0, 0, N, 10000)
	print(g[0])

	y_predict = predict(x[6],w0,w1)
	print(y_predict)

	#Write the code below
	a = np.array([1]*N)
	a = a.reshape(a.shape[0],1)
	X = np.hstack((a,x))
	print X.shape
	print X

	print("w0 is " + str(w0))
	print("w1 is " + str(w1))
