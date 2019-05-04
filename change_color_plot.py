import matplotlib.pyplot as plt


years = [1800, 1860, 1900, 1950,
         1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000,
         2005, 2010, 2015, 2019]

pops = [1000, 1262, 2525, 2758, 3018, 3322, 3682,
        4961, 4440, 4853, 5310, 6127, 6520, 6930, 7349, 8000, 9000, 10000]


plt.ylabel("Years")
plt.xlabel('Population')
plt.plot(years, pops, color=(255/255, 100/255, 100/255))
plt.show()
