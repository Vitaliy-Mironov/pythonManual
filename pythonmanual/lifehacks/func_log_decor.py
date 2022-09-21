# декоратор логирования вызова функции

def function_start(function):
    def wrapper(*args, **kwargs):
        print(f'Function [{function.__name__}] start..')
        function(*args, **kwargs)

    return wrapper


@function_start
def add(x, y):
    print(x + y)


add(1, 2)
