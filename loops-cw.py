
# ### Exercise 1:
# Print -20 to and including 50. Use any loop you want.
#

# for x in range(-20,51):
#     print(x)
#

# ### Exercise 2:
# Create a loop that prints even numbers from 0 to and including 20.Hint: You can find multiples of 2 with (whatever_number % 2 == 0)
#

# start = 0
# end = 20
# for num in range(start, end +1):
#     if num %2==0:
#         print(num, end = " ")

# ### Exercise 3:
# Prompt the user for 3 numbers. Then print the 3 numbers along with their average after the 3rd number is entered. Refer to example below replacing ```NUMBER1```, ```NUMBER2```, ```NUMBER3```, and ```THEAVERAGE``` with the actual values.
#
# Ex.Output
# ```
# The average of NUMBER1, NUMBER2, and NUMBER3 is THEAVERAGE
# ```

userInput1=int(input("Enter a number"))
userInput2=int(input("Enter another number"))
userInput3=int(input("Enter another number"))
sum= userInput1 + userInput2 +userInput3
aver=sum/3
print(sum)
print(aver)




# ### Exercise 4:
# Use any loop to print all numbers between 0 and 100 that are divisible by 4.
#
# ### Challenge:
# Password Checker - Ask the user to enter a password. Ask them to confirm the password. If it's not equal, keep asking until it's correct or they enter 'Q' to quit.


