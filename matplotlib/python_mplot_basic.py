from matplotlib import pyplot as plt

# plt.xkcd()
# print(plt.style.available)
# ['seaborn-ticks', 'ggplot', 'dark_background', 'bmh', 'seaborn-poster', 'seaborn-notebook',
# 'fast', 'seaborn', 'classic', 'Solarize_Light2', 'seaborn-dark', 'seaborn-pastel',
# 'seaborn-muted', '_classic_test', 'seaborn-paper', 'seaborn-colorblind', 'seaborn-bright',
#  'seaborn-talk', 'seaborn-dark-palette', 'tableau-colorblind10', 'seaborn-darkgrid',
# 'seaborn-whitegrid', 'fivethirtyeight', 'grayscale', 'seaborn-white', 'seaborn-deep']
plt.style.use('ggplot')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# color='green', marker='o', linestyle='dashed',linewidth=2, markersize=12

plt.plot(ages_x, dev_y, color='#1EF2F9', marker='o',label="All Devs")


py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, color='#747B95', linestyle='dashed', marker='.',label="Python")

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x, js_dev_y, color='#333535' , marker='>',linestyle='dotted', linewidth=2, label="Java Scripts")


plt.xlabel("Ages")
plt.ylabel("Medain Salary (USD)")
plt.title("Median Salary Age wise (USD)")

plt.legend()
plt.tight_layout()
# plt.grid(color='k', linestyle='-.', linewidth=1)
# plt.grid(True)
plt.savefig('plot.png')
plt.show()