#number of classes held:
total_classes = int(input ("How many clases have been held in the year thus far? "));

#number of classes attended:
attended_classes = int(input("How many classes have you attended? "));

#percentage of classes
percentage_attendence = ((attended_classes/total_classes)*100);

if percentage_attendence < 75:
    medic = input("Do you have a medical cause? (Y/N or y/n only)");
    if medic == "y" or "Y" or "yes" or "ye":
        print ("You are free to take part in the exam");
    else:
        print ("You can not take part in the exam");
else:
    print ("You are free to take part in the exam");
