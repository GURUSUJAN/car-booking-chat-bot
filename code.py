print("HOLA SOY SUJAN!")
print("YOUR FRIEND FOR THIS SESSION!")
num1=input("Name: ")
num2=int(input("Year of Birth: "))
num4=2022-num2
if (num4>18):
    num3=int(input("Moblie Number: "))
    print("Would you like to select a car:")
    print("Yes   No")
    num5=input(">")
    if num5.capitalize()=='Yes':
        print("Car Type: ")
        print("1.Sedan\n2.Suv\n3.LUXURY")
        num6=input(">")
        if num6.capitalize()=='Sedan':
            print("In Sedan which car")
            print("Suzuki    Tata")
            num7=input(">")
            if num7.capitalize()=='Suzuki':
                print("Swift   Dzire   Claz")
                num8=input(">")
                if num8.capitalize()=='Swift':
                    print("Can you Specify Your Licence Number: ")
                    num9=input(".")
                    num10=int(input("Duration: "))
                    num11=num10*100
                    print("Your fair is",num11)
                elif num8.capitalize()=='Dzire':
                    print("Can you Specify Your Licence Number: ")
                    num9 = input(".")
                    num10 = int(input("Duration: "))
                    num11 = num10 * 100
                    print("Your fair is", num11)
                elif num8.capitalize()=='Claz':
                    print("Can you Specify Your Licence Number: ")
                    num9 = input(".")
                    num10 = int(input("Duration: "))
                    num11 = num10 * 100
                    print("Your fair is", num11)
                else:
                    print("Sorry sir the car is not present for now")
            elif num7.capitalize()=='Tata':
                print("Tigor   Tiago   Altroz")
                num8=input(">")
                if num8.capitalize()=='Tigor':
                    print("Can you Specify Your Licence Number: ")
                    num9=input(".")
                    num10=int(input("Duration: "))
                    num11=num10*100
                    print("Your fair is",num11)
                if num8.capitalize()=='Tiago':
                    print("Can you Specify Your Licence Number: ")
                    num9=input(".")
                    num10=int(input("Duration: "))
                    num11=num10*100
                    print("Your fair is",num11)
                if num8.capitalize()=='Altroz':
                    print("Can you Specify Your Licence Number: ")
                    num9=input(".")
                    num10=int(input("Duration: "))
                    num11=num10*100
                    print("Your fair is",num11)
                else:
                    print("Sorry sir the car is not present for now")
        elif num6.capitalize()=='Suv':
            print("In Suv which car")
            print("Hundai " " Tata " " Kia ")
            num7=input(">")
            if num7.capitalize()=="Hundai":
                    print("Creta " "Venue " " Tuscon " " Alcazar")
                    num8 = input(">")
                    if num8.capitalize() == 'Creta':
                        print("Can you Specify Your Licence Number: ")
                        num9 = input(".")
                        num10 = int(input("Duration: "))
                        num11 = num10 * 150
                        print("Your fair is", num11)
                    elif num8.capitalize() == 'Venue':
                        print("Can you Specify Your Licence Number: ")
                        num9 = input(".")
                        num10 = int(input("Duration: "))
                        num11 = num10 * 150
                        print("Your fair is", num11)
                    elif num8.capitalize() == 'Tuscon':
                        print("Can you Specify Your Licence Number: ")
                        num9 = input(".")
                        num10 = int(input("Duration: "))
                        num11 = num10 * 150
                        print("Your fair is", num11)
                    elif num8.capitalize() == 'Alcazar':
                        print("Can you Specify Your Licence Number: ")
                        num9 = input(".")
                        num10 = int(input("Duration: "))
                        num11 = num10 * 150
                        print("Your fair is", num11)
                    else:
                        print("Sorry sir the car is not present for now")
            elif num7.capitalize()=='Tata':
                print("Punch " "Nexon " " Harrier " " Safari")
                num8 = input(">")
                if num8.capitalize() == 'Punch':
                    print("Can you Specify Your Licence Number: ")
                    num9 = input(".")
                    num10 = int(input("Duration: "))
                    num11 = num10 * 150
                    print("Your fair is", num11)
                elif num8.capitalize() == 'Nexon':
                    print("Can you Specify Your Licence Number: ")
                    num9 = input(".")
                    num10 = int(input("Duration: "))
                    num11 = num10 * 150
                    print("Your fair is", num11)
                elif num8.capitalize() == 'Safari':
                    print("Can you Specify Your Licence Number: ")
                    num9 = input(".")
                    num10 = int(input("Duration: "))
                    num11 = num10 * 150
                    print("Your fair is", num11)
                elif num8.capitalize() == 'Harrier':
                    print("Can you Specify Your Licence Number: ")
                    num9 = input(".")
                    num10 = int(input("Duration: "))
                    num11 = num10 * 150
                    print("Your fair is", num11)
                else:
                    print("Sorry sir the car is not present for now")
            elif num7.capitalize()=='Kia':
                print("Seltos " " Sonet " " Carnes")
                num8 = input(">")
                if num8.capitalize() == 'Seltos':
                    print("Can you Specify Your Licence Number: ")
                    num9 = input(".")
                    num10 = int(input("Duration: "))
                    num11 = num10 * 150
                    print("Your fair is", num11)
                elif num8.capitalize() == 'Sonet':
                    print("Can you Specify Your Licence Number: ")
                    num9 = input(".")
                    num10 = int(input("Duration: "))
                    num11 = num10 * 150
                    print("Your fair is", num11)
                elif num8.capitalize() == 'Carnes':
                    print("Can you Specify Your Licence Number: ")
                    num9 = input(".")
                    num10 = int(input("Duration: "))
                    num11 = num10 * 150
                    print("Your fair is", num11)
                else:
                    print("Sorry sir the car is not present for now")
        elif num6.upper()=='LUXURY':
            print("In LUXURY we have ")
            print("Mercedes")
            print("Can you Specify Your Licence Number: ")
            num9 = input(".")
            num10 = int(input("Duration: "))
            num11 = num10 * 240
            print("Your fair is", num11)
    elif num5.capitalize()=='No':
        num12=int(input("Count of total travelling people: "))
        num100=1      
        num95=6
        num99=2
        num98=3
        num97=4
        num96=5
        num94=7
        num93=8
        num92=0
        if num12==num98 or num97 :
            print("100 is the fair ",num1)
        elif num12==num96 or num12==num95 or num12==num94 or num12==num93:
            print("200 is the fair ",num1)    
        elif num12==num100 or num12==num99:
            print("350 is the fair ",num1)
        elif num12==num92:
            print("0 is the fair ",num1)
        else:
         print("We don't have heavy vehicals",num1)
else :
    print("Your under age ",num1)
