def ft_filter(func, iterable):
    """
    filter(function or None, iterable) --> filter object

    note:   Return an iterator yielding those items of iterable for which
            function(item) is true. If function is None,
            return the items that are true.
    """
    # using Generator Expression (),
    # which is more memory efficient than list comprehension []
    if func is None:
        return (item for item in iterable if item)
    return (item for item in iterable if func(item))
    if func is None:
        # use list comprehension [], then cast it to an iterator
        # this is less memory efficient than using a generator expression
        return iter([item for item in iterable if item])
    return iter([item for item in iterable if func(item)])
