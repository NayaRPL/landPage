x = [10,10,15,10,5]
y = [3,2.5,2,1.5,1]
total_x = 0
x1 = []
x2 = []
total_y = 0
y1 = []
y2 = []
xy = []

for c in range (len(x)):
    total_x+=x[c]
mean_x= total_x/len(x)

for z in range(len(x)):
    a = x[z]-mean_x
    x1.append(round(a,1))
    
print(total_x)
print(mean_x)
print (x1)