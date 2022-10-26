num_of_class=100
num_of_class_attend=int(input("Please enter your attendance: "))
per=(num_of_class_attend/num_of_class)*100
if (per<75):
  print("Not Allowed")
  proof=input("If medical certificate press yes otherwise no: ")
  if (proof=="yes"):
    print("Allowed")
  else:
    print("Not Allowed")
else:
  print("Allowed")
