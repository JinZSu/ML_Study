import pandas as pd 
import numpy as np 

x = np.array([0,1,2,3,4])
y = np.array([0,2,3,8,17])

n = y.shape[0]

print x ,"x"
print y , "y"

xmean = np.mean(x)
ymean = np.mean(y)

print xmean, "xmean"
print ymean, "ymean"

sx= (np.sum((x-xmean)**2))/(x.shape[0] -1)
sy= (np.sum((y-ymean)**2))/(y.shape[0] -1)
syx= (np.sum((y-ymean)*(x-xmean)))/(y.shape[0] -1)

print sx ,"sx"
print sy ,"sy"
print syx, "syx"

w1 = syx/sx

w0 = ymean - w1 *xmean

yhat = w0 +w1*x


e=1-((np.sum((y-yhat)**2))/(np.sum((y-ymean)**2)))


print w1, w0 ,"w1 w0"
print e

RSS = np.sum((y-yhat)**2)
MSG = RSS/n
print RSS, MSG

TSS = np.sum((y-ymean)**2)
RSS = np.sum((y-yhat)**2)
ESS = np.sum((yhat-ymean)**2)

R2=1- RSS/TSS


print R2, "R2"

w0=0
w1=0
alpha = .1

for x in range(2):
	temp0 = w0 - (alpha/n)*(np.sum(w0+w1*x-y))
	temp1 = w1 - (alpha/n)*(np.sum((w0+w1*x-y)*x))
	w0=temp0
	w1=temp1
	print w0,w1, "w0", "w1", "Iteration :",x






