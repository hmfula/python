
def manhattan(rating1, rating2):
    """Computes the Manhattan distance. Both rating1 and rating2 are
        dictionaries of the form
        {'The Strokes': 3.0, 'Blue Streak': 2.5 ...}"""
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
    return distance

