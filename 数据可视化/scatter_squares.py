import matplotlib.pyplot as plt
x_value=[1,2,3,4,5]
y_value=[x**2 for x in x_value]
plt.style.use('classic')
fig,ax=plt.subplots()
ax.scatter(x_value,y_value,s=100,c=y_value,cmap=plt.cm.Blues)
plt.show()