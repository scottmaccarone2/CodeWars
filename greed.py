# Greed is Good
# Instructions: Greed is a dice game played with 5 six-sided dice. Score a
# throw according the rules below. You will always be given an array with
# 5 six-sided dice values

# Rules:
# Three 1's => 1000 points
# Three 6's =>  600 points
# Three 5's =>  500 points
# Three 4's =>  400 points
# Three 3's =>  300 points
# Three 2's =>  200 points
# One   1   =>  100 points
# One   5   =>   50 point

# A single die can only be counted once in each roll. For example, a "5" can
# only count as part of a triplet (contributing to the 500 points) or as a
# single 50 points, but not both in the same roll.

# Example:
 # Throw       Score
 # ---------   ------------------
 # 5 1 3 4 1   50 + 2 * 100 = 250
 # 1 1 1 3 1   1000 + 100 = 1100
 # 2 4 4 5 4   400 + 50 = 450

 # NOTE: Do NOT mutate the input to the function - ever!!

 # The score of [2, 3, 4, 6, 2] should be 0
 # The score of [4, 4, 4, 3, 3] should be 400
 # The score of [2, 4, 4, 5, 4] should be 450
 # The score of [1, 4, 1, 4, 4] should be 600

# def score(dice_list):
    # Go to the first item in the list
        # Count the number of times that item occurs in the list
        # Identify the index at which any additional identical items?
        # If the item occurs 3 times or more
            # Check which number it is
                # points = three_count_points (2, 3, 4, 6)
                # points = three_count_points + single_count_points *
                # count_mod_3
        # Else if the item occurs less than 3 times
            # Check if the number is 1 or 5 (since single_count_points only
            # matter if the value is a 1 or 5)
                # points = single_count_points * count
    # Go to the next item in the list (skipping over any other occurance
    # already accounted for in the preceeding step)


def score(dice_list):
    # initialize an empty dictionary to keep track of each rolled value and
    # how many times that value shows up
    item_count_dict = dict()
    # identify those rolled values which must occur three times in order for
    # those values to count towards earning points
    three_count_only = [2, 3, 4, 6]
    # initialize a variable to keep track of total points scored
    total_points = 0
    # begin the counting process for rolled values
    for item in dice_list:
        if item not in item_count_dict:
            item_count_dict[item] = 1
        elif item in item_count_dict:
            item_count_dict[item] += 1
    # iteratre through the key, value pairs of the dictionary
    # break the cases up into two large categories: if the rolled value occurs
    # at least three times; or if the rolled value occurs less than three times
    for key, value in item_count_dict.items():
        if value >= 3:
        # if the rolled value occurs at least three times, there are cases
            if key in three_count_only:
            # if the number rolled is one of the values that must occur three
            # times to count towards accruing points:
                total_points += key * 100
            elif key not in three_count_only:
            # if the number rolled is a 1 or 5
                remainder = value % 3
                # depending on how many times 1 or 5 shows up, our total points
                # changes
                if key == 1:
                    total_points += 1000 + 100 * remainder
                elif key == 5:
                    total_points += 500 + 50 * remainder
        elif value < 3:
        # if the rolled value occurs less than three times, then the only values
        # that matter (accrue points) are 1 and 5
            if key == 1:
                total_points += 100 * value
            elif key == 5:
                total_points += 50 * value
    print(total_points)


score([2, 3, 4, 6, 2])
score([4, 4, 4, 3, 3])
score([2, 4, 4, 5, 4])
score([1, 4, 1, 4, 4])

# Rated "best practices" top solution
# def score(dice):
#   sum = 0
#   counter = [0,0,0,0,0,0]
#   points = [1000, 200, 300, 400, 500, 600]
#   extra = [100,0,0,0,50,0]
#   for die in dice:
#     counter[die-1] += 1
#
#   for (i, count) in enumerate(counter):
#     sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)
#
#   return sum
