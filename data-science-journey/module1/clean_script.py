def mean_ignore_none(values : list[float | None]) -> float:
    """Return the arithmetic mean of a list of numbers, ignoring None values.

    arguments:
        values: list of numbers, some of which may be None
    
    returns:
        the mean of the non-None values, or 0 if there are no non-None values
    """
    somme = 0
    nombre = 0
    for extra in values:
        if extra is not None:
            somme = somme + extra
            nombre = nombre + 1
    if nombre == 0:
        return 0
    return somme / nombre


def filter_above(values : list[float | None], t : float) -> list[float]:
    """Return a list of values above a threshold.

    arguments:
        values: list of numbers
        t: threshold

    returns:        
        a list of values from the input that are above the threshold
    """
    r = []
    for extra in values:
        extra = extra if extra is not None else 0
        if extra > t:
            r.append(extra)
    return r


def main():
    data = [10, 20, None, 30, None, 40, 50]
    print("moyenne:", mean_ignore_none(data))
    print("sup a 25:", filter_above([extra for extra in data if extra is not None], 25))

if __name__ == "__main__":
    main()