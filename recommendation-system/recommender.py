from utils.manhattan import manhattan

__author__ = 'harry'
"""
Solution based on the idea  that birds of the same feather flock together,
in other words, similar people tend to like similar things.
Similarity can be likes, habits etc in this lab, we use movie ratings of 'closest neighbors'
to recommend movies to similar customers


Example usage:
>>> recommend('Hailey', users)
[('Phoenix', 4.0), ('Blues Traveler', 3.0), ('Slightly Stoopid', 2.5)]
>>> recommend('Chan',users)
[('The Strokes', 4.0), ('Vampire Weekend', 1.0)]
>>> recommend('Sam',users)
[('Deadmau5', 1.0)]
>>> recommend('Angelica',users)
[]
>>>
"""


def compute_nearest_neighbor(username, users):
    """creates a sorted list of users based on their distance to
    username"""
    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))
    # default sort based on index 0 of tuples ie distance --> closest first ie ascending order
    distances.sort()
    return distances


def recommend(username, users):
    """Give list of recommendations"""
    # first find nearest neighbor
    nearest = compute_nearest_neighbor(username, users)[0][1]
    recommendations = []
    # now find bands neighbor rated that user didn't
    neighbor_ratings = users[nearest]
    user_ratings = users[username]
    for artist in neighbor_ratings:
        if artist not in user_ratings:
            recommendations.append((artist, neighbor_ratings[artist]))
            # using the function sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda artist_tuple: artist_tuple[1],
                  reverse=True)


if __name__ == "__main__":
    users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0,
                          "Norah Jones": 4.5, "Phoenix": 5.0,
                          "Slightly Stoopid": 1.5,
                          "The Strokes": 2.5, "Vampire Weekend": 2.0},
             "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5,
                      "Deadmau5": 4.0, "Phoenix": 2.0,
                      "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
             "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0,
                      "Deadmau5": 1.0, "Norah Jones": 3.0,
                      "Phoenix": 5, "Slightly Stoopid": 1.0},
             "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0,
                     "Deadmau5": 4.5, "Phoenix": 3.0,
                     "Slightly Stoopid": 4.5, "The Strokes": 4.0,
                     "Vampire Weekend": 2.0},
             "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0,
                        "Norah Jones": 4.0, "The Strokes": 4.0,
                        "Vampire Weekend": 1.0},
             "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0,
                        "Phoenix": 5.0, "Slightly Stoopid": 4.5,
                        "The Strokes": 4.0, "Vampire Weekend": 4.0},
             "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0,
                     "Norah Jones": 3.0, "Phoenix": 5.0,
                     "Slightly Stoopid": 4.0, "The Strokes": 5.0},
             "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0,
                          "Phoenix": 4.0, "Slightly Stoopid": 2.5,
                          "The Strokes": 3.0}}

    """
    change from Hailey to any user in the test data i.e users dictionary
    that you'd like to make a recommendation for e.g to make recommendations for user  Sam, type as below
    recommend('Sam', users)
    """
    print 'Nile Movie Rental\n' \
          '------------------'
    continue_condition = True
    while continue_condition:
        user_to_recommend_movies = raw_input('Enter the customer name to recommend movies: ')
        print '\nRecommended movies for {c} are:\n'.format(c=user_to_recommend_movies), [cust[0] for cust in recommend(user_to_recommend_movies, users)]
        user_response = raw_input('Press y continue or n to quit ')

        if user_response not in ['y', 'Y', 'n', 'N']:
            print 'Please enter y or n.'
            continue
        if user_response == 'y' or user_response == 'Y':
            continue_condition = True
        if user_response == 'n' or user_response == 'N':
            continue_condition = False
            print 'Bye!'