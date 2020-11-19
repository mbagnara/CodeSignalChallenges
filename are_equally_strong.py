'''
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

Example

    For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be
    areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;

    For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output should be
    areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;

    For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output should be
    areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = false.
'''

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):

    equally_strong = (yourLeft + yourRight) == (friendsLeft + friendsRight)

    if equally_strong:
        equally_strong = False

        if yourLeft == friendsLeft or yourLeft == friendsRight:
            return True

        if yourRight == friendsRight or yourRight == friendsLeft:
            return True

    return equally_strong


yourLeft = 10
yourRight = 15
friendsLeft = 5
friendsRight = 20

print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))
