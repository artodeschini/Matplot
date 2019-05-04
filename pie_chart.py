import matplotlib.pyplot as plt


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct


labels = 'Python', 'Java', 'C++', 'PHP', 'Ruby', 'Scala'
sizes = [33, 52, 12, 17, 62, 48]
separated = (0.2, 0, 0, 0, 0, 0)

plt.pie(sizes, labels=labels, autopct=make_autopct(sizes), explode=separated)

plt.show()


