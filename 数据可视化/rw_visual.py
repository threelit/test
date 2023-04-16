
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw=RandomWalk()
    rw.fill_walk()
    plt.style.use("classic")
    fig,ax=plt.subplots(figsize=(15,9))
    point_number=range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c=point_number,cmap=plt.cm.Blues,s=10,edgecolors='none')
    ax.scatter(0,0,s=100,c='red',edgecolor='none')
    ax.scatter(rw.x_values[-1],rw.y_values[-1],s=100,c='blue',edgecolor='none')
    ax.get_xaxis().set_visible(False)#隐藏坐标轴
    ax.get_yaxis().set_visible(False)

    plt.show()

    keeprunning=input('y/n')
    if keeprunning=='y':
        print("go on")
    else:
        break
