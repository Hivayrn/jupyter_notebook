{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "18c3aa58-2c69-4abe-bf47-04fa180e7a03",
   "metadata": {},
   "source": [
    "# Python"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "561d9778-93fe-49f9-8304-58ed04a306a7",
   "metadata": {},
   "source": [
    "**python:**\n",
    "*In simple words, it can be said that Python is a simple calculator that shows mathematical operations easily.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2eab5969-38ca-4fb5-a5e8-435fecd2dbe0",
   "metadata": {},
   "source": [
    "**Mathematical symbols:** <p> *: Multiplication</p> <p>-: Minus</p> <p>+: Sum</p> <p> **: Might</p> <p>/: Division</p>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1e9f157c-ff0c-4255-9735-41ca0879a100",
   "metadata": {},
   "source": [
    "**Famous IDE:**\n",
    "1. Pycham\n",
    "2. Visual stdio vs code\n",
    "3. Spydder IDE\n",
    "4. Ninja IDE\n",
    "5. IDLE\n",
    "6. Jupyter Notebook"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "51c07cc0-7345-4e30-923e-7be03ba758bc",
   "metadata": {},
   "source": [
    "**Python file format:** .py <p> **PointS:** </p>\n",
    "1. *Python is case sensitive.*\n",
    "2. *Space has no effect on math operations and has an effect on letters.*\n",
    "3. *The variable variable stores any value that the programmer decides.*\n",
    "4. *If the variable you wanted to write is part of the keyword, you must put an underline at the end.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "71ac2562-8cfe-4a30-bc9b-f43930417380",
   "metadata": {},
   "source": [
    "**1. Beginner level: Simple Python code Hello World**\n",
    "*<p>The simplest elementary Python code is Hello World, whose code fragment is as follows:</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    print(\"Hello World!\")\n",
    "    \"\"\"\n",
    "**Explanation:** *This program in Python simply prints the string \"Hello, World!\"*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f39e2203-166a-4e4a-aa98-927f3e5f4f1e",
   "metadata": {},
   "source": [
    "**2. Beginner level: Simple Python calculator**\n",
    "*<p>Below is a ready-made Python code for a simple calculator to add numbers.</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    num1 = float(input(\"Enter the first number: \"))\n",
    "    num2 = float(input(\"Enter the second number: \"))\n",
    "    sum = num1 + num2\n",
    "    print(\"Sum:\", sum)\n",
    "    \"\"\"\n",
    "**Explanation:** *This program takes two numbers as input from the user and calculates their sum and prints the result.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9aaa9d67-0ecb-4b2f-8c54-7f69b22687b8",
   "metadata": {},
   "source": [
    "**3. Beginner/intermediate level: Python programming codes to check the primeness of numbers**\n",
    "*<p>The following code determines whether numbers are prime or not in Python:</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    def is_prime(num):\n",
    "    if num <= 1:\n",
    "        return False\n",
    "    for i in range(2, int(num**0.5) + 1):\n",
    "        if num % i == 0:\n",
    "            return False\n",
    "    return True\n",
    "    num = int(input(\"Enter a number: \"))\n",
    "    if is_prime(num):\n",
    "        print(num, \"is a prime number.\")\n",
    "    else:\n",
    "        print(num, \"is not a prime number.\")\n",
    "    \"\"\"\n",
    "**Explanation:** *This ready-to-use Python code checks whether a given number is prime or not. A prime number is a number greater than 1 that has no divisors other than 1 and itself.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d2f3dc09-e69a-4871-82e9-2b09de27da30",
   "metadata": {},
   "source": [
    "**4. Intermediate level: Programming code in Python for Fibonacci series**\n",
    "*<p>Below is ready-made Python code to check the Fibonacci series:</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    def fibonacci(n):\n",
    "    fib_series = [0, 1]\n",
    "    while len(fib_series) < n:\n",
    "        fib_series.append(fib_series[-1] + fib_series[-2])\n",
    "    return fib_series\n",
    "    num_terms = int(input(\"Enter the number of Fibonacci terms to generate: \"))\n",
    "    print(fibonacci(num_terms))\n",
    "    \"\"\"\n",
    "**Explanation:** *This program generates the Fibonacci series up to a certain number of expressions and prints the resulting list.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "90803df4-e793-48e5-976e-ace82c9707c6",
   "metadata": {},
   "source": [
    "**5. Intermediate level: Character frequency counter with Python**\n",
    "*<p>The following program will count the characters of each sentence:</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    def count_character_frequency(sentence):\n",
    "    \n",
    "        char_frequency = {}\n",
    "        for char in sentence:\n",
    "            if char.isalpha():\n",
    "                char = char.lower()\n",
    "                char_frequency[char] = char_frequency.get(char, 0) + 1\n",
    "        return char_frequency\n",
    "\n",
    "    input_sentence = input(\"Enter a sentence: \")\n",
    "    result = count_character_frequency(input_sentence)\n",
    "\n",
    "    print(\"Character Frequencies:\")\n",
    "    for char, frequency in result.items():\n",
    "        print(f\"{char}: {frequency}\")\n",
    "    \"\"\"\n",
    "**Explanation:** *This ready-made Python code takes a sentence as input and counts the frequency of each word in the sentence, then prints a dictionary with the frequency of the words.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "008ef211-d7af-4b41-89a4-0b8df5822ce0",
   "metadata": {},
   "source": [
    "**6. Intermediate level: file encryption/decryption with Python**\n",
    "*<p>The following code is for encoding and decoding the file:</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    def encrypt(text, key):\n",
    "        encrypted_text = \"\"\n",
    "        for char in text:\n",
    "            encrypted_text += chr((ord(char) + key) % 128)\n",
    "        return encrypted_text\n",
    "    \n",
    "    def decrypt(encrypted_text, key):\n",
    "        decrypted_text = \"\"\n",
    "        for char in encrypted_text:\n",
    "            decrypted_text += chr((ord(char) - key) % 128)\n",
    "        return decrypted_text\n",
    "\n",
    "    message = \"Hello, World!\"\n",
    "    encryption_key = 3\n",
    "    encrypted_message = encrypt(message, encryption_key)\n",
    "    print(\"Encrypted Message:\", encrypted_message)\n",
    "    print(\"Decrypted Message:\", decrypt(encrypted_message, encryption_key))\n",
    "    \"\"\"\n",
    "**Explanation:** *This program demonstrates a basic encryption and decryption algorithm that shifts each message character by a specific key. It then encrypts and decrypts the message and prints the results.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a1b5c08c-fc94-40cf-972f-cd739092d24a",
   "metadata": {},
   "source": [
    "**7. Advanced Level: Web Scraping with Python**\n",
    "*<p>The following is a simple program for web scraping with Python:</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    import requests\n",
    "    from bs4 import BeautifulSoup\n",
    "\n",
    "    url = \"https://maktabkhooneh.org/mag/\"\n",
    "    response = requests.get(url)\n",
    "    soup = BeautifulSoup(response.text, \"html.parser\")\n",
    "\n",
    "    print(soup.title.text)\n",
    "    \"\"\"\n",
    "**Explanation:** *This program uses the requests library to fetch the HTML content of a web page and the BeautifulSoup library to parse the HTML and extract the page title.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "96b3599c-89a5-4166-b0e8-752e87e2eb97",
   "metadata": {},
   "source": [
    "**8. Advanced level: Image processing with OpenCV**\n",
    "*<p>Below is some Python code for image processing:</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    import cv2\n",
    "\n",
    "    image = cv2.imread(\"image.jpg\")\n",
    "    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\n",
    "\n",
    "    cv2.imshow(\"Original Image\", image)\n",
    "    cv2.imshow(\"Grayscale Image\", gray_image)\n",
    "    cv2.waitKey(0)\n",
    "    cv2.destroyAllWindows()\n",
    "    \"\"\"\n",
    "**Explanation:** *This program uses the OpenCV library to read an image from a file, convert it to grayscale, and then display both the original and grayscale images.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a3dbc7bb-7383-43e9-b349-0bbf2456b3e8",
   "metadata": {},
   "source": [
    "**9. Advanced level: Create a simple web API**\n",
    "*Below is a ready-made Python program to use the Web API in Python:*\n",
    "\n",
    "    \"\"\"\n",
    "    from flask import Flask, jsonify, request\n",
    "\n",
    "    app = Flask(__name__)\n",
    "\n",
    "    @app.route('/api/square', methods=['POST'])\n",
    "    def square_number():\n",
    "        data = request.get_json()\n",
    "        number = data.get('number')\n",
    "        result = number ** 2\n",
    "        return jsonify({'result': result})\n",
    "\n",
    "    if __name__ == '__main__':\n",
    "        app.run()\n",
    "    \"\"\"\n",
    "**Explanation:** *This app uses the Flask web framework to create a simple API that takes a JSON input with a number and returns the square of that number.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b9c34727-c6a1-4ba6-aceb-3c764d6a44f3",
   "metadata": {},
   "source": [
    "**10. Advanced level: Python code ready for natural language processing (NLP) with NLTK**\n",
    "*In the following ready-made Python code, a kind of natural language processing has been done with NLTK:*\n",
    "\n",
    "    \"\"\"\n",
    "    import nltk\n",
    "    from nltk.tokenize import word_tokenize\n",
    "    from nltk.probability import FreqDist\n",
    "\n",
    "    nltk.download('punkt')\n",
    "    text = \"This is a sample text for NLP analysis.\"\n",
    "\n",
    "    tokens = word_tokenize(text.lower())\n",
    "    fdist = FreqDist(tokens)\n",
    "\n",
    "    print(\"Tokenized Text:\", tokens)\n",
    "    print(\"Word Frequencies:\", fdist.most_common())\n",
    "    \"\"\"\n",
    "**Explanation:** *This program uses the Natural Language Toolbox (NLTK) to tokenize a text, convert it to lowercase, calculate word frequency, and print the results. These 10 ready-to-use Python code samples cover a range of difficulty levels and demonstrate various functions and applications of Python programming. You can provide these examples to users who are looking to learn and experiment with Python programming.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "12445d1f-fe6c-4f10-a2b8-c2a06ec9cf00",
   "metadata": {},
   "source": [
    "**examples for programming with Python:**\n",
    "1. Number Guessing Game: Write a program that generates a random number and asks the user to guess it.\n",
    "2. To-do list application: Create a simple command-line to-do list application that allows users to add, view, and delete tasks.\n",
    "3. Dice Roll Simulator: Build a program that simulates rolling dice. Ask the user how many dice they want to roll and how many sides each die has.\n",
    "4. Doz game with Python: Doz game project with Python is also one of the popular projects that you can work on.\n",
    "5. Snake or Snack game with Python: Another recommended project is Snake or Snack game, which you can implement with Python and the pygame library.\n",
    "6. Weather forecast app: Use a weather API to build a simple app that fetches and displays the weather forecast for the user's location.\n",
    "7. Password Generator: Create a program that generates random and secure passwords based on user preferences (length, special characters, etc.).\n",
    "8. Rock-paper-scissors game with Python: Play a two-player rock-paper-scissors game where the computer decides the winner.\n",
    "9. Basic Calculator Graphical User Interface: Create a graphical user interface (GUI) for a basic calculator that performs arithmetic operations. You can use Google search to download the ready Python code of this project."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b1eb1f3e-4dff-4027-893a-3fb6fa7e7b8d",
   "metadata": {},
   "source": [
    "**Best resources for ready-made Python code:**\n",
    "*<p>There are many great resources where you can find ready-made Python code samples, tutorials, and projects to learn and improve your Python programming skills. Here are some popular and trusted platforms:</p>*\n",
    "\n",
    "1. Official Python Documentation: The official Python website (org) provides comprehensive documentation, including tutorials and code samples, covering various Python modules and features.\n",
    "2. GitHub: GitHub is an extensive code repository where you can find a wide variety of projects, Python programming examples, Python library usage examples, and Python code snippets. In Python, you can download ready-made Python code and customize them.\n",
    "3. Stack Overflow: Stack Overflow (stackoverflow.com) is a popular question and answer platform for developers. You can find tons of Python code snippets and solutions for various programming problems.\n",
    "Real Python: Real Python (realpython.com) 4 offers a collection of high-quality Python tutorials and articles ranging from beginner to advanced. Some content is available for free.\n",
    "4. GeeksforGeeks: GeeksforGeeks (geeksforgeeks.org) is a website that covers a variety of programming topics, including Python. This tutorial provides ready-made Python code samples and interview preparation resources.\n",
    "5. PythonFor Beginners: PythonForBeginners (pythonforbeginners.com) is a resource specifically targeted at beginners to Python. This sample provides simple code and tutorials for beginners.\n",
    "6. Code Academy: Codecademy (codecademy.com) offers interactive Python courses that you can learn by coding directly in the browser. It is a great platform for hands-on learning.\n",
    "7. Programiz: Programiz (programiz.com) provides Python tutorials, examples, and an online Python compiler for practice.\n",
    "8. DataCamp: DataCamp (datacamp.com) specializes in data science and offers Python courses with a focus on data analysis, visualization, and machine learning.\n",
    "9. YouTube: YouTube has an extensive collection of Python tutorials and code guides from various developers.\n",
    "10. ChatGPT: This is a type of chatbot based on artificial intelligence, which is a product of OPENAI and you can use it as a programmer's assistant. You can ask it prompts that will give you all kinds of python code. You can learn how to use ChatGPT in the tutorial.\n",
    " \n",
    "**Point:** *When using online resources, always check that the content is up-to-date, especially if you run into compatibility issues with Python versions. Additionally, practice programming regularly and try to apply what you learn to personal projects to strengthen your understanding of Python programming.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e262180-6af3-4fa9-a6f8-6039dce90f04",
   "metadata": {},
   "source": [
    "**Exercise 1:** *Calculate the factorial of a number with Python*\n",
    "*<p>The code of this Python programming exercise is as follows:*</p>\n",
    "\n",
    "    \"\"\"\n",
    "    def factorial(n):\n",
    "    if n == 0:\n",
    "        return 1\n",
    "    else:\n",
    "        return n * factorial(n-1)\n",
    "\n",
    "    num = 5\n",
    "    print(\"Factorial of\", num, \"is\", factorial(num))\n",
    "    \"\"\"\n",
    "\n",
    "*This code calculates the factorial of a given number using return. The factorial function takes an integer n as input and returns its factorial. The base case is when n is 0, in which case the factorial is 1. Otherwise, it calls its factorial with n-1 and multiplies the result by n.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fff485cb-5d21-487c-83b1-77d442be74db",
   "metadata": {},
   "source": [
    "**Exercise 2:** *Sum of digits of a number with Python*\n",
    "*<p>The mentioned exercise code fragment is as follows:</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    def sum_of_digits(num):\n",
    "    total = 0\n",
    "    while num > 0:\n",
    "        total += num % 10\n",
    "        num //= 10\n",
    "    return total\n",
    "\n",
    "    number = 12345\n",
    "    print(\"Sum of digits in\", number, \"is\", sum_of_digits(number))\n",
    "    \"\"\"\n",
    "*<p>This code will calculate the sum of the digits of a given number. This Python programming exercise uses a while loop to extract each digit from the number, add it to the total variable, and then divide the integer by 10 to remove the last digit from the number. This loop continues until the number becomes 0.</p>*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b722c664-d239-4588-89c5-28ae8ffbacfc",
   "metadata": {},
   "source": [
    "**Exercise 3:** *Reversing strings with Python*\n",
    "*<p>The Python programming practice code snippet for reversing the string is as follows:</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    def reverse_string(input_str):\n",
    "        return input_str[::-1]\n",
    "\n",
    "    text = \"Salam maktabkhooneh\"\n",
    "    print(\"Reversed:\", reverse_string(text))\n",
    "    \"\"\"\n",
    "*<p>The code above defines a function reverse_string that takes an input string input_str and returns its image using truncation.</p>*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae4a439b-5144-44fc-94e2-a0c001c68b09",
   "metadata": {},
   "source": [
    "**Exercise 4:** *Finding common elements in lists*\n",
    "\n",
    "    \"\"\"\n",
    "    def common_elements(list1, list2):\n",
    "        return list(set(list1) & set(list2))\n",
    "\n",
    "    list_a = [1, 2, 3, 4, 5]\n",
    "    list_b = [3, 4, 5, 6, 7]\n",
    "    print(\"Common elements:\", common_elements(list_a, list_b))\n",
    "    \"\"\"\n",
    "*<p>The above code defines a common_elements function that takes two lists list1 and list2 as input and returns a new list containing their common elements. This code uses sets to find the intersection of two lists and then converts the result into a list.</p>*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b6944c36-5ce1-4dab-a4e0-82ce72210cfe",
   "metadata": {},
   "source": [
    "**Exercise 5:** *Palindrome check*\n",
    "\n",
    "    \"\"\"\n",
    "    def is_palindrome(word):\n",
    "        return word == word[::-1]\n",
    "\n",
    "    text = \"radar\"\n",
    "    if is_palindrome(text):\n",
    "        print(text, \"is a palindrome.\")\n",
    "    else:\n",
    "        print(text, \"is not a palindrome.\")\n",
    "    \"\"\"\n",
    "**Point:** *Palindrome means that reading the text from left and right becomes one word, This code checks whether a given word string is a palindrome or not using a slicer. The is_palindrome function returns True if the word is equal to its inverse, and False otherwise.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f210cc34-ad57-4a97-bf7e-704d97c513bf",
   "metadata": {},
   "source": [
    "**What are data types in Python?**\n",
    "*<p>Python has several built-in data types, including:</p>*\n",
    "1. Number types: int, float, complex\n",
    "2. Sequence types: str, list, tuple\n",
    "3. Mapping type: dict\n",
    "4. Types of sets: set, frozenset\n",
    "5. Boolean type: bool"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "be928949-8b1d-4b50-9c88-7bc3dc3d1129",
   "metadata": {},
   "source": [
    "**How is a passing comment in Python?**\n",
    "*<p># is used to write a single line comment in Python. For multi-line comments, you can use triple quotes (\"' or \"\") at the beginning of the block.</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    # This is a single-line comment\n",
    "\n",
    "    '''\n",
    "    This is a\n",
    "    multi-line comment\n",
    "    '''\n",
    "    \"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2934424f-6940-482e-b40a-b3ba217b4f71",
   "metadata": {},
   "source": [
    "**How to create a function in Python?**\n",
    "*<p>You can create a function in Python by using the def keyword, followed by the function name, a list of parameters (if any), and a colon. The function code block is placed under the def statement.</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    def greet(name):\n",
    "\n",
    "    print(\"Hello, \" + name + \"!\")\n",
    "    \"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "959cd712-6a0b-4f48-b9ea-ecc932a4a2eb",
   "metadata": {},
   "source": [
    "**How do you use if-else statements in Python?**\n",
    "*<p>Python uses the if, elif (else if) and else keywords for conditional statements.</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    x = 10\n",
    "    if x > 0:\n",
    "    print(\"Positive\")\n",
    "    elif x < 0:\n",
    "    print(\"Negative\")\n",
    "    else:\n",
    "    print(\"Zero\")\n",
    "    \"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "04e92320-1b92-44a5-badf-afcdaf07824e",
   "metadata": {},
   "source": [
    "**How to traverse a list in Python?**\n",
    "*<p>You can use a for loop to traverse a Python list as follows.</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    fruits = [\"apple\", \"banana\", \"orange\"]\n",
    "    for fruit in fruits:\n",
    "    print(fruit)\n",
    "    \"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0ede6bdb-dd60-4c6a-8a54-bcc996749392",
   "metadata": {},
   "source": [
    "**What is a module in Python and how do you import it?**\n",
    "*<p>A module in Python is a file that contains Python definitions and expressions. You can use the import keyword in Python to import a module and access its functions, classes, or variables.</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    import math\n",
    "\n",
    "    result = math.sqrt(25)\n",
    "    print(result)\n",
    "    \"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c9f965f4-878d-4be8-ae82-91e1596c34d7",
   "metadata": {},
   "source": [
    "**How to handle exceptions in Python?**\n",
    "*<p>Python uses try and except for this purpose, and on the other hand, you can optionally use else and finally for this purpose.</p>*\n",
    "\n",
    "    \"\"\"\n",
    "    try:\n",
    "    num = int(input(\"Enter a number: \"))\n",
    "    result = 10 / num\n",
    "    print(\"Result:\", result)\n",
    "    except ValueError:\n",
    "    print(\"Invalid input. Please enter a valid number.\")\n",
    "    except ZeroDivisionError:\n",
    "    print(\"Cannot divide by zero.\")\n",
    "    else:\n",
    "    print(\"No exceptions occurred.\")\n",
    "    finally:\n",
    "    print(\"Execution completed.\")\n",
    "    \"\"\"\n",
    "*<p>In this example, if the user enters a non-numeric value or zero, the corresponding exception will be thrown and an appropriate message will be printed. If no exception occurs, the else block will be executed. The finally block is always executed regardless of whether an exception has occurred or not.</p>*"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
