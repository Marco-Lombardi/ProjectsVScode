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

#Exercise 8.7: Album

def make_album(artist_name, album_title, num_songs=None):
    #Builds a dictionary describing a music album.
    album = {
        'artist': artist_name,
        'title': album_title
    }
    if num_songs:
        album['songs'] = num_songs
    return album

# Making three dictionaries representing different albums
album1 = make_album("Artist1", "Album1")
album2 = make_album("Artist2", "Album2", 12)
album3 = make_album("Artist3", "Album3", 8)

# Printing each return value to show that the dictionaries are storing the album information correctly
print(album1)
print(album2)
print(album3)

#Exercise 8.8: User Album

def make_album(artist_name, album_title):
    #Builds a dictionary describing a music album.
    album = {
        'artist': artist_name,
        'title': album_title
    }
    return album

# While loop to allow users to enter album information
while True:
    artist = input("Enter the artist's name: ")

    title = input("Enter the album title: ")
    
    # Call make_album() with user's input and print the created dictionary
    album_info = make_album(artist, title)
    print(album_info)

#Exercise 8-9: Messages
def show_messages(messages):
    # Prints each text message from a list.
    for message in messages:
        print(message)

# List containing a series of short text messages
text_messages = [
    "Hello!",
    "How are you?",
    "Just checking in.",
    "Have a great day!"
]

# Calling the show_messages() function
show_messages(text_messages)

# Exercise 8.10: Send Messages

def show_messages(messages):
    # Prints each text message from a list.
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    
    # Prints each text message from a list,
    # and moves each message to a new list called sent_messages.
    
    for message in messages:
        print(message)
        sent_messages.append(message)

# List containing a series of short text messages
text_messages = [
    "Hello!",
    "How are you?",
    "Just checking in.",
    "Have a great day!"
]

# List to store sent messages
sent_messages = []

# Calling the send_messages() function
send_messages(text_messages, sent_messages)

# Printing both lists to make sure the messages were moved correctly
print("\nOriginal Messages:")
show_messages(text_messages)

print("\nSent Messages:")
show_messages(sent_messages)



