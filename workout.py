print ('Weekly Workout Progression')
	
max_lift = {'Squat': 300, 'Bench': 265, 'Deadlift': 300, 'Militry': 155}
#These are the maxes you can actually lift placed near the top for easy change.

for value in max_lift:
	max_lift[value] *= 0.95
	# We calculated all sets using 95% of our actual max.
	
def week_1():
	for value in max_lift:
		print (value)
		print ('5 X %d' % (max_lift[value] * 0.65))
		print ('5 X %d' % (max_lift[value] * 0.75))
		print ('5 X %d' % (max_lift[value] * 0.85))
		#Week 1 is 3 sets of 5 at 65%, 75%, and 85% of revised max.
		
def week_2():
	for value in max_lift:
		print (value)
		print ('3 X %d' % (max_lift[value] * 0.70))
		print ('3 X %d' % (max_lift[value] * 0.80))
		print ('3 X %d' % (max_lift[value] * 0.90))
		#Week 2 is 3 sets of 3 at 70%, 80%, and 90% of revised max.
	
def week_3():
	for value in max_lift:
		print (value)
		print ('5 X %d' % (max_lift[value] * 0.75))
		print ('3 X %d' % (max_lift[value] * 0.85))
		print ('1 X %d' % (max_lift[value] * 0.95))
		#Week 3 is 3 sets of 5/3/1 at 75%, 85%, and 95% of revised max.
		
def week_4():
	for value in max_lift:
		print (value)
		print ('5 X %d' % (max_lift[value] * 0.60))
		print ('5 X %d' % (max_lift[value] * 0.60))
		print ('5 X %d' % (max_lift[value] * 0.60))
		#Week 4 is 3 sets of 5 deloaded back to 60% of revised max.

print ('Week 1 3X5')
print (week_1())
print ()
print ('Week 2 3X3')
print (week_2())
print ()
print ('Week 3 3X5/3/1')
print (week_3())
print ()
print ('Week 4 3X5')
print (week_4())
