from abc import ABC, abstractmethod


# Abstract Product Interfaces
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


# Concrete Products for Light Theme
class LightButton(Button):
    def paint(self):
        print("Painting a light-themed button")


class LightCheckbox(Checkbox):
    def paint(self):
        print("Painting a light-themed checkbox")


# Concrete Products for Dark Theme
class DarkButton(Button):
    def paint(self):
        print("Painting a dark-themed button")


class DarkCheckbox(Checkbox):
    def paint(self):
        print("Painting a dark-themed checkbox")


# Abstract Factory Interface
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# Concrete Factory for Light Theme
class LightThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()


# Concrete Factory for Dark Theme
class DarkThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()


# Client Code
def client(factory: UIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.paint()
    checkbox.paint()


if __name__ == "__main__":
    # Usage
    print("Using Light Theme:")
    client(LightThemeFactory())

    print("\nUsing Dark Theme:")
    client(DarkThemeFactory())
