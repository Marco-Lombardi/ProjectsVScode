#Marco Lombardi

#Exercise 8.1: Message
def display_message():
    #Prints a message about what is being learned in this chapter
    print("In this chapter, we are learning about functions in Python.")

# Calling the function
display_message()

#Exercise 8.2: Favourite Books

def favorite_book(title):
    #Prints a message about a favorite book
    print(f"One of my favorite books is {title}.")

# Calling the function with a book title
favorite_book("Alice in Wonderland")

#Exercise 8.3: T-Shirt

def make_shirt(size, message):
    #Prints a sentence summarizing the size of the shirt and the message printed on it.
    print(f"A {size} shirt will be made with the message: '{message}'.")

# Calling the function once using positional arguments
make_shirt("medium", "Hello, World!")

# Calling the function a second time using keyword arguments
make_shirt(size="large", message="Python Rocks!")