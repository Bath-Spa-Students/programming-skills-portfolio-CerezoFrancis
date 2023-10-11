#Practice 4- Question 4
a = float(input('left side: '))  
b = float(input('right side: '))  
c = float(input('buttom side: '))  
  
# calculate the semi-perimeter  
s = (a + b + c) / 2  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)   
