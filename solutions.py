
# 1.
import numpy as np

a = np.array([1,2,3,4])

def show_elements(arr):
    for el in arr:
        print(el)

show_elements(a)

# 2.

# import numpy as np

b = np.array([1,5,-2,10])

# iterative approach
def array_sum(numberArr):
    arrSum = 0
    for i in numberArr:
        arrSum = arrSum + i
    return arrSum

print(array_sum(b))

# uncomment the below function to test the recursive approach
# def array_sum_recursive(numberArr):
#     if len(numberArr) == 1:
#         return numberArr[0]
    
#     # Recursive case
#     return numberArr[0] + array_sum(numberArr[1:])

# print(array_sum_recursive(b))


# uncomment the below line to test the solution using the NumPy sum operator
# print(b.sum())

# 3.import numpy as np

a = np.array([1,2,3,4])

def multiply_elements_by_3(arr):
    return 3 * arr

multiply_elements_by_3(a)



# Activity: Choosing and Implementing Data Structures
# In this activity, you will determine which data structures are the most efficient for certain situations as well as create arrays in Python.

# There are two parts of this activity:

# In the first part, you will pick the best data structure to use for different situations.
# In the second part, you will learn how to implement an array in Python.
# 1. Choose Your Data Structure
# Data needs to be stored in different structures based on the situation. Read each scenario or question and choose the best data structure for the situation. In other words, pick the data structure that would help make a program the most efficient and scalable.

# Reminder: Review your notes and the slides from the previous lesson to help answer these questions.

# Print Requests
# You need to store the order in which print requests are made upon their arrival. The orders must be printed in the order of their arrival.

# Array
# Stack
# Singly linked list
# Queue
# Undoing Operation
# You need to be able to undo operations in a text editor. Which data structure allows us to undo operations in a text editor?

# Array
# Stack
# Hash Table
# Queue
# Music Playlist
# You need to be able to play a past and next song in a playlist.

# Array
# List
# Singly linked list
# Doubly linked list
# Customer Orders
# You need to store the customer order information at a restaurant (for a drive-thru).

# Array
# Stack
# Queue
# Followers
# You need to be able to store who follows who for a social media site.

# Array
# Stack
# Singly linked list
# Queue
# Tree
# At this point, you have reviewed which data structures are best for different situations. Now it is time to implement and work with arrays in Python.

# 2. Working with Arrays
# Setup
# Instructions:
# Click HERE for the link to the repo.
# Fork (not clone) it to your OWN GitHub account.
# Now to clone the repo to your machine, click the green 'Code' button and then copy the URL.
# In a new terminal, or Git Bash, go to where you want to clone the repo.
# Type git clone in the terminal or Git Bash, then a space, then paste the URL you copied from your repo. Example:
# undefinedClick here to copy
# Hit "Enter" or "Return" whichever is on your keyboard.
# Now, in your terminal, change to your repository directory (cd repo name)
# Open your repository in Visual Studio Code.
# Open terminal in your Visual Studio Code.
# Do the assignment in Visual Studio Code and stage your changes using git add -A command.
# Make at least one commit by using git commit -m "write your message here" command. Example:
# undefinedClick here to copy
# Finally push your changes using the git push command. Example:
# undefinedClick here to copy
# When you get to the second part of the activity, start problem solving and coding.

# Arrays
# An array is not a built-in data structure in Python, but there is a Python library called NumPy that can be used. There are other options for using arrays in Python, such as using the array module, but we will focus on using the NumPy Python library when working with arrays.

# NumPy stands for Numerical Python, and is often used in performing mathematical operations such as matrix multiplication and other linear algebra tasks. It is very useful for most applications where arrays would be preferred over lists, and is a powerful tool to add to your toolbox of resources.

# Note that we will be working in the 'arrays' folder for this section.

# If any of the steps below do not work for you, read the NumPy documentation for a detailed introduction and overview of NumPy. Reference the installation documentation for NumPy for additional instructions.

# Since we already have Python installed, run the following in the terminal to install NumPy:

# undefinedClick here to copy
# Let's check if NumPy is installed correctly by creating an array. Declare an array by using the following example:

# undefinedClick here to copy
# We need to import the NumPy library, which is shown on line 1. Note that np is used as an alias and is a widely adopted practice for better code readability when using NumPy.

# To create an array, we use the np.array() function. To create a basic one-dimensional array, we want to pass a list into the function. An example of this can be seen on line 2, where a numerical array named 'a' is declared.

# If you are having an error running Python2 versus Python3, debug the error in your terminal. Running the following command will use Python3 to install NumPy: 'python3 -m pip install numpy''.

# Practice with NumPy Arrays
# Now that we have NumPy installed correctly, we will practice working with NumPy arrays by completing the following two challenges.

# 1. Write a program that prints each item in a numerical array individually.

# For example, if we had an array of [1,2,3], the output would look like this:
# undefinedClick here to copy
# 2. Calculate the sum of an array of numbers. Try doing this without using a loop (refer to numpy's array methods to accomplish this).

# For example, if we had an array of [1,6,3], the output would be 10 (1+6+3=10).
# 3. Use a single operation (no loops) to multiply every element of an array by 3.

# For example, if we had an array of [1,6,3], the output would be [3,18,9].
# If stuck, check your code against the possible solutions here.

# This is a brief introduction to working with arrays in Python, but now you have created and used one-dimensional NumPy arrays when writing algorithms. You can read the NumPy documentation or w3schools documentation for more information about using NumPy arrays.

# Acceptance Criteria
# When given a description of a scenario for an application, you can determine which data structure is the best (most efficient) for the situation.
# Note that this will not be part of the submitted repository but is referring to the questions in the first part of the activity.
# Given the NumPy library is installed and imported correctly, you can create a one-dimensional array.
# When running your first program, each item in a numerical array is printed individually.
# When running your second program, the sum of a numerical array is calculated correctly.
# When running your third program, the values in an array are multiplied by 3.
# Before submitting, make sure you do a self-review of your code. Check for formatting and spelling, include comments in your code, and ensure that you have a healthy commit history.

# Make sure to submit your github repository link on the submission page.

# Summary
# You are learning about various data structures and algorithms in this course that can help you with future coding challenges. As stated before, practice is how you will continue to become a better coder and problem solver. Practice is also how you will better understand difficult computer science concepts. Make sure to reach out to your instructional staff and other learners with questions as needed.

# Remember: If stuck, do not panic. Problem solving and understanding these concepts take time!

# Feel free to check out the solutions branch linked above. Note that when reading additional resources and working more in Python, you will probably see lists used interchangeably with arrays, as lists are basically dynamic arrays. However, it is important to know the difference and the distinction between lists, arrays, and linked lists, especially for technical interviews.