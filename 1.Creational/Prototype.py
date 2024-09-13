import copy

# 1. Define the prototype interface

class Prototype:
    def clone(self):
        raise NotImplementedError("You should implement the clone method.")



# 2. Concrete prototype class 

class ConcretePrototype(Prototype):
    def __init__(self,name):
        self._name = name 

    def __str__(self):
        return f"ConcretePrototype(name={self._name})"

    def clone(self):
        return copy.deepcopy(self)


# 3. client code


def main():
    original = ConcretePrototype("Original")
    print("Original:",original)

    clone1 = original.clone()
    print("Clone1: ",clone1)


    # Modify the clone to show that it is a separate instance

    clone1._name = "Modified Clone"
    print("After modification - original: ",original)
    print("After modification - Clone: " ,clone1)


if __name__ == "__main__":
    main()

