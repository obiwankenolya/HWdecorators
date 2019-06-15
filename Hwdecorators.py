import datetime

data = [1, '5', 'abc', 20, '2']


def logger_path(path):
    def logger(old_function):
        def new_function(*args, **kwargs):
            dt = datetime.datetime.now()
            func_name = old_function.__name__
            func = old_function(*args, **kwargs)
            with open(path, 'w') as f:
                f.write(str(dt))
                f.write(' ')
                f.write(func_name)
                f.write(' ')
                args_list = [value for key, value in kwargs.items()]
                f.write(str(args_list))
                f.write(' ')
                f.write(str(func))
            return dt, func_name, args_list, func
        return new_function
    return logger


@logger_path('log.txt')
def square(data):
    for item in data:
        if type(item) == int:
            result = item ** 2
            yield result
        elif item.isdigit() == True:
            result = int(item) ** 2
            yield result
        else:
            pass


square(data)
