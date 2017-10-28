# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False

def parrot_trouble(talking, hour):
	if(hour>=0 and hour<=23):
		print(hour)
		if(hour>7 and hour<20):
			#if parrot speaks in valid hour of the day
			if(talking == True):
				
				return True
			else:
				return False
		else:
			
			if(talking == False):
				return True
			else:
				return False
	else:
		print("This is not a valid hour of the day")
		
talking = True
hour = 24

print(parrot_trouble(talking,hour))