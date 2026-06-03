import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

food = Category("Food", 5000)
travel = Category("Travel", 3000)
shopping = Category("Shopping", 4000)

food.spent = 4500
travel.spent = 3500
shopping.spent = 2500

categories = [food, travel, shopping]

for category in categories:
    if category.spent > category.limit:
        print(f"Alert: {category.name} budget exceeded!")

labels = [c.name for c in categories]
amounts = [c.spent for c in categories]

plt.pie(amounts, labels=labels, autopct="%1.1f%%")
plt.title("Monthly Budget Usage")
plt.show()