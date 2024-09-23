run_main = 1
print("Welcome to the exponent calculator!")
print("Your first number will be the intenger and the second will be your exponent.")
while run_main > 0:
  inte = input("Integer: ")
  exp = input("Exponent: ")
  print("Calculating...")
  ans = float(inte) ** float(exp)
  ("********************")
  print("Answer is: " + str(ans))
  ("********************")
  run = input("Would you like to run this again? 1 = yes, 2 = no. ")
  runn = int(run)
  if runn == 2:
    print("Exiting...")
    break
  print("Reloading...")
