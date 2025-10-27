"""Lab 5 python file"""
import json
import logging  

def add_item(stock_data, item="default", qty=0):
    """Adds a specified quantity of an item to the stock."""
    if not isinstance(item, str) or not item:
        logging.error("Invalid name: %s. Must be a non-empty string.", item)
        return
    if not isinstance(qty, int):
        logging.error("Invalid quantity %s for item %s. Must be integer.", qty, item)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logging.info("Added %s of %s.New total: %s", qty, item, stock_data.get(item))

def remove_item(stock_data, item, qty):
    """Removes a specified quantity of an item from the stock."""
    # Input validation
    if not isinstance(item, str) or not item:
        logging.error("Invalid item name: %s. Must be a non-empty string.", item)
        return
    if not isinstance(qty, int):
        logging.error("Invalid quantity: %s for item %s. Must be an integer.", qty, item)
        return

    try:
        stock_data[item] -= qty
        logging.info("Removed %s of %s. New total: %s", qty, item, stock_data.get(item, 0))
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Item %s removed from stock (quantity <= 0).", item)
    except KeyError:
        logging.warning("Attempted to remove %s, but it was not in stock.", item)

def get_qty(stock_data, item):
    """Gets the current quantity of a specific item."""
    if not isinstance(item, str) or not item:
        logging.error("Invalid item name: %s for get_qty.", item)
        return 0  # Return a safe default

    return stock_data.get(item, 0)

def load_data(file="inventory.json"):
    """Loads the inventory data from a JSON file."""
    loaded_stock = {}
    try:
        with open(file, "r", encoding="utf-8") as f:
            loaded_stock = json.loads(f.read())
            logging.info("Stock data loaded from %s.", file)
    except FileNotFoundError:
        logging.warning("%s not found. Starting with empty inventory.", file)
    except json.JSONDecodeError:
        logging.error("Could not decode JSON from %s. Starting with empty inventory.", file)
    return loaded_stock


def save_data(stock_data, file="inventory.json"):
    """Saves the current inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            f.write(json.dumps(stock_data, indent=4))
            logging.info("Stock data saved to %s.", file)
    except IOError as e:
        logging.error("Could not save data to %s: %s", file, e)

def print_data(stock_data):
    """Prints a formatted report of all items in stock."""
    print("--- Items Report ---")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")
    print("--------------------")

def check_low_items(stock_data, threshold=5):
    """Checks for items at or below a given threshold."""
    result = []
    for item in stock_data:
        if stock_data[item] < threshold:
            result.append(item)
    if result:
        logging.warning("Low stock items (<= %s): %s", threshold, result)
    return result

def main():
    """Main function to run the inventory system."""

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("inventory.log"),
            logging.StreamHandler()
        ]
    )

    logging.info("--- Inventory System Start ---")


    stock_data = load_data()


    add_item(stock_data, "apple", 10)
    add_item(stock_data, "banana", -2)

    add_item(stock_data, 123, "ten")

    remove_item(stock_data, "apple", 3)
    remove_item(stock_data, "orange", 1)

    print(f"Apple stock: {get_qty(stock_data, 'apple')}")
    print(f"Low items: {check_low_items(stock_data)}")

    save_data(stock_data)
    print_data(stock_data)

    logging.info("--- Inventory System End ---")


if __name__ == "__main__":
    main()
