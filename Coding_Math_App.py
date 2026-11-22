from math import sqrt

while True:
    try:
        a = float(input("Enter the value of 'a'.\n >> "))
        b = float(input("\nEnter the value of 'b'.\n >> "))
        c = float(input("\nEnter the value of 'c'.\n >> "))
        
        x1 = ((-(b) + (sqrt(((b)**2)-(4*a*c)))) / 2*a)
        
        x2 = ((-(b) - (sqrt(((b)**2)-(4*a*c)))) / 2*a)
        
        print(f"\nThe value of x is {x1:.2f} or {x2:.2f}.")
    
    except ValueError:
        print("\nThis Quadratic Equation Has No Real Roots.")
    else:
#        print("Invalid Input. Please Enter Numerical Values Of Your Quadratic Problem.")
    finally:
        anthr_prbm = input("\nWould You like to solve another problem?\n >> ").title().strip()
        if anthr_prbm == "Yes":
            #print("Yes")
            continue
        elif anthr_prbm == "No":
            #print("No")
            break
        else:
            anthr_prbm = ("\nI did quite understand your responce.\n")
            print("Unknown")
    
print("\nThank you for using Coding Math")