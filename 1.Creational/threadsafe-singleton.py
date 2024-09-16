from threading import Lock , Thread


class SingletonMeta(type):

    _instances = {}

    _lock: Lock = Lock()
    """
        we now have a lock object that will be used to synchronize thread
        during first access to the singleton.
    """

    def __call__(cls,*args,**kwargs):
        """  Possible changes to the value of the `__init__` arguments
            do not affect the returned instance.
        """
        # Now , imageine that the program has jus been launched. Since there's no
        # Singleton instance yet , multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            #The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the singleton instance. Once it leaves the
            # lock body, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args,*kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]



class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self,value:str) -> None:
        self.value = value

    def some_business_logic(self):
        pass


def test_singleton(value:str) -> None:
    singleton = Singleton(value)
    print(singleton.value)



if __name__ == "__main__":
    print("If you see the same value, the singleton was reused (yay!!)\n"
          "If you see different values, "
          "then 2 singletons were created (boooo!!) \n\n"
          "Result: \n")

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
