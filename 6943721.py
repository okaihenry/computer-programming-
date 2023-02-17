"""
M = w(-6x^2 + 6Lx - L^2)/12

V = w(L/2 - x)

where M = bending moment
V = shear force
L = the span of the beam
x = a specified distance
w = Load intensity
"""

#Question a
#Print the bending moment and shear force at the ends (that is x = 0 and x = L)

#Span of the beam 
L = 12                                  #in meters

#Load intensity
w = 10                                  #in kN/m


#At x = 0
x = 0

#Formula for the Bending Moment
M = w*(-6*x**2 + 6*L*x  - L**2)/12

#Formula for the Shear Force
V = w*(L/2 - x)
print("The bending moment at x =", x, "is ", M,"kNm")
print("The shear force at x =", x, "is ", V,"kN" )
print()


#At x = L
x = L

#Formula for the Bending Moment
M = w*(-6*x**2 + 6*L*x  - L**2)/12

#Formula for the Shear Force
V = w*(L/2 - x)
print("The bending moment at x =", x, "is", M,"kNm")
print("The shear force at x =", x, "is", V,"kN")
print()


#Question b 
#Write an expression to estimate the distance at which the bending moment will be zero

#Using the method of completing square x = L*sqrt(3)/6   + L/2 or -L*sqrt(3)/6 + L/2

# Importing the sqrt function from the math module
from math import sqrt 
x1 = (L*sqrt(3))/6 + L/2
x2 = (-L*sqrt(3))/6 + L/2
print("The distance at which the Bending Moment will be zero is",str(x1)+"m", "or",str(x2)+"m")
print()



#Question c
#Also determine the point at which the bending moment will be zero

#The shear force will be zero at x = L/2
distance = L/2 
print("The shear force occurs at the point at which x =", str(distance)+" m")
print()



#Question d
"""
Use Numpy array to discretize a span of L = 12m, at a step of 10mm. Using the 
initialized variable, evaluate the bending moment at each step in the array
"""
# Importing the numpy library
import numpy as np

#NOTE : 10mm is equivalent to 0.01m so the step would be 0.01

#Using the arange function from numpy to generate an array of steps of 0.01 on the span length
span_steps = np.arange(0, L + 0.01, 0.01)

#Bending Moment at each step
BM_each_step = w*(-6*span_steps**2 + 6*L*span_steps  - L**2)/12

print("Bending Moment at each step: ",BM_each_step,"in kNm")
print()




#Question e 

#Also calculate the shear force for each step, along the span
Shear_Force_each_step = w*(L/2 - span_steps)

print("Shear Force at each step :",Shear_Force_each_step,"in kN")
print()
abs_BM = np.abs(BM_each_step)

#Question f 
#Find points along L at which the absolute values of the bending moment array in d is minimum

#Absolute values of the bending moment in (d)

#Points along L at which the absolute values of the bending moment is minimum
L_BM_min = span_steps[abs_BM == abs_BM.min()]
print(L_BM_min[0], "in metres")
print()



#Question g 
# Determine the relative errors between the estimated points of contra-flexure in (b) and (f)

"""
Relative Error = (|Expected - Actual|/ Actual Value) * 100%
Expected = Distances(x1, x2) at which the Bending Moment will be minimum in (b) 
Actual Value = The value we had in question (f) i.e. Point along L at which the BM is minimum in (f)
"""

#Converting the distances to an array
Expected = np.array([x1, x2])
Actual = L_BM_min

#Relative errors in percent
Relative_Errors = ((np.abs(Expected - Actual))/Actual) * 100
print("Relative Errors :",Relative_Errors, "in percent(%)")
print()



#Question (h)
#Find the points at which the maximum and minimum bending moment occur, using the discretized ponts 

#Points along the discretized points at which the maximum bending moment occur 
print("Points along wich the bending moment is maximum :",span_steps[ BM_each_step == BM_each_step.max()][0],"in metres")

#Points along the discretized points at which the minimum bending moment occur 
print("Points along wich the bending moment is minimum :",span_steps[ BM_each_step == BM_each_step.min()][0],"in metres")
 
#github link https://github.com/okaihenry/computer-programming-
