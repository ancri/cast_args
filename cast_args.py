def cast(**types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Cast positional arguments
            args = list(args)  # Convert tuple to list for mutability
            for i, (arg, param) in enumerate(zip(args, func.__code__.co_varnames)):
                if param in types:
                    args[i] = types[param](arg)
            
            # Cast keyword arguments
            for param, type_ in types.items():
                if param in kwargs:
                    kwargs[param] = type_(kwargs[param])
            
            return func(*args, **kwargs)
        return wrapper
    return decorator
