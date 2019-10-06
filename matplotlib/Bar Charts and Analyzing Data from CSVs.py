import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('ggplot')

Data = pd.read_csv('data.csv')

id = Data['Responder_id']
lang_response= Data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_response:
    language_counter.update(response.split(';'))

id = []
lang_response = []

for item in language_counter.most_common(15):
    id.append(item[0])
    lang_response.append(item[1])

id.reverse()
lang_response.reverse()

plt.barh(id,lang_response)

# plt.ylabel("Commodity")
plt.xlabel("No of people using")
plt.title("Most Used Language")

plt.legend()
plt.tight_layout()
# plt.grid(color='k', linestyle='-.', linewidth=1)
# plt.grid(True)
# plt.savefig('plot.png')
plt.show()