from abc import ABC, abstractmethod


# 1 . Define the Product Interface

class Logger(ABC):
    @abstractmethod
    def log(self,message:str):
        pass


# 2 . Define Concrete Products

class FileLogger(Logger):
    def log(self,message:str):
        #simulate logging to the console
        return f"Logging to the file: {message}"

class ConsoleLogger(Logger):
    def log(self,message:str):
        return f"Logging to the console: {message}"

# 3 . Define the Creator

class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass

# 4. Define Concrete Creators

class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()

class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()


# 5 . Client Code

def log_message(factory : LoggerFactory , message : str):
    logger = factory.create_logger()
    print(logger.log(message))


if __name__ == "__main__":
    #Use FileLoggerFactory to create a FileLogger
    file_logger_factory = FileLoggerFactory()
    log_message(file_logger_factory,"File log message")

    #Use ConsoleLoggerFactory to create a ConsoleLogger
    console_logger_factory = ConsoleLoggerFactory()
    log_message(console_logger_factory,"Console log message")
