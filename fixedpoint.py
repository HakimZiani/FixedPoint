from pylab import plot,show
from numpy import linspace,sqrt,exp
from numpy.linalg import norm
from random import random
print(random(1,1000))

def fixedp(f,x0,tol=10e-5,maxiter=100):
 """ Fixed point algorithm """
 e = 1
 itr = 0
 xp = []
 while(e > tol and itr < maxiter):
  x = f(x0)      # fixed point equation
  e = norm(x0-x) # error at the current step
  x0 = x
  xp.append(x0)  # save the solution of the current step
  itr = itr + 1
 return x,xp



f = lambda x : sqrt(x)

x_start = .5
xf,xp = fixedp(f,x_start)

x = linspace(0,2,100)
y = f(x)
plot(x,y,xp,f(xp),'bo',
     x_start,f(x_start),'ro',xf,f(xf),'go',x,x,'k',x,exp(x),'bo ')
show()
