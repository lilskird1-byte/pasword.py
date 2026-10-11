print(" My First Pasword Code Using Python.")
print()
correct_pasword= "ferd"
attempts=0
while attempts<3:
    pasword= str(input("What is the pasword:"))

    if pasword== correct_pasword:
        print("Access Granted!")
        break
    else:
        attempts +=1
        print("Access Denied!")
    if attempts==3:
        print("Program Locked!!")
        quit()