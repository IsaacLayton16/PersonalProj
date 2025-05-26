#This programs main focus is to show principle knowledge of the python progrmaming language.
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("https://github.com/IsaacLayton16")
print("Program built by Isaac Layton")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


userName = input("Hello, what is your name? " )
userAge = int(input("Thank you, " + userName + ". Please enter your age: "))

try:
    userWeightLb = int(input("Please enter your weight in pounds: "))
except:
    print("Please ensure weight is entered as an integer (e.g, 165).")
    exit()

try:
    userHeightInch = int(input("Please enter your height in inches: "))
except:
    print("Please ensure height is entered as an integer (e.g, 67).")
    exit()

print()

try:
    finalBMI = round((703 * userWeightLb)/(userHeightInch*userHeightInch), 2)
    print("Your BMI is: " + str(finalBMI) + ", here is what that means:")
except:
    print("An unexpected error occured when calculating BMI. Ensure age and height are entered as integers (e.g, 150).")
    exit()


if(finalBMI< 18.5):
    print("According to the CDC, a BMI of " + str(finalBMI) + " is a sign of being underweight.")
    print("Consider consulting with your doctor for nutrition advice.")
elif(finalBMI< 24.91):
        print("According to the CDC, a BMI of " + str(finalBMI) + " is a sign of being a normal weight.")
        print("You are maintaining a healthy balance.")
elif(finalBMI< 29.91):
        print("According to the CDC, a BMI of " + str(finalBMI) + " is a sign of being overweight.")
        print("Consider consulting with your doctor for nutrition advice.")
elif(finalBMI< 34.91):
        print("According to the CDC, a BMI of " + str(finalBMI) + " is a sign of being in obesity class 1.")
        print("Consult a medical provider.")
elif(finalBMI< 39.91):
        print("According to the CDC, a BMI of " + str(finalBMI) + " is a sign of being in obesity class 2 or above.")
        print("Medical guidance is very recommended.")





