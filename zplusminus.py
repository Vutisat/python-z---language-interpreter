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
	with open("prog3.zpm") as f:
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
	for i in range(0, len(commands)):
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




	print(values)
	return

zPlusMinus();

'''
	
	public zPlusMinus() {
	

	/**
	 * This method print out the values for each variable by alphabetical order
	 */
	private void printValues() {
		Map<String, Integer> map = new TreeMap<String, Integer>(values);
		Set set2 = map.entrySet();
		Iterator iterator2 = set2.iterator();
		while (iterator2.hasNext()) {
			Map.Entry me2 = (Map.Entry) iterator2.next();
			System.out.print(me2.getKey() + ": ");
			System.out.println(me2.getValue());
		}
	}

	// This method allow to test the code to be interpreted for the correct
	// output
	private void test() {
		int a = 0;
		int b = 0;
		a = 1;
		for (int i = 0; i < 20; i++) {
			b += a;
			a *= 2;
		}
		a += 1000;

		for (int j = 0; j < 20; j++) {
			b -= a;
			a += 2;
		}
		System.out.println("final a = " + a);
		System.out.println("final b = " + b);

	}

	}

	private void interpretCode() {
		values = new HashMap<String, Integer>();

		for (int i = 0; i < commands.size(); i++) {

			

			// This following part of the code takes care of assignments

			

				

			

			// Handling For Loops here////
			if (commands.get(i).equals("FOR")) {
				int iterations = Integer.parseInt(commands.get(i + 1));

				for (int j = 0; j < iterations; j++) {

					if ((!values.containsKey(commands.get(i + 2)) && commands
							.get(i - 2).equals("FOR"))
							|| (!values.containsKey(commands.get(i + 2)) && commands
									.get(i - 6).equals("FOR"))) {

						if (commands.get(i + 1).equals("=")) {
							values.put(commands.get(i),
									Integer.parseInt(commands.get(i + 2)));
						}

						if (commands.get(i + 1).equals("+=")) {
							values.put(
									commands.get(i),
									values.get(commands.get(i))
											+ Integer.parseInt(commands
													.get(i + 2)));
						}

						if (commands.get(i + 1).equals("-=")) {
							values.put(
									commands.get(i),
									values.get(commands.get(i))
											- Integer.parseInt(commands
													.get(i + 2)));
						}

						if (commands.get(i + 1).equals("*=")) {
							values.put(
									commands.get(i),
									values.get(commands.get(i))
											* Integer.parseInt(commands
													.get(i + 2)));
						}
					}

					// /////////////////Assign from a variable//////////

					if ((values.containsKey(commands.get(i + 2)) && commands
							.get(i - 2).equals("FOR"))
							|| (values.containsKey(commands.get(i + 2)) && commands
									.get(i - 6).equals("FOR"))) {

						if (commands.get(i + 1).equals("=")) {
							values.put(commands.get(i),
									values.get(commands.get(i + 2)));
						}

						if (commands.get(i + 1).equals("+=")) {
							values.put(
									commands.get(i),
									values.get(commands.get(i))
											+ values.get(commands.get(i + 2)));
						}

						if (commands.get(i + 1).equals("-=")) {
							values.put(
									commands.get(i),
									values.get(commands.get(i))
											- values.get(commands.get(i + 2)));
						}

						if (commands.get(i + 1).equals("*=")) {
							values.put(
									commands.get(i),
									values.get(commands.get(i))
											* values.get(commands.get(i + 2)));
						}
					}

					if (!commands.get(i).equals("ENDFOR")) {
						j--;
					}

					if (commands.get(i).equals("ENDFOR")) {
						i = i - 9;
					}

					i++;
				}
			}

		}

	}
}
'''