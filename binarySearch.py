#imported the median function to get the median
from statistics import median
#used sleep to make the program look cool
from time import sleep
# the list that I used "l"
l = [4,7,9,20,60,100,90,15,30,12]
# the list that the program use
r = []
def findNumber(list,number):
	list.sort()
	# "t" is index of the midean
	t = int(len(list)/2)
	theMedian = int(median(list))
	print(theMedian)
	# this block is so  important without it the program will keep runing into recrusions and crash
	if number > list[-1] or number < list[0]:
		print("Sorry your number is'nt in the given list")
	elif theMedian > number:
		print("gotta go left")
		sleep(1)
		r = list[0:t]
		#used recrusion here
		findNumber(r,number)

	elif theMedian < number:
		print("gotta go right")
		sleep(1)
		r = list[t:]
		findNumber(r,number)
	#if there's only two numbres we can't use the same method as I think I need to test this
	elif len(list) == 2:
		print("almost there")
		sleep(1)
		if list[1] or list[0] == number:
			 	print("found your number")
		elif list[1] and list[0] != number:
			print("Sorry your number isn't here sorry")

	
	elif theMedian == number:
		print("your number were found in the given list")

	else:
		return "an error occured please be sure to contact the developer"
	
e = int(input())
findNumber(l,e)