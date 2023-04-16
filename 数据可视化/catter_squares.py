import matplotlib.pyplot as plt

plt.style.use('classic')
fig,ax=plt.subplots()
ax.set_title('平方数',fontsize=24)
ax.set_xlabel('值',fontsize=14)
ax.set_ylabel('值的平方',fontsize=14)
ax.tick_params(axis='both',which='major',labelsize=14)
ax.scatter(2,4)
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.show()