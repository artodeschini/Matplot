import matplotlib.pyplot as plt


years = [1800, 1860, 1900, 1950,
         1955, 1960, 1965, 1970,
         1975, 1980, 1985, 1990,
         2005, 2010, 2015, 2019]

pops = [1, 1.5, 2, 2.7,
        3, 3.17, 3.5, 4,
        4.440, 5, 6, 7,
        7.5, 7.2, 8, 10]

deaths = [1.2, 1.7, 1.8, 2.2,
          2.5, 2.7, 2.9, 3,
          3.1, 3.3, 3.5, 3.8,
          4.0, 4.3, 4.7, 5]

plt.ylabel("Population in Billions")
plt.xlabel('Population growth by years')

plt.title('Population Growth')
plt.plot(years, pops, color=(255/255, 100/255, 100/255))
plt.plot(years, deaths, color=(.6, .6, 1))
plt.show()

