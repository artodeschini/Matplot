import matplotlib.pyplot as plt
import numpy as np


col_count = 3
bar_width = .1

brasil_scores = (554, 536, 530)
canada_scores = (518, 523, 625)
france_scores = (299, 333, 444)
eua_scores = (666, 777, 888)

index = np.arange(col_count)

b1 = plt.bar(index + 0.1, brasil_scores, bar_width, label='Brasil', alpha=.4)
c1 = plt.bar(index + 0.2, canada_scores, bar_width, label='Canada', alpha=.4)
fr = plt.bar(index + 0.3, france_scores, bar_width, label='France', alpha=.4)
eua = plt.bar(index + 0.4, eua_scores, bar_width, label='United States', alpha=.4)

plt.grid(True)
plt.legend()
plt.xticks(index + .3 / 2)

plt.xlabel('Subjects')
plt.ylabel('Means score')
plt.title('Bar code Plot')

plt.show()
