from functools import wraps


def decorator_one(inner_function):
    def wrapper(*args, **kwargs):
        print("TEST 1")
        inner_function(*args, **kwargs)
    return wrapper


def decorator_two(inner_function):
    def wrapper(*args, **kwargs):
        print("TEST 2")
        inner_function(*args, **kwargs)

    return wrapper


def decorator_three(line=""):
    def decorator(function):
        def wrapper(*args, **kwargs):
            print(line)
            return function(*args, **kwargs)
        return wrapper
    return decorator


decorator_list = [decorator_one, decorator_two, decorator_three]


@decorator_list[0]
@decorator_list[1]
@decorator_list[2]("THIS IS A LINE")
def print_something():
    print("something!")


use_decorator_one = False


@decorator_list[0] if use_decorator_one else decorator_list[1]
def print_text(text):
    print(text)


if __name__ == "__main__":
    print_something()
    print("-"*80)
    print_text("something")