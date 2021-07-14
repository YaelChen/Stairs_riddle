
def stairs(stair):
    """
    a function to simply find the answer for: "1000 people are climbing an infinite staircase, all start at 0 and some
    go up one stair each turn. in each turn are going up only the people that are divisible by the turn number (1,2,3...
    2,4,6... 3,6,9...etc) and this continues for 1000 turns. how many people are on stair no.3?" (any n in this function)
    :param stair: stair number to check how many people finished on.
    :type stair: int
    :return nth: number of people that finish on the nth stair.
    :rtype nth: int
    """
    locations = 1000 * [0]
    for turn in range(1, 1001):
        for person in range(1, 1001):
            if person % turn == 0:
                locations[person - 1] += 1

    # print(locations)
    # by sorting the locations list we can also easily find a highest stair reached and other parameters:
    # print(sorted(locations))

    # to find the numbers that finish on nth stair, so you can find the logic connection between them:
    numbers = []
    for i in range(1000):
        if locations[i] == stair:
            numbers.append(i + 1)
    print(numbers)
    # so all PRIME NUMBER will finish at 2nd floor (because they divides two times; by 1 and themselves)
    # and all PRIME NUMBER ** 2 will finish at 3nd floor (because they divides 3 times)

    nth = locations.count(stair)
    return nth


print(stairs(3))
