def add_sprinkles(func):
    def wrapper():
        print("You add sprinkles ***")
        func()
    return wrapper

@add_sprinkles
def get_ice_cream(flavor):
    print(f"here is your {flavor} ice cream🍨🍦")

get_ice_cream("ege") 