"""A tiny corner-store app used for a Git skills demonstration.

Nothing here is meant to be complex. The file exists purely to give you
something small and readable to branch, edit, commit, and merge -- the
point of the exercise is the Git workflow, not the code.
"""

import argparse

STORE_NAME = "Corner Store"
OPENING_HOURS = "9am - 6pm"

# Each entry is "product": price (in USD).
MENU = {
    "coffee": 13.0,
    "tea": 3.00,
    "bagel": 2.50,
    "muffin": 5.50,
    # Add new products here
}

INVENTORY = {
    "coffee": 38,
    "tea": 15,
}


def greet_customer():
    """Print a short welcome message using the store's name and hours."""
    print(f"Welcome to {STORE_NAME}! We're open {OPENING_HOURS}.")


def print_menu():
    """Print each menu item, its price, and how many are available.

    Not every menu item is necessarily tracked in INVENTORY (e.g. a
    newly added item might not have stock recorded yet) -- those are
    shown as "not tracked" rather than assumed to be zero or unlimited.
    """
    for item, price in MENU.items():
        available = INVENTORY.get(item)
        stock = "not tracked" if available is None else f"{available} available"
        print(f"{item}: ${price:.2f} ({stock})")


def restock(item, quantity):
    """Add `quantity` units of `item` to the inventory."""
    INVENTORY[item] = INVENTORY.get(item, 0) + quantity
    return INVENTORY[item]


def main():
    """Entry point. Run with --help (or -h) to see usage."""
    parser = argparse.ArgumentParser(
        prog="store.py",
        description="A tiny corner-store CLI used for a Git skills demonstration.",
        epilog="With no options, greets the customer and prints the menu.",
    )
    parser.add_argument(
        "--restock",
        nargs=2,
        metavar=("ITEM", "QUANTITY"),
        help="Add QUANTITY units of ITEM to the inventory and print the new total.",
    )
    args = parser.parse_args()

    if args.restock:
        item, quantity = args.restock
        new_total = restock(item, int(quantity))
        print(f"Restocked {item}: now {new_total} in stock.")
        return

    greet_customer()
    print_menu()


if __name__ == "__main__":
    main()
