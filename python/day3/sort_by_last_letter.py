# Task: define a function that takes a string as input parameter. Defines a
# local function that returns the last letter of the string. Your main
# function returns a sorted list based on the last letter.


store = list()

def sort_by_last_letter(strings):
    """
    Sorts input list by last letter
    :param strings: list of strings
    :return: returns list sorted by last letter
    """

    # Local function
    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(last_letter)
    return sorted(strings, key=last_letter)


def logger(msg):
    def log_message():
        print("Log:", msg)
    return log_message


def html_tag(tag):
    """
    creates an HTML tag based on input
    :param tag: desired tag
    :return: callable function
    """
    def wrap_text(msg):
        print("<{0}>{1}></{0}>".format(tag, msg))

    return wrap_text

def main():
    strings = ["one", "two", "three", "four"]
    print(sort_by_last_letter(strings))


if __name__ == "__main__":
    main()
