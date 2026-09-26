from time import sleep

program_state = True

while program_state:

  binary_numbers = "01"
  binary = 2
  index = 0
  storage = 0
  
  user_numbers = input("Insert a binary number: ")

  for check in user_numbers:

    if check in binary_numbers and user_numbers[0] != "0":
      pass

    else:
      
      print(str(index) + ".", check, "is not a valid input.")
      input("Press Enter to terminate.")
      quit()
    
    for i in reversed(range(0, 1, 1)):
      
      power = len(user_numbers) - index - 1
    
      if check == "1":
        storage += binary ** power
      
      elif check == "0":
        pass
      
    index += 1

  if storage > 0:
    
    print("Calculating binary code", user_numbers, "to number...")
    sleep(2)
    print("Result is:", str(storage))

    program = input("Would you like to continue? ").strip().lower()
    
    while program != "y" and program != "n":
      
      program = input("Would you like to continue? ")
      
    if program == "y" or program == "n":
      
      if program == "y":
        pass
        
      else:
        program_state = False
        
    else:
      program_state = False
  
  else:
    quit()
