'''
 @author Pob Vutisalchavakul 2/5/2015
 
''' 
commands = list()
values = {}

def zPlusMinus():
	readFile()
	interpretCode()
	printValues()
	return

def printValues():
	return

def readFile():
	with open("prog6.zpm") as f:
		content = f.readlines()

	for i in content:
		commands.extend(i.split());

	commands.extend("AlmostEnd")
	commands.extend("Ending")
	
#	This will print out all the commands
#	for i in commands:
#		print(i)
	return


def interpretCode():
	i = 0
	while i < len(commands):
		# This code takes care of declarations
		if commands[i] == "DEF":
			values[commands[i+1]] = 0

		#////////////////////Assign from a number//////////////
		if ((commands[i] in values and commands[i - 1] == ";" and not commands[i + 2] in values	and not commands[i + 4] == "ENDFOR") or (commands[i] in values and not commands[i + 2] in values and not commands[i + 4]  == "ENDFOR" and commands[i - 1] == "ENDFOR")):
			
			if commands[i + 1] == "=":
					values[commands[i]] = int(commands[i + 2]);

			if commands[i + 1] == "+=":
					values[commands[i]] = int(values[commands[i]]) + int(commands[i + 2]);
				
			if commands[i + 1] == "-=":
					values[commands[i]] = int(values[commands[i]]) - int(commands[i + 2]);

			if commands[i + 1] == "*=":
					values[commands[i]] = int(values[commands[i]]) * int(commands[i + 2]);

		#////////////////////Assign from a variable//////////
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
				
				if (not(commands[i + 2] in values) and commands[i - 2] =="FOR") or (not (commands[i + 2] in values) and commands[i - 6] == "FOR"):
					
					if commands[i + 1] == "=":
						values[commands[i]] = int(commands[i + 2])

					if commands[i + 1] == "+=":
						values[commands[i]] = int(values[commands[i]]) + int(commands[i + 2])
				
					if commands[i + 1] == "-=":
						values[commands[i]] = int(values[commands[i]]) - int(commands[i + 2])

					if commands[i + 1] == "*=":
						values[commands[i]] = int(values[commands[i]]) * int(commands[i + 2])
						

				#// /////////////////Assign from a variable//////////

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




	print(values)
	return

zPlusMinus();