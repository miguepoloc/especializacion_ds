from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def show_details(self):
        pass


class Clothing(Product):
    pass

class Electronics(Product):
    pass

class Furniture(Product):
    pass


class TShirt(Clothing):
    def show_details(self):
        print("Details of the T-shirt")

class Pants(Clothing):
    def show_details(self):
        print("Details of the pants")

class Television(Electronics):
    def show_details(self):
        print("Details of the television")

class Sofa(Furniture):
    def show_details(self):
        print("Details of the sofa")


class AbstractFactory(ABC):
    @abstractmethod
    def create_clothing(self):
        pass

    @abstractmethod
    def create_electronics(self):
        pass

    @abstractmethod
    def create_furniture(self):
        pass


class ClothingFactory(AbstractFactory):
    def create_clothing(self):
        return TShirt()

    def create_electronics(self):
        return None

    def create_furniture(self):
        return None

class ElectronicsFactory(AbstractFactory):
    def create_clothing(self):
        return None

    def create_electronics(self):
        return Television()

    def create_furniture(self):
        return None

class FurnitureFactory(AbstractFactory):
    def create_clothing(self):
        return None

    def create_electronics(self):
        return None

    def create_furniture(self):
        return Sofa()


def main():
    clothing_factory = ClothingFactory()
    tshirt = clothing_factory.create_clothing()
    tshirt.show_details()

    electronics_factory = ElectronicsFactory()
    television = electronics_factory.create_electronics()
    television.show_details()

    furniture_factory = FurnitureFactory()
    sofa = furniture_factory.create_furniture()
    sofa.show_details()

if __name__ == "__main__":
    main()