#1.Create a Python class called Product with a method get_discount() that returns 0. Write a subclass called Electronics that overrides get_discount() to return 10.
class Product:
    def get_discount(self):
        return 0


class Electronics(Product):
    def get_discount(self):
        return 10


# Create objects
product = Product()
electronic = Electronics()

print("Product Discount:", product.get_discount(), "%")
print("Electronics Discount:", electronic.get_discount(), "%")



#2.Build a class FoodOrder with a method calculate_total() that returns the base price. Create a subclass ZomatoOrder that overrides calculate_total() to add a 5% delivery charge.
class FoodOrder:
    def __init__(self, base_price):
        self.base_price = base_price

    def calculate_total(self):
        return self.base_price


class ZomatoOrder(FoodOrder):
    def calculate_total(self):
        return self.base_price + (self.base_price * 0.05)


# Create object
order = ZomatoOrder(500)

print("Total Amount: ₹", order.calculate_total())



#3.Write a function show_bonus(employee) that takes any object with a bonus() method and prints the result. Test it with two classes: Influencer (bonus returns 2000) and BrandManager (bonus returns 5000), demonstrating polymorphism.
class Influencer:
    def bonus(self):
        return 2000


class BrandManager:
    def bonus(self):
        return 5000


def show_bonus(employee):
    print("Bonus:", employee.bonus())


# Create objects
influencer = Influencer()
manager = BrandManager()

show_bonus(influencer)
show_bonus(manager)



#4.Given this code: class User: def get_status(self): return 'active' class PremiumUser(User): pass. Update PremiumUser to override get_status() so it returns 'premium'. Then, create one User and one PremiumUser and print their statuses.<br><br><em><strong>Hint:</strong> Use the same method name in both classes to override.</em>
class User:
    def get_status(self):
        return "active"


class PremiumUser(User):
    def get_status(self):
        return "premium"


# Create objects
user = User()
premium = PremiumUser()

print("User Status:", user.get_status())
print("Premium User Status:", premium.get_status())