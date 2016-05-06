#Coffee.py written by Eric Cain, Teacher Candidate at UOIT
#May 5th, 2016


#WakingUp is a string that checks if the user is just waking up
WakingUp = input("Are you just waking up?:")

#If the user is waking up, then they need a coffee
if str.lower(WakingUp) == 'yes':
    wakingUp = True

else:
    wakingUp = False
    time = int(input("Enter the military time :"))

#If they are not just waking up, their need for coffee depends on the time of day


if (wakingUp == True or time < 6):
    print("\nYou need a coffee")

elif (time > 6 and time < 18):
    print("\nYou should probably have some coffee")

else:
    print("\nMaybe you don't need that ish")
    
