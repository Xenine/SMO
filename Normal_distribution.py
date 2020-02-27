"""Нормальное распределение системы массового обслуживания"""
import random
from matplotlib import pylab

number_of_times = 2000
number_of_trials = 1000
p1 = 0.997
p2 = 0.998
p3 = 0.998
p4 = 0.997
p5 = 0.999

list_of_times = []

for t in range(number_of_times):
	list_of_values = []
	for i in range(number_of_trials):
		time_of_work=0
		j = 1
		while j == 1: 
			state1=random.random()
			state2=random.random()
			state3=random.random()
			state4=random.random()
			state5=random.random()
			if (state1 < p1) and ((state2 < p2) or (state3 < p3)) and (state4 < p4) and (state5 < p5):
				time_of_work+=1
			else:
				j = 0	
		list_of_values.append(time_of_work)
	mean=pylab.mean(list_of_values)
	list_of_times.append(mean)

mean=pylab.mean(list_of_times)
std=pylab.std(list_of_times)
print ("Количество испытаний: ", number_of_times)
print ("Среднее: ", mean)
print ("Среднеквадратичное отклонение: ", std)

pylab.hist(list_of_times, 50, color='purple')
pylab.xlabel('Среднее количество часов работы для каждого испытания')
pylab.ylabel('Количество совпадений')
pylab.show()
