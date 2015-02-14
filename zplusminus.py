'''
 @author Pob Vutisalchavakul 2/5/2015
 This is my first actual program written in Python.
 It interprets the language z+- given a file input.
 The coding can definitely be reduce but the logic currently work, will polish if I have time.

 Please change the file input in line 32 of the program.
''' 
#Declaring Global Variables
commands = list()
values = {}

def zPlusMinus():
	readFile()
	interpretCode()
	printValues()
	return

#This method sorts the variables alphabetically then print out their values at the end.
def printValues():

	from collections import Counter
	c = Counter(values)
	
	for k,v in sorted(c.items()):
		print('{}: {}'.format(k,v))
	
	return

#This method reads from a file and split each meaningful part into an array
def readFile():
	with open("prog4.zpm") as f:
		content = f.readlines()

	for i in content:
		commands.extend(i.split());

	commands.extend("AlmostEnd")
	commands.extend("Ending")
	
	return

#This part interpret and do the work of the code. A dictionary "values" is used to store all variables
def interpretCode():
	i = 0
	while i < len(commands):
		# This code takes care of declarations
		if commands[i] == "DEF":
			values[commands[i+1]] = 0

		#Assigning from number and arithmetric
		if ((commands[i] in values and commands[i - 1] == ";" and not commands[i + 2] in values	and not commands[i + 4] == "ENDFOR") or (commands[i] in values and not commands[i + 2] in values and not commands[i + 4]  == "ENDFOR" and commands[i - 1] == "ENDFOR")):
			
			if commands[i + 1] == "=":
					values[commands[i]] = int(commands[i + 2]);

			if commands[i + 1] == "+=":
					values[commands[i]] = int(values[commands[i]]) + int(commands[i + 2]);
				
			if commands[i + 1] == "-=":
					values[commands[i]] = int(values[commands[i]]) - int(commands[i + 2]);

			if commands[i + 1] == "*=":
					values[commands[i]] = int(values[commands[i]]) * int(commands[i + 2]);

		#Assigning from variable
		if ((commands[i] in values and commands[i-1] == ";" and commands[i+2] in values and not(commands[i+4] == "ENDFOR"))	or (commands[i] in values and commands[i+2] in values and not(commands[i+4] == "ENDFOR" and commands[i - 1] == "ENDFOR"))):

			if commands[i + 1] == "=":
				values[commands[i]] = values[commands[i + 2]]

			if commands[i + 1] == "+=":
				values[commands[i]] = (values[commands[i]] + values[commands[i + 2]])
				
			if commands[i + 1] == "-=":
				values[commands[i]] = (values[commands[i]] - values[commands[i + 2]])

			if commands[i + 1] == "*=":
				values[commands[i]] = (values[commands[i]] * values[commands[i + 2]])


		if commands[i] == "FOR":
			iterations = int(commands[i + 1])
			j = 0

			while j < iterations:
				
				#For loop with arithmetric
				if (not(commands[i + 2] in values) and commands[i - 2] =="FOR") or (not (commands[i + 2] in values) and commands[i - 6] == "FOR"):
					
					if commands[i + 1] == "=":
						values[commands[i]] = int(commands[i + 2])

					if commands[i + 1] == "+=":
						values[commands[i]] = int(values[commands[i]]) + int(commands[i + 2])
				
					if commands[i + 1] == "-=":
						values[commands[i]] = int(values[commands[i]]) - int(commands[i + 2])

					if commands[i + 1] == "*=":
						values[commands[i]] = int(values[commands[i]]) * int(commands[i + 2])

				#For loop with assignment
				if (commands[i + 2] in values and commands[i - 2] == "FOR") or (commands[i + 2] in values and commands[i - 6] == "FOR"):

					if commands[i + 1] == "=":
						values[commands[i]] = values[commands[i + 2]]

					if commands[i + 1] == "+=":
						values[commands[i]] = (values[commands[i]] + values[commands[i + 2]])
				
					if commands[i + 1] == "-=":
						values[commands[i]] = (values[commands[i]] - values[commands[i + 2]])

					if commands[i + 1] == "*=":
						values[commands[i]] = (values[commands[i]] * values[commands[i + 2]])

				if not commands[i] == "ENDFOR":
					j -= 1
					
				if commands[i] == "ENDFOR":
					i = i - 9

				j += 1
				i += 1
		i += 1
	return

zPlusMinus();