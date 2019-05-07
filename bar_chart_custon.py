import matplotlib.pyplot as plt
import numpy as np


def create_labels(data):
    for item in data:
        height = item.get_height()
        plt.text(
            item.get_x() + item.get_width() / 2.,
            height * 1.05, '%d' % int(height),
            ha='center', va='bottom')


col_count = 3
bar_width = .2

brasil_scores = (554, 536, 530)
canada_scores = (518, 523, 625)
france_scores = (299, 333, 444)
eua_scores = (666, 777, 888)

index = np.arange(col_count)

b1 = plt.bar(index, brasil_scores, bar_width, label='Brasil', alpha=.4)
c1 = plt.bar(index + 0.2, canada_scores, bar_width, label='Canada', alpha=.4)
fr = plt.bar(index + 0.4, france_scores, bar_width, label='France', alpha=.4)
eua = plt.bar(index + 0.6, eua_scores, bar_width, label='United States', alpha=.4)

plt.grid(True)
plt.legend()
plt.xticks(index + .3 / 2, ('python', 'java', 'c#'))

plt.xlabel('Subjects')
plt.ylabel('Means score')
plt.title('Bar code Plot')

create_labels(b1)
create_labels(c1)
create_labels(fr)
create_labels(eua)

plt.show()


