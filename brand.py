class Brand:
    def __init__(self, name, country_of_origin):
        self.name = name
        self.country_of_origin = country_of_origin

    def show_brand(self):
        print(
            f"{self.name}: {self.country_of_origin}")


brand1 = Brand("Witchery", "Australia")
brand1.show_brand()
