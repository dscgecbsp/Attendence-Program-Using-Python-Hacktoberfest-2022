num_of_class=100
num_of_class_attend=input("Please enter your attendance")
per=(num_of_class_attend/num_of_class)*100
if per<75:
  print("Not Allowed")
  con=input("If medical certificate press yes otherwise no")
  if con=="yes":
    print("Allowed")
  else:
    print("Not Allowed")
else:
  print("Allowed")
