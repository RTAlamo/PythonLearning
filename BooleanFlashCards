# This is creating the "super_test" function, which will contain the necessary variables, functions,
# and logic tests to allow the user to input their answer for a boolean question and then
# have that answer evaluated, counted as correct or incorrect, and then shown after each step.

def super_test():
# This is introduction text for dramatic effect.
	print "\nThis is a test of your boolean knowledge. Think you can hack it? Yeah, we'll find out.\n"

# This is establishing the correct score, or correct/incorrect answer counts. This starts at 0,
# and with each right or wrong answer the corresponding variable increases by 1.
	correct_count = 0
	incorrect_count = 0

# This function will return the text notifying the user that the answer was correct as well as
# displaying their current score.
	def correct_text():
		print "\n> That is CORRECT!\n"
		print ">> Your current score is: %d correct, %d incorrect.\n" % (correct_count, incorrect_count)
	
# This function will return the text notifying the user that the answer was correct as well as
# displaying their current score.	
	def incorrect_text():
		print "\n> That is INCORRECT.\n"
		print ">> Your current score is: %d correct, %d incorrect.\n" % (correct_count, incorrect_count)
	
# This function will return the text notifying the user of their final score. This will only be
# executed once, after the final question is answered and evaluated.
	def final_score():
			print "Your final score is...drumroll please...%d correct, %d incorrect.\n" % (correct_count, incorrect_count)
		
# Question 1
	answer = raw_input("\n1) What does 'not False' evaluate to? ")
	if answer == "True":
		correct_count += 1
		correct_text()
	else:
		incorrect_count += 1
		incorrect_text()
		
# Question 2
	answer = raw_input("2) What does 'not True' evaluate to? ")
	if answer == "False":
		correct_count += 1
		correct_text()
	else:
		incorrect_count += 1
		incorrect_text()
# Question 3
	answer = raw_input("3) What does 'True or False' evaluate to? ")
	if answer == "True":
		correct_count += 1
		correct_text()
	else:
		incorrect_count += 1
		incorrect_text()
# Question 4
	answer = raw_input("4) What does 'True or True' evaluate to? ")
	if answer == "True":
		correct_count += 1
		correct_text()
	else:
		incorrect_count += 1
		incorrect_text()
# Question 5
	answer = raw_input("5) What does 'False or True' evaluate to? ")
	if answer == "True":
		correct_count += 1
		correct_text()
	else:
		incorrect_count += 1
		incorrect_text()
		
# Question 6
	answer = raw_input("6) What does 'False or False' evaluate to? ")
	if answer == "False":
		correct_count += 1
		correct_text()
	else:
		incorrect_count += 1
		incorrect_text()

# Question 7
	answer = raw_input("7) What does 'not (True or False)' evaluate to? ")
	if answer == "False":
		correct_count += 1
		correct_text()
	else:
		incorrect_count += 1
		incorrect_text()
		
# Question 8
	answer = raw_input("8) What does 'not (True or True)' evaluate to? ")
	if answer == "False":
		correct_count += 1
		correct_text()
	else:
		incorrect_count += 1
		incorrect_text()
		
# Question 9
	answer = raw_input("9) What does 'not (False or True)' evaluate to? ")
	if answer == "False":
		correct_count += 1
		correct_text()
	else:
		incorrect_count += 1
		incorrect_text()
		
# Question 10
	answer = raw_input("10) What does 'not (False or False)' evaluate to? ")
	if answer == "True":
		correct_count += 1
		correct_text()
	else:
		incorrect_count += 1
		incorrect_text()
		
# Question 11
	answer = raw_input("11) What does 'not (True and False)' evaluate to? ")
	if answer == "True":
		correct_count += 1
		correct_text()
	else:
		incorrect_count += 1
		incorrect_text()
		
# Question 12
	answer = raw_input("12) What does 'not (True and True)' evaluate to? ")
	if answer == "False":
		correct_count += 1
		correct_text()
	else:
		incorrect_count += 1
		incorrect_text()
		
# Question 13
	answer = raw_input("13) What does 'not (False and True)' evaluate to? ")
	if answer == "True":
		correct_count += 1
		correct_text()
	else:
		incorrect_count += 1
		incorrect_text()
		
# Question 14
	answer = raw_input("14) What does 'not (False and False)' evaluate to? ")
	if answer == "True":
		correct_count += 1
		correct_text()
	else:
		incorrect_count += 1
		incorrect_text()
		
	final_score()
	
# And now that our program is written, now we call the "super_test()" function to run it!	
super_test()
