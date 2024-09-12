from abc import ABC, abstractmethod
# 1. Define Abstract Products

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Checkbox(ABC):

    @abstractmethod
    def paint(self):
        pass



# 2. (a) Define concrete product for windows

class WindowsButton(Button):
    def paint(self):
        return "Rendering a button in Windows style"

class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Redering a Checkbox in Windows style"



# 2. (b) Define concrete product for MacOS

class MacOSButton(Button):
    def paint(self):
        return "Rendering a button in MacOS style."

class MacOSCheckbox(Checkbox):
    def paint(self):
        return "Rendering a checkbox in MacOS style."




#  3. Define an Abstract Factory

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass



# 4. Define Concrete Factories

# 4a windows concrete Factory
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


# 4b macos concrete factory
class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()





# 5 . Client Code


def get_factory(os_type):
    if os_type == "Windows":
        return WindowsFactory()
    elif os_type == "macOS":
        return MacOSFactory()
    else:
        raise ValueError("Unknown OS type")


def client_code(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.paint())
    print(checkbox.paint())

if __name__ == "__main__":
    os_type = input("Enter OS type (Windows/macOS): ")
    factory = get_factory(os_type)
    client_code(factory)
