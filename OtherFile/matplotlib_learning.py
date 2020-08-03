import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family'] = 'SimHei'  # 黑体
matplotlib.rcParams['font.size'] = 20  # 黑体
a = np.arange(5)
plt.plot(a, 2*a, 'go-', a, 3*a, 'b*')
plt.axis([-1, 5, 0, 6])
plt.xlabel('测试x', fontsize=10)
plt.title('标题$\\frac{2}{x}$')
plt.text(2, 1, '$y=x$', fontsize=8)
plt.annotate(r'$\mu = 300$', xy=(3, 1), xytext=(4, 2),
             arrowprops=dict(facecolor='b', shrink=0.1))
plt.show()
