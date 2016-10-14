from collections import Counter
import matplotlib.pyplot as plt
import csv


def manhattan(rating1, rating2):
    """Computes the Manhattan distance. Both rating1 and rating2 are
        dictionaries of the form
        {'The Strokes': 3.0, 'Blue Streak': 2.5 ...}"""
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
    return distance

def calculate_mean(list_of_numbers):
    """
    Calculates the mean from a list of numbers
    :rtype : object
    """
    sum_of_numbers = sum(list_of_numbers)
    count_of_numbers = len(list_of_numbers)
    mean = sum_of_numbers/count_of_numbers
    return mean


def calculate_median(numbers):
    """
    Calculates the median from a list of numbers
    """
    N = len(numbers)
    numbers.sort()
    # Find the median
    if N % 2 == 0:
        # if N is even
        m1 = N/2
        m2 = (N/2) + 1
        # Convert to integer, match position, list index starts from 0 while len starts from 1 ..n
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2])/2
    else:
        m = (N+1)/2
        # Convert to integer, match position
        m = int(m) - 1
        median = numbers[m]
    return median
if __name__ == '__main__':
        donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
        print calculate_mean(donations)




def calculate_mode(numbers):
    '''
    Calculating the mode
    '''
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]
if __name__=='__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    mode = calculate_mode(scores)
    print('The mode of the list of numbers is: {0}'.format(mode))


'''
Frequencies
Calculating the mode when the list of numbers may
have multiple modes
'''
def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]
    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes
if __name__ == '__main__':
    scores = [5, 5, 5, 4, 4, 4, 9, 1, 3]
    modes = calculate_mode(scores)
    print('The mode(s) of the list of numbers are:')
    for mode in modes:
        print(mode)

"""Frequency table"""
def frequency_table(numbers):
    table = Counter(numbers)
    print('Number\tFrequency')
    for number in table.most_common():
            print('{0}\t{1}'.format(number[0], number[1]))
if __name__=='__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    frequency_table(scores)


'''
Find the range
'''
def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    # Find the range
    r = highest-lowest
    return lowest, highest, r
if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    lowest, highest, r = find_range(donations)
    print('Lowest: {0} Highest: {1} Range: {2}'.format(lowest, highest, r))



def find_differences(numbers):
    # Find the mean
    mean = calculate_mean(numbers)
    # Find the differences from the mean
    diff = []
    for num in numbers:
        diff.append(num-mean)
    return diff


def calculate_variance(numbers):
    # Find the list of differences
    diff = find_differences(numbers)
    # Find the squared differences
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    # Find the variance
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers)
    return variance
if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = calculate_variance(donations)
    print('The variance of the list of numbers is {0}'.format(variance))
    std = variance**0.5
    print('The standard deviation of the list of numbers is {0}'.format(std))


def find_corr_x_y(x,y):
    n = len(x)
    # Find the sum of the products
    prod = []
    for xi, yi in zip(x,y):
        prod.append(xi*yi)
    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2
    x_square = []
    for xi in x:
        x_square.append(xi**2)
    # Find the sum
    x_square_sum = sum(x_square)
    y_square=[]
    for yi in y:
        y_square.append(yi**2)
    # Find the sum
    y_square_sum = sum(y_square)
    # Use formula to calculate correlation
    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1*denominator_term2)**0.5
    correlation = numerator/denominator
    return correlation
if __name__ == '__main__':
    x = [1, 2, 3, 4]
    y = [2, 4, 6, 8]
    print "Correlation ||||==>", find_corr_x_y(x,y)


# Find the sum of numbers stored in a file
def sum_data(filename):
    s = 0
    with open(filename) as f:
        for line in f:
            s = s + float(line)
        print('Sum of the numbers =====>: {0}'.format(s))
if __name__ == '__main__':
        sum_data('../res/test_data.txt')

'''
Calculating the mean of numbers stored in a file
'''
def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
         numbers.append(float(line))
    return numbers

if __name__ == '__main__':
    data = read_data('../res/test_data.txt')
    mean = calculate_mean(data)
    print('Mean: {0}'.format(mean))


def scatter_plot(x, y):
    plt.scatter(x, y)
    plt.xlabel('X-Axis')
    plt.ylabel('Correlation')
    plt.show()


# def read_csv(filename):
#     numbers = []
#     squared = []
#     with open(filename) as f:
#         reader = csv.reader(f)
#         next(reader)
#         for row in reader:
#             numbers.append(int(row[0]))
#             squared.append(int(row[1]))
#         return numbers, squared
# if __name__ == '__main__':
#     numbers, squared = read_csv('../res/numbers.csv')
#     scatter_plot(numbers, squared)


def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        summer = []
        highest_correlated = []
        for row in reader:
            summer.append(float(row[1]))
            highest_correlated.append(float(row[2]))
    return summer, highest_correlated
if __name__ == '__main__':
    summer, highest_correlated = read_csv('../res/correlate-summer.csv')
    corr = find_corr_x_y(summer, highest_correlated)
    print('Highest correlation********: {0}'.format(corr))
    scatter_plot(summer, highest_correlated)