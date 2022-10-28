num_of_class=100
num_of_class_attend=input("Please enter your attendance :")
per=(num_of_class_attend/num_of_class)*100
if per<75:
  print("Not Allowed")
  dec=input("If medical certificate enter 'YES' otherwise 'NO' :")
  if dec=="yes" or con=="YES":
    print("Allowed")
  else:
    print("Not Allowed")
else:
  print("Allowed")
  
