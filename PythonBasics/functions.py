from msilib import sequence


def contains (sequence, item):
    for element in sequence:
        if element == item:
            return True
        return False

sequence = [100,200,300,400]
item = 350

print (contains(sequence, item))