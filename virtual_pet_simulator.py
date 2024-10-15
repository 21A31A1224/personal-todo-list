import random

# Define a function to create a new pet
def create_pet():
    name = input("What's the name of your pet? ")
    pet = {
        "name": name,
        "happiness": 50,
        "hunger": 50
    }
    return pet

# Function to feed the pet
def feed_pet(pet):
    if pet["hunger"] > 0:
        pet["hunger"] = max(0, pet["hunger"] - 20)  # Reduces hunger
        pet["happiness"] = max(0, pet["happiness"] - 5)  # Slight happiness decrease
        print(f"{pet['name']} is fed! Hunger decreased, happiness slightly reduced.")
    else:
        print(f"{pet['name']} is not hungry.")

# Function to play with the pet
def play_with_pet(pet):
    if pet["happiness"] < 100:
        pet["happiness"] = min(100, pet["happiness"] + 20)  # Increases happiness
        pet["hunger"] = min(100, pet["hunger"] + 5)  # Slight hunger increase
        print(f"{pet['name']} is happy! Happiness increased, hunger slightly increased.")
    else:
        print(f"{pet['name']} is already very happy.")

# Function to give toy to the pet
def give_toy(pet):
    if pet["happiness"] < 100:
        pet["happiness"] = min(100, pet["happiness"] + 10)  # Boosts happiness
        print(f"{pet['name']} loves the new toy! Happiness increased.")
    else:
        print(f"{pet['name']} doesn't want a toy right now.")

# Function to give medicine to the pet
def give_medicine(pet):
    if pet["hunger"] >= 80:
        pet["hunger"] = max(0, pet["hunger"] - 40)  # Reduces hunger by a lot
        pet["happiness"] = max(0, pet["happiness"] - 10)  # Slight happiness decrease
        print(f"{pet['name']} took the medicine. Hunger greatly reduced, but happiness slightly decreased.")
    else:
        print(f"{pet['name']} doesn't need medicine right now.")

# Function to check the pet's status
def check_status(pet):
    print(f"{pet['name']}'s Status: Happiness = {pet['happiness']}, Hunger = {pet['hunger']}")

# Function for automatic changes
def automatic_changes(pet):
    pet["hunger"] = min(100, pet["hunger"] + 10)  # Hunger increases over time
    pet["happiness"] = max(0, pet["happiness"] - 10)  # Happiness decreases over time

# Function to check for game over
def check_game_over(pet):
    if pet["hunger"] >= 100:
        print(f"{pet['name']} is too hungry. Game over!")
        return True
    elif pet["happiness"] <= 0:
        print(f"{pet['name']} is too sad. Game over!")
        return True
    return False

# Random event system
def random_event(pet):
    event = random.choice(["find_snack", "get_sick", "nothing"])
    
    if event == "find_snack":
        pet["hunger"] = max(0, pet["hunger"] - 15)
        print(f"Good news! {pet['name']} found a snack and feels less hungry.")
    elif event == "get_sick":
        pet["hunger"] = min(100, pet["hunger"] + 20)
        pet["happiness"] = max(0, pet["happiness"] - 20)
        print(f"Oh no! {pet['name']} got sick. Hunger increased, happiness decreased.")
    else:
        print(f"{pet['name']} is doing fine, no random events.")

# Main menu and game loop
def main():
    pets = []
    
    # Create multiple pets
    num_pets = int(input("How many pets do you want to manage? "))
    for i in range(num_pets):
        pets.append(create_pet())
    
    actions = 0
    
    while True:
        print("\nMenu:")
        print("1. Feed the pet")
        print("2. Play with the pet")
        print("3. Give a toy to the pet")
        print("4. Give medicine to the pet")
        print("5. Check pet's status")
        print("6. Quit")
        
        pet_choice = int(input(f"Which pet do you want to interact with? (1-{len(pets)}): ")) - 1
        pet = pets[pet_choice]
        
        choice = input("Choose an action: ")
        
        if choice == "1":
            feed_pet(pet)
        elif choice == "2":
            play_with_pet(pet)
        elif choice == "3":
            give_toy(pet)
        elif choice == "4":
            give_medicine(pet)
        elif choice == "5":
            check_status(pet)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
        
        actions += 1
        
        # Every 3 actions, apply automatic changes and random events
        if actions % 3 == 0:
            automatic_changes(pet)
            random_event(pet)
            print("Time passes... Hunger and happiness have changed.")
        
        # Check if the game is over
        if check_game_over(pet):
            break

if __name__ == "__main__":
    main()
