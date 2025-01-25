#Exercise 1: Write a Python program to read a file and display its contents

file1=open("C:\\Users\\hp\\Desktop\\sample.txt",'r')
print(file1.read())

#Exercise 2: Write a Python program to copy the contents of one file to another file

firstfile=open('First_file.txt','r')
data=firstfile.read()
secondfile=open('second_file.txt','w')
secondfile.write(data)
secondfile.close()
secondfile=open('second_file.txt','r')
text=secondfile.read()
print(text)


#Exercise 3:Write a Python program to read the content of a file and count the total number of words in that file


num_of_words=0
with open("Newfile.txt",'r') as file:
 content = file.read()
 words = content.split()
 word_count = len(words)
print("Total number of words:",word_count)


#Exercise 4:Write a Python program that prompts the user to input a string and converts it to an integer. Use try-except blocks to handle any exceptions that might occur

input=input("enter a string:")
try:
    int1=int(input)
    print("The converted integer is:",int1)
except:
    print("Error: The input could not be converted to an integer")
finally:
    print("For proper execution enter number string")


#Exercise 5:Write a Python program that prompts the user to input a list of integers and raises an exception if any of the integers in the list are negative.

def check_positive_integers():
    while True:
        try:
            user_input = input("Please enter a list of integers: ")
            integer_list = list(map(int, user_input.split()))

            if any(num < 0 for num in integer_list):
                raise ValueError("Negative integers are not allowed in the list.")
            else:
                print("All integers are positive. List accepted.")
                break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a list of non-negative integers.")

check_positive_integers()



#Exercise 6:Write a Python program that prompts the user to input a list of integers and computes the average of those integers. Use try-except blocks to handle any exceptions that might occur.use the finally clause to print a message indicating that the program has finished running.

def compute_average():
    while True:
        try:
            user_input = input("Please enter a list of integers: ")
            integer_list = list(map(int, user_input.split()))
            average = sum(integer_list) / len(integer_list)
            print(f"The average of the integers is: {average}")
            break
        except ValueError:
            print("Invalid input! Please enter a list of integers.")

        finally:
            print("Program has finished running.")
compute_average()


#Exercise 7 :Write a Python program that prompts the user to input a filename and writes a string to that file. Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no exception occurred.

def write_to_file():
    while True:
        try:

            filename = input("Please enter a filename to write to: ")
            content = "Welcome to my file!"
            with open('Newfile.txt','w') as file:
                file.write(content)

            print("File written successfully! Welcome message added.")
            break
        except:
            print("File not found! Please enter a valid filename.")
write_to_file()



