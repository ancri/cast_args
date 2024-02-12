def cast(**types):
    """Example:
    
    >>> @cast(arg1=str, arg2=str)
    >>> def concatenate_strings(arg1, arg2):
    >>>    assert isinstance(arg1, str)
    >>>    assert isinstance(arg2, str)
    >>>    return arg1 + arg2
    
    >>> concatenate_strings(123, arg2=456)
    "123456"
    """    
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
