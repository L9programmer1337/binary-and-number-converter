binary = 2
storage = 0
detector = "0123456789"
number_collector = ""
zero_detector = True

binary_converter = input("Number to Binary Code: ")

if binary_converter == '':
  quit("Invalid Input: No input.")

elif binary_converter == "0":
  quit("Invalid Input: Cannot calculate with 0.")

else:
  pass

for integer in binary_converter:

  if integer in detector:
    continue
    
  else:
    quit("Invalid Input: Negative Number/Non-Integer.")

for i in reversed(range(0, int(binary_converter), 1)):
  
  i = binary ** i
  
  if storage < int(binary_converter) and int(binary_converter) >= i:
    
    if storage + i > int(binary_converter):
      number_collector += "0"
      
    else:
      storage += i
      number_collector += "1"

  else:
    number_collector += "0"

if storage == int(binary_converter):
  
  for j in number_collector:
    
    if j == "0" and zero_detector:
      print(end = "")
      
    else:
      zero_detector = False
      print(j, end = "")
      
  print("\nSolved", str(storage) + "!")
  input("Press Enter to terminate.")
  quit()
