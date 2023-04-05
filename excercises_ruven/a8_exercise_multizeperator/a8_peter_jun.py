_str = ["a", "b", "c"]
_ints = ["1", "2", "3", "4"]


def iterable_to_generator(iterable):
    """
    Takes an iterable and yields one item at a time.
    """
    for item in iterable:
        yield item


def multiziperator(*iterables):
    """
    Takes one or more iterables turns them into a generator.
    """
    min_length = min([len(len_int) for len_int in iterables])
    generators = [iterable_to_generator(iterable) for iterable in iterables]
    for i in range(min_length):
        for generator in generators:
            yield next(generator)
