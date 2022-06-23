string = input("Please enter your input: ")

if len(string) <= 7:
      print("Odd Index number characters: ", string[::2])
else: 
      print("Even Index number characters: ", string[1::2])
