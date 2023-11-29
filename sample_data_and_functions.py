import random

# Sample data for random animal
animal_names = ["Bella", "Max", "Charlie", "Luna", "Lucy", "Milo", "Buddy", "Daisy", "Bailey", "Lola",
    "Rocky", "Sadie", "Toby", "Zoe", "Coco", "Ruby", "Oscar", "Molly", "Oliver", "Stella",
    "Winston", "Penny", "Jack", "Lily", "Duke", "Rosie", "Louie", "Maggie", "Bentley", "Sophie",
    "Chloe", "Harley", "Bear", "Ellie", "Jasper", "Abby", "Ginger", "Murphy", "Lily", "Rudy",
    "Marley", "Sammy", "Frankie", "Hazel", "Thor", "Pepper", "Hunter", "Nala", "Grace", "Bruno",
    "Layla", "Hank", "Annie", "Apollo", "Lulu", "Ace", "Remy", "Willow", "Leo", "Piper",
    "Archer", "Luna", "Gus", "Nova", "Finn", "Izzy", "Benji", "Mocha", "Blue", "Belle",
    "Athena", "Dexter", "Maisie", "Oreo", "Chester", "Rosie", "Scout", "Boomer", "Millie", "Simba",
    "Koda", "Phoebe", "Zeus", "Lacey", "Moose", "Roxy", "Otis", "Jax", "Callie", "Titan",
    "Pearl", "Rex", "Fluffy", "Shadow", "Bandit", "Tasha", "Bruce", "Ivy", "Bobby", "Scooby Doo", "Momo", "Mickey",
    "Allie", "Barbie", "Marley", "Rex", "Azor", "Cutey Pie"]
species_list = ["Dog", "Cat", "Rabbit", "Bird", "Fish", "Turtle", "Hamster", "Lizard"]
colors = ["Black", "White", "Brown", "Grey", "Golden", "Spotted", "Striped"]
food_preferences = ["Dry Food", "Wet Food", "Carrots", "Seeds", "Insects", "Fruits", "Vegetables", "Meat", "Omnivore"]

# sample data for random person
first_names = ['John', 'Mary', 'Michael', 'Jennifer', 'David', 'Susan', 'Robert', 'Lisa', 'William', 
    'Karen', 'James', 'Nancy', 'Joseph', 'Sarah', 'Richard', 'Linda', 'Charles', 'Patricia', 
    'Daniel', 'Jessica', 'Thomas', 'Angela', 'Christopher', 'Kimberly', 'Matthew', 'Elizabeth', 
    'Andrew', 'Laura', 'Nicholas', 'Amanda', 'Kevin', 'Emily', 'Mark', 'Rachel', 'Brian', 'Rebecca', 
    'Steven', 'Megan', 'Timothy', 'Sandra', 'Jason', 'Stephanie', 'Jeffrey', 'Nicole', 'Benjamin', 
    'Christina', 'Ryan', 'Heather', 'Christopher', 'Melissa']
last_names = ['Smith', 'Johnson', 'Brown', 'Davis', 'Wilson', 'Lee', 'Clark', 'Martinez', 'Hall', 'Allen', 
    'Turner', 'Garcia', 'Walker', 'Lewis', 'White', 'Thomas', 'Adams', 'Young', 'Harris', 'Turner', 
    'Miller', 'Baker', 'Green', 'Scott', 'King', 'Carter', 'Nelson', 'Hall', 'Davis', 'Wright', 
    'Anderson', 'Moore', 'Harris', 'Stewart', 'Taylor', 'Martin', 'Evans', 'Turner', 'Parker', 
    'Walker', 'Mitchell', 'Adams', 'Hall', 'Johnson', 'Allen', 'Wilson', 'Mitchell', 'Moore', 
    'Carter', 'Brown']
hobbies = [    "Reading", "Painting", "Playing Chess", "Gardening", "Hiking",
    "Cooking", "Photography", "Swimming", "Playing Guitar", "Dancing",
    "Birdwatching", "Yoga", "Fishing", "Cycling", "Sculpting",
    "Playing Soccer", "Knitting", "Writing", "Meditation", "Traveling"]
sexes = ['F', 'M']


# Function to generate a random animal record
def generate_random_animal():
    name = random.choice(animal_names)
    species = random.choice(species_list)
    age = random.randint(1, 15)  # Random age between 1 and 15
    color = random.choice(colors)
    food_preference = random.choice(food_preferences)
    return f'{name},{species},{age},{color},{food_preference}'

animals_columns = 'id,name,species,age,color,food_preference'

# Writing data to a CSV file
def write_data_to_csv(filename, number):
    with open(filename, mode='w') as file:
        # Writing number of random records
        for id in range(number):
            animal = generate_random_animal()
            file.write(str(id) + "," + animal + "\n")

# Writing data to a CSV file with headers
def write_data_to_csv_headers(filename, number):
    with open(filename, mode='w') as file:
        # Writing the header
        file.write(f"{animals_columns}\n")
        # Writing number of random records
        for id in range(number):
            animal = generate_random_animal()
            file.write(str(id) + "," + animal + "\n")

# Function to generate a random person record
def generate_random_person():
    name = random.choice(first_names)
    sex = random.choice(sexes)
    height = random.randint(150, 210)
    hobby = random.choice(hobbies)
    # return f'{name},{sex},{height},{hobby}'
    return [name, sex, height, hobby]

# people_columns = 'id,name,sex, height, hobby'
