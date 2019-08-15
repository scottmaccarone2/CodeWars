# Make a program that filters a list of strings and returns a list with only
# your friends name in it. If a name has exactly 4 letters in it, you can be
# sure that it has to be a friend of yours. Otherwise, you can be sure he is
# not.
# EX: Input = ['Ryan', 'Kieran', 'Jason', 'Yous']
# Output = ['Ryan', 'Yous']

if __name__ == "__main__":

    def isFriend(list):
        friends = []
        for names in list:
            if len(names) == 4:
                friends.append(names)
        return friends
