# Intersection of sets

We use `&` operator to find the intersection of two sets. The output of the intersection is also a set.

For example:

```python
fruits = {"Apple", "Banana", "Grapes", "Orange"}
colors = {"Red", "Black", "Orange", "Green"}

print(fruits & colors)

# Output: {'Orange'}
```

## A real world example

Let's say you have a grocery list of fruits and vegetables that you want to buy. You want to check if any of the items on your list match with the items that your local grocery store has in stock.

You could represent your grocery list and the store's inventory using sets in Python. You can use the intersection operation to find the common/available items.

For example:

```python
grocery_list = {"Apple", "Banana", "Spinach", "Carrot", "Tomato"}
store_inventory = {"Apple", "Banana", "Kale", "Carrot", "Lettuce"}

common_items = grocery_list & store_inventory

print("The items you can buy from the store are:")
for item in common_items:
    print("-", item)
```

In this example, `grocery_list` represents the items that you want to buy and store_inventory represents the items that the store has in stock. We use the `&` operator to find the intersection of the two sets, which gives us the common items in both sets.

The output of the program will be:

```python
The items you can buy from the store are:
- Banana
- Carrot
- Apple
```

The intersection of the two sets gives us the items that are common to both sets, which in this case are "Banana", "Carrot", and "Apple". These are the items that you can buy from the store.
