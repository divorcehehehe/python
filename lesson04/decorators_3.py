from functools import wraps

def shout(func):
    @wraps(func)
    def wrapper(name):
        original_result = func(name)
        modified_result = original_result.upper() + '!!!'
        return modified_result
    return wrapper

@shout
def greet(name):
    """Приветствует пользователя."""
    return f'Привет, {name}!'


print(greet('Анна'))
# print(greet.__name__)
# print(greet.__doc__)
