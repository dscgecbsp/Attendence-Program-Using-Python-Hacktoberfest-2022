num_of_class=100
num_of_class_attended=input("Please enter your attendance")
per=(num_of_class_attended/num_of_class)*100
if per<75:
  print("Entry Not Allowed")
  con=input("If medical certificate press yes otherwise no")
  if con=="yes":
    print(" Entry Allowed")
  else:
    print(" Entry Not Allowed")
else:
  print(" Entry Allowed")
