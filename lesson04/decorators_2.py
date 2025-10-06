def shout(func):
    def wrapper(name):
        original_result = func(name)
        modified_result = original_result.upper() + '!!!'
        return modified_result
    return wrapper

def greet(name):
    return f'Привет, {name}!'


loud_greet = shout(greet)
print(loud_greet('Анна'))
