from collections import defaultdict
import json
import operator

# Initialize Dictiionary
mydic = defaultdict(list)

def list_to_dictionary(mylist):
    # Iterating through the list elements and adding it to the dictionary


    # for i in range(len(mylist)): # One way to iterate and add data to dic
    #     mydic[mylist[i][0]].append(mylist[i][1])

    for name, list in mylist: # Another way to iterate and add
        mydic[name].append(list)


    # Sorting the dictionary based on the key alphabets
    sorted_dict = sorted(mydic.items(), key=operator.itemgetter(0))
    return sorted_dict

if __name__ == '__main__':

    # Initializing the list with tuple elements

    mylist = [('John', ('Physics', 80)),
              ('Daniel', ('Science', 90)),
              ('John', ('Science', 95)),
              ('Mark', ('Maths', 100)),
              ('Daniel', ('History', 75)),
              ('Mark', ('Social', 95))]


    sorted_dict = list_to_dictionary(mylist)

    # Prinitng the final sorted dictionary
    print(sorted_dict)