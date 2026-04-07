

#### TASK 1 - ENTER YOUR TEAM NAME AND NUMBER
team_name = ""

#### TASK 2 - Clone the empty gitHub repo in your local computer (Member #1)

#### TASK 3 - Add this code to your gitHub repo - follow the best practices of add --> commit --> pull --> push

def addition(number1, number2):
  print("We are adding " + str(number1) + " and " + str(number2))
  return number1 + number2


def calculator():
  print("Calculator by team =  " + team_name)
  print("Choose the operation you want to perform: ")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Integer Division")
  print("6. Square Root")
  print("7. Exponent")

  choice = int(input("Enter your choice: "))



calculator()


#### TASK 4 (Member #2)- pull the gitHub repo in your local computer  and implement the SUBTRACTION function()

def subtract(num1,num2):
  print("We are subtracting " + str(number1) + " from " + str(number2))
  return num2-num1

#### TASK 5 (Member #2)- Add the implemented the SUBTRACTION function() to your gitHub repo in a new branch called feature/subtract

#### TASK 7 (Member #3) - Add the implemented the Multiplication function() to your gitHub repo in a new branch called feature/mult
def mult(num1, num2):
  print("we are  multiplying" + str(number1) + " and " + str(number2) )
  return num1 * num2

#### TASK 9 (Member #4)- Add the implemented the Division function() to your gitHub repo in a new branch called feature/div
def div(num1, num2):
  print("we are  dividing"+ str(number1) + " and " + str(number2) )
   if num2 == 0:
  return "error can't divide by 0"
  return num1/num2
  


#### TASK 10 (Member #2)- pull the gitHub repo in your local computer  and implement the SQRT function()

#### TASK 11 (Member #2)- Add the implemented the SQRT function() to your gitHub repo in the main branch