[Python Certification](https://www.freecodecamp.org/learn/python-v9/)

## 1. Build a User Configuration Manager
In this lab, you will build a User Configuration Manager that allows users to manage their settings such as theme, language, and notifications. You will implement functions to add, update, delete, and view user settings.

1. You should define a function named `add_setting` with two parameters representing a dictionary of settings and a tuple containing a key-value pair

2. `add_setting` function should:

   - Convert the key and value to lowercase.
   - If the key setting exists, return `Setting '[key]' already exists! Cannot add a new setting with this name.`
   - If the key setting doesn't exist, add the key-value pair to the given dictionary of settings and return `Setting '[key]' added with value '[value]' successfully!.`
   - The messages returned should have the key and value in lowercase.

3. You should define a function named `update_setting` with two parameters representing a dictionary of settings and a tuple containing a key-value pair.

4. `update_setting` function should:

   - Convert the key and value to lowercase.
   - If the key setting exists, update its value in the given dictionary of settings and return: `Setting '[key]' updated to '[value]' successfully!`
   - If the key setting doesn't exist, return `Setting '[key]' does not exist! Cannot update a non-existing setting.`
   - The messages returned should have the key and value in lowercase.

5. You should define a function named `delete_setting` with two parameters representing a dictionary of settings and a key.

6. `delete_setting` function should:

   - Convert the key passed to lowercase.
   - If the key setting exists, remove the key-value pair from the given dictionary of settings and return Setting '[key]' deleted successfully!
   - If the key setting does not exist, return Setting not found!
   - The messages returned should have the key in lowercase.

7. You should define a function named view_settings with one parameter representing a dictionary of settings.

8. view_settings function should:

   - Return No settings available. if the given dictionary of settings is empty.

   - If the dictionary contains any settings, return a string displaying the settings. The string should start with `Current User Settings:` followed by the key-value pairs, each on a new line and with the key capitalized. For example, `view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})` should return:

```
Current User Settings:
Theme: dark
Notifications: enabled
Volume: high
```

## 2. Build a Budget App
In this lab, you will build a simple budget app that tracks spending in different categories and can show the relative spending percentage on a graph.

1. You should have a `Category` class that accepts a name as the argument.

2. The `Category` class should have an instance attribute ledger that is a list, and contains the list of transactions.

3. The `Category` class should have the following methods:

   - A `deposit` method that accepts an amount and an optional description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.
   - A `withdraw` method that accepts an amount and an optional description (default to an empty string). The method should store in ledger the amount passed in as a negative number, and should return True if the withdrawal succeeded and False otherwise.
   - A `get_balance` method that returns the current category balance based on ledger.
   - A `transfer` method that accepts an amount and another Category instance, withdraws the amount with description Transfer to [Destination], deposits it into the other category with description Transfer from [Source], where [Destination] and [Source] should be replaced by the name of destination and source categories. The method should return True when the transfer is successful, and False otherwise.
   - A `check_funds` method that accepts an amount and returns False if it exceeds the balance or True otherwise. This method must be used by both the withdraw and transfer methods.

4. When a Category object is printed, it should:

   - Display a title line of 30 characters with the category name centered between `*` characters.
   - List each `ledger` entry with up to 23 characters of its description left-aligned and the amount right-aligned (two decimal places, max 7 characters).
   - Show a final line Total: [balance], where [balance]` should be replaced by the category total.

Here is an example usage:
```python
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
```

And here is an example of the output:

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

## 3. Build a Polygon Area Calculator
In this project, you will use object-oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit its methods and attributes.

1. You should create a Rectangle class.

2. When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:

    - `set_width`: Sets the width of the rectangle.
    - `set_height`: Sets the height of the rectangle.
    - `get_area`: Returns area ($\text{width} \times \text{height}$).
    - `get_perimeter`: Returns perimeter $2(\text{width} + \text{height})$.
    - `get_diagonal`: Returns diagonal $\sqrt{\text{width}^2 + \text{height}^2}$.
    - `get_picture`: Returns a string that represents the shape using lines of *. The number of lines should be equal to the - height and the number of * in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: `Too big for picture..`
    - `get_amount_inside`: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of `4` and a height of `8` could fit in two squares with sides of `4`.

3. If an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10).

4. You should create a Square class that subclasses Rectangle.

5. When a Square object is created, it should be initialized with a single side length. The __init__ method should store the side length in both the width and height attributes from the Rectangle class.

6. The Square class should contain the following methods:

   - `set_width`: Overrides the set_width method from the Rectangle class. It should set the width and height to the side length.
   - `set_height`: Overrides the set_height method from the Rectangle class. It should set the width and height to the side length.
   - `set_side`: Sets the height and width of the square equal to the side length.

1. The Square class should be able to access the Rectangle class methods.

2. If an instance of a Square is represented as a string, it should look like: Square(side=9).

Usage example
```python
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```

That code should return:

```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```


## 4. Build a Hash Table
In this lab, you will build a hash table from scratch. A hash table is a data structure that stores key-value pairs. A hash table works by taking the key as an input and then hashing this key according to a specific hashing function.

For the purpose of this lab, the hashing function will be simple: it will sum the Unicode values of each character in the key. The hash value will then be used as the actual key to store the associated value. The same hash value would also be used to retrieve and delete the value associated with the key.

1. You should define a class named `HashTable` with a collection attribute initialized to an empty dictionary when a new instance of `HashTable` is created. The collection dictionary should store key-value pairs based on the hashed value of the key.

2. The `HashTable` class should have four instance methods: `hash`, `add`, `remove`, and `lookup`.

3. The `hash` method should:

   - Take a string as a parameter.
   - Return a hashed value computed as the sum of the Unicode (ASCII) values of each character in the string. You can use the `ord` function for this computation.

4. The `add` method should:

   - Take two arguments representing a key-value pair, and compute the hash of the key.
   - Use the computed hash value as a key to store a dictionary containing the key-value pair inside the collection dictionary.
   - If multiple keys produce the same hash value, their key-value pairs should be stored in the existing nested dictionary under the same hash value.

5. The `remove` method should:

   - Take a key as its argument and compute its hash.
   - Confirm if the key exists in the collection.
   - Remove the corresponding key-value pair from the hash table.
   - If the key does not exist in the collection, it should not raise an error or remove anything.

6. The `lookup` method should:

   - Take a key as its argument.
   - Compute the hash of the key, and return the corresponding value stored inside the hash table.
   - If the key does not exist in the collection, it should return None.


## 5. Implement the Tower of Hanoi Algorithm
In this lab, you will solve the mathematical puzzle known as the Tower of Hanoi. The puzzle consists of three rods and a number of disks of different diameters.

1. You should have a function named `hanoi_solver` that takes an integer representing the total number of disks of the puzzle as the argument.
2. The `hanoi_solver` function should solve the puzzle following the given rules in $2^n - 1$ moves, where n is the total number of disks.

3. The `hanoi_solver` function should return a string with all the moves taken to solve the puzzle, including the starting arrangement, with each move on a new line. Rods should be represented as lists of integers, (the smallest disk is represented by the number `1`) with each rod separated by a space. For example, `hanoi_solver(3)` should return the following:
```
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]
```
