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

#Exercise 8.4: Large Shirts

def make_shirt(size="large", message="I love Python"):
    #Prints a sentence summarizing the size of the shirt and the message printed on it.
    print(f"A {size} shirt will be made with the message: '{message}'.")

# Making a large shirt with the default message
make_shirt()

# Making a medium shirt with the default message
make_shirt(size="medium")

# Making a shirt of any size with a different message
make_shirt(size="small", message="Keep Calm and Code On!")

#Exercise 8.5: Cities

def describe_city(city, country="Iceland"):
    """Prints a simple sentence describing the city and its country."""
    print(f"{city} is in {country}.")

# Calling the function for three different cities
describe_city("Reykjavik")
describe_city("Tokyo", "Japan")
describe_city("Paris", "France")

#Exercise 8.6 City Names

def city_country(city, country):
    #Returns a string formatted as 'city, country'.
    return f"{city}, {country}"

# Calling the function with three city-country pairs and printing the returned values
print(city_country("Santiago", "Chile"))
print(city_country("Tokyo", "Japan"))
print(city_country("Paris", "France"))
