# Python program to compute 95% confidence interval, 
# normal distribution, t = ?
# v1 so far it returns mean and median

# step 1 get values

N = raw_input("Number of values:")
N = int(N)
print N

values = [] # declare list variable to hold the input values

# loop to have user enter all the values
for i in range(0, N):
	print "Enter value %d :" % (i+1),
	temp = raw_input()
	values.append(int(temp))

# sort and print sorted values
values.sort()
print values

# arithmetric mean
mean = 0
for item in values:
	mean = mean + item

mean = float(mean) / len(values)
print "The arithmetric mean is: %f" % mean

# median
median = 0
if len(values) % 2 == 0: # even number of values, average the middle values
	median = (float(values[len(values) / 2]) + values[(len(values) / 2) - 1]) / 2
	print "The median is: %f" % median 
else: # odd number of values, return the middle value
	median = values[len(values) / 2]
	print "The median is: %d" % median 

