import os
import sys

def compare(itemtocheck, listagainst):  # this WAS more justifiable as a function back when I was trying to be fancy
    # with efficiency
    for item in listagainst:
        if itemtocheck == item:
            return True
    return False


def main():
    if len(sys.argv[1:]) != 2:
        return "Please pass two arguments in. The first should be the directory to filter, and the second should be the" \
               "file with the list of desired filenames"

    files = os.listdir(sys.argv[1])
    # so I had wanted to improve efficiency
    # somewhat by limiting iterations of the inner loop based on the filename, but I relied on this list being sorted.
    # I could sort it first, but its long, If I want to improve this efficiency, the only really viable option would be
    # a binary search on the small list as a result
    names = []
    for line in open(sys.argv[2]):
        names += [line[0:-1]]
    for file in files:
        if not compare(file, names):
            os.remove("C:\\Users\\cnorton9.UR\\Desktop\\Lincoln Letter Files\\original\\" + file)


main()
