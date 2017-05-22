import logging
logging.basicConfig(filename="example.log", level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info("Running '{}' with argument {}".format(
            func.__name__, args))

        print(func(*args))

    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def main():
    add_logger = logger(add)
    sub_logger = logger(sub)

    print(add_logger(3, 4))
    print(add_logger(4, 9))
    print(sub_logger(3, 4))
    print(sub_logger(4, 9))



if __name__ == "__main__":
    main()
