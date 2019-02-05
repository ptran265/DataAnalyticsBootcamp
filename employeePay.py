import sys

id = sys.argv[1]
name = sys.argv[2]
rate = int(sys.argv[3])
hours = int(sys.argv[4])

if hours <=40:
	salary = hours*rate
else:
	overtime = hours-40
	salary = (40*rate)+(overtime*rate*1.5)

print(name,': ', salary)