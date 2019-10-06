import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
plt.style.use('ggplot')

slices = [59219, 55466, 47544, 36443, 35917,]
label = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode =[0,0,0.1,0,0]

plt.pie(slices,labels=label,explode=explode,  autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black', 'linewidth': 2},
        shadow=True, radius=1)


# plt.legend()
plt.tight_layout()
# plt.grid(color='k', linestyle='-.', linewidth=1)
# plt.grid(True)
plt.savefig('pie.png')
plt.show()