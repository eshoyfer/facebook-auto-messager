from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sched, time, timeit
import random
import getpass

while True:
	userEmail = raw_input("Please enter email.\n")
	userPass = getpass.getpass("Please enter password.\n")
	userTarget = raw_input("Please enter Facebook username of the user you wish to target.\n")
	userQuantity = input("Please enter how many messages you wish to send.\n")
	userTimeInterval = input("Please enter time (seconds) between each message. \n")
	userMessageType = raw_input("Please enter message type ['single' or 'multiple', without quotes]. \n")
	if userMessageType == 'single':
		userMessageQuantity = 1
		userMessage = raw_input("Please enter the message you wish to send. \n")
		userMessages = [userMessage]
		operation = True
	elif userMessageType == 'multiple':
		userMessageQuantity = input("How many distinct messages will you have?\n")
		userMessages = []
		for i in range(1, userMessageQuantity + 1):
			thisMessage = raw_input("Please enter message " + str(i) + " of " + str(userMessageQuantity) + ".\n")
			userMessages.append(thisMessage)
		operation = True
	else:
		print("Invalid input.")
		operation = False
		input("Press ENTER to restart the program.\n")


	if operation:
		print "Please confirm the following request information:\n"
		print "User email: " + userEmail + "\n"
		print "Target user: " + userTarget + "\n"
		print "Message count: " + str(userQuantity) + "\n"
		print "Time interval: " + str(userTimeInterval) + "\n"
		print "Messages: \n"
		print "    " + "Number of distinct messages: " + str(userMessageQuantity) + "\n"
		for i in range(userMessageQuantity):
			print "    " + str(i + 1) + " " + userMessages[i] + "\n"
		print "Estimated completion time: " + str(userQuantity * userTimeInterval) + " seconds OR " + str((userQuantity * userTimeInterval)/60.0) + " minutes."
		proceed = raw_input("Proceed? y/n\n")
		if proceed == 'y':
			operation = True
			break;
		else:
			print "Operation aborted.\n"
			input("Press ENTER to restart the program.\n")
			operation = False






if operation:
	print "Initializing..."
	browser = webdriver.Chrome()
	browser.maximize_window()

	print "Operation in progress."

	browser.get('http://www.facebook.com')
	emailElem = browser.find_element_by_id("email")
	emailElem.send_keys(userEmail)
	passElem = browser.find_element_by_id("pass")
	passElem.send_keys(userPass)
	passElem.send_keys(Keys.RETURN)
	userTargetUrl = "http://www.facebook.com/messages/" + userTarget
	browser.get(userTargetUrl)
	textAreaElem = browser.find_element_by_css_selector("div textarea.uiTextareaNoResize")
	for i in range(userQuantity):
		print "Sending message " + str(i + 1) + " of " + str(userQuantity) + "..."
		thisMessage = random.choice(userMessages)
		textAreaElem.send_keys(thisMessage)
		textAreaElem.send_keys(Keys.RETURN)
		time.sleep(userTimeInterval)
	print "Operation successful."
