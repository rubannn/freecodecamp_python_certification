class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Title line
        title = self.name.center(30, "*") + "\n"

        # Ledger lines
        items = ""
        for entry in self.ledger:
            description = entry["description"][:23]
            amount = f"{entry['amount']:.2f}"
            items += f"{description:<23}{amount:>7}\n"

        # Total line
        total = f"Total: {self.get_balance():.2f}"

        return title + items + total


def create_spend_chart(categories):
    # Title
    chart = "Percentage spent by category\n"

    # Calculate total spent per category (withdrawals only)
    spent = []
    total_spent = 0

    for category in categories:
        category_spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                category_spent += -item["amount"]
        spent.append(category_spent)
        total_spent += category_spent

    # Calculate percentages rounded to nearest 10
    percentages = []
    for amount in spent:
        percent = int((amount / total_spent) * 100)
        percent = percent // 10 * 10
        percentages.append(percent)

    # Build bars
    for i in range(100, -1, -10):
        chart += f"{str(i).rjust(3)}|"
        for percent in percentages:
            chart += " o " if percent >= i else "   "
        chart += " \n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical category names
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)

print(create_spend_chart([food, clothing]))
