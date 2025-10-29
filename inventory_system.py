import json
import logging
from datetime import datetime
from typing import List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
stock_data = {}

def addItem(item: str = "default", qty: int = 0, logs: Optional[List[str]] = None) -> None:
    """Add item to inventory."""
    if logs is None:
        logs = []
    
    if not isinstance(item, str):
        raise ValueError("Item must be a string")
    if not isinstance(qty, int):
        raise ValueError("Quantity must be an integer")
    
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def removeItem(item: str, qty: int) -> None:
    """Remove item from inventory."""
    try:
        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
    except KeyError as e:
        logging.error(f"Error removing item: {e}")

def getQty(item: str) -> int:
    """Get quantity of an item."""
    return stock_data.get(item, 0)

def loadData(file: str = "inventory.json") -> None:
    """Load inventory data from file."""
    try:
        with open(file, 'r', encoding='utf-8') as f:
            global stock_data
            stock_data = json.load(f)
    except FileNotFoundError:
        stock_data = {}

def saveData(file: str = "inventory.json") -> None:
    """Save inventory data to file."""
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(stock_data, f, indent=2)

def printData() -> None:
    """Print inventory data."""
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def checkLowItems(threshold: int = 5) -> List[str]:
    """Check for low stock items."""
    return [i for i in stock_data if stock_data[i] < threshold]

def main() -> None:
    """Main function."""
    addItem("apple", 10)
    addItem("banana", 5)  # Fixed: positive number
    # addItem(123, "ten")  # Removed problematic line
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()
    print('Safe print used')  # Removed eval

if __name__ == "__main__":
    main()