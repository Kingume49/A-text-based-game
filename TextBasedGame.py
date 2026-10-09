# TextBasedGame.py


# Function to display game instructions and commands
def show_instructions():
    print("Haunted Mansion Text Adventure Game")
    print("Collect 6 items to escape the mansion before facing the Ghost!")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get [item name]")
    print("-" * 50)


# Function to display the player's current status
def show_status(current_room, inventory, rooms):
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")

    # Display item in the room if it exists and is not the villain
    if "item" in rooms[current_room]:
        item = rooms[current_room]["item"]
        if item != "Ghost":
            print(f"You see a {item}")
    print("-" * 50)


# Main function that contains the gameplay loop
def main():
    # Dictionary linking rooms and items
    rooms = {
        "Foyer": {"North": "Library", "East": "Dining Room"},
        "Library": {"South": "Foyer", "East": "Study", "item": "Ancient Book"},
        "Study": {"West": "Library", "item": "Silver Key"},
        "Dining Room": {"West": "Foyer", "North": "Kitchen", "item": "Flashlight"},
        "Kitchen": {"South": "Dining Room", "East": "Basement", "item": "Knife"},
        "Basement": {"West": "Kitchen", "item": "Rope"},
        "Attic": {"South": "Study", "item": "Amulet"},
        "Secret Room": {"item": "Ghost"}  # Villain room
    }

    # Add additional room connections
    rooms["Study"]["North"] = "Attic"
    rooms["Attic"]["South"] = "Study"
    rooms["Basement"]["North"] = "Secret Room"
    rooms["Secret Room"]["South"] = "Basement"

    # Starting values
    current_room = "Foyer"
    inventory = []
    total_items_needed = 6

    show_instructions()

    # Gameplay loop
    while True:
        show_status(current_room, inventory, rooms)

        # Check for villain encounter
        if "item" in rooms[current_room] and rooms[current_room]["item"] == "Ghost":
            if len(inventory) == total_items_needed:
                print("Congratulations! You have collected all items and defeated the Ghost!")
            else:
                print("NOM NOM... The Ghost has caught you... GAME OVER!")
            print("Thanks for playing the game. Hope you enjoyed it.")
            break

        # Get player input
        player_input = input("Enter your move: ").strip().lower()
        print()

        # Handle movement commands
        if player_input.startswith("go "):
            direction = player_input.split(" ")[1].capitalize()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")

        # Handle item collection
        elif player_input.startswith("get "):
            item_requested = player_input[4:].strip()

            if "item" in rooms[current_room]:
                room_item = rooms[current_room]["item"]

                if item_requested.lower() == room_item.lower():
                    if room_item not in inventory:
                        inventory.append(room_item)
                        print(f"{room_item} added to inventory.")
                        del rooms[current_room]["item"]  # Remove item after pickup
                    else:
                        print("You already have that item.")
                else:
                    print("That item is not in this room.")
            else:
                print("There is no item in this room.")

        # Handle invalid commands
        else:
            print("Invalid command. Try again.")


# Run the game
if __name__ == "__main__":
    main()
