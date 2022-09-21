# lambda function
x = lambda a,b,c : a+b+c
print(x(1,2,3))

l1 = [12,34,5,6,8] 
l2 = []
for i in l1:
  t = lambda a : a+1
  l2.append(t(i))
print(l2)