import json

# Define the main index structure
main_index = {
    "wheat": {
        "varieties": [],
        "diseases": [],
        "cultivation": {},
        "uses": [],
        "communication": []
    },
    "wood": {
        "types": [],
        "properties": {},
        "uses": [],
        "communication": []
    }
}

def save_index():
    # Save the main index to a JSON file
    with open("main_index.json", "w") as file:
        json.dump(main_index, file)

def load_index():
    # Load the main index from a JSON file
    try:
        with open("main_index.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return main_index

def add_item(index_type, sub_index_type):
    # Add information about an item
    name = input(f"Enter {sub_index_type} name: ")
    description = input("Enter description: ")
    main_index[index_type][sub_index_type].append({"name": name, "description": description})
    
    # Include communication/advertisement details
    communication = input("Enter communication/advertisement method: ")
    main_index[index_type]["communication"].append({"name": name, "method": communication})
    
    save_index()

def display_index():
    # Display the main index
    print(json.dumps(main_index, indent=4))

def main():
    main_index = load_index()

    while True:
        print("\nWheat and Wood Information Index\n")
        print("1. Add Wheat Variety")
        print("2. Add Wood Type")
        print("3. Display Index")
        print("4. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            add_item("wheat", "varieties")
        elif choice == "2":
            add_item("wood", "types")
        elif choice == "3":
            display_index()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
