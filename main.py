import math

def binary_search(my_list, target):
    lower_idx = 0
    upper_idx = len(my_list) - 1
    comparisons = 0  # track number of comparisons

    while lower_idx <= upper_idx:
        comparisons = comparisons + 1
        
        mid_idx = math.ceil((lower_idx + upper_idx) / 2) # calculate middle index; ceil function rounds up

        # compare target with value at the middle index
        if my_list[mid_idx] < target:
            print("index " + str(mid_idx) + ": value = " + str(my_list[mid_idx]) + " --> too low!")
            lower_idx = mid_idx + 1 # update lower index
        elif my_list[mid_idx] > target:
            print("index " + str(mid_idx) + ": value = " + str(my_list[mid_idx]) + " --> too high!")
            upper_idx = mid_idx - 1 # update upper index
        else:
            print("index " + str(mid_idx) + ": value = " + str(my_list[mid_idx]) + " --> FOUND!")
            print("number of comparisons: " + str(comparisons))
            return True # target is found, early return true
    
    print("target not in list")
    print("number of comparisons: " + str(comparisons))
    return False # loop ended without returning true, so target not in list


#CHALLENGE PROCEDURE: Write a function, which works almost identically to binary_search(my_list, target), except it works for lists that are sorted in descending order
def binary_search_descending(my_list, target):
    comparisons = 0
    l_index = 0  #lower boundary index
    u_index = len(my_list) - 1  #upper boundary index

    while l_index <= u_index:
        comparisons += 1

        #This lines calculate the middle index for the remaining values
        m_index = (l_index + u_index) / 2
        if(m_index % 2 != 0) and ((l_index + u_index) % 2 == 1):
            m_index = int(m_index + 1)
        elif(m_index % 2 != 0) and ((l_index + u_index) % 1 == 0.5):
            m_index = int(m_index + 0.5)
        m_index = int(m_index)
        
        #This lines compare the middle index value to the target, WITH EDITS FOR DESCENDING LISTS
        if(my_list[m_index] < target):
            print("index " + str(m_index) + ": value = " + str(my_list[m_index]) + " --> too low!")
            u_index = m_index - 1    #if the list is descending and the value is too small, we need to elimate LATER indices
        elif(my_list[m_index] > target):
            print("index " + str(m_index) + ": value = " + str(my_list[m_index]) + " --> too high!")
            l_index = m_index + 1    #if the list is descending and the value is too large, we need to elimate EARLIER indices
        
        #These lines are the same as the above function
        else:
            print("index " + str(m_index) + ": value = " + str(my_list[m_index]) + " --> FOUND!")
            print("number of comparisons: " + str(comparisons))
            return True # target is found, early return true
     
    print("target not in list")
    print("number of comparisons: " + str(comparisons))
    return False # loop ended without returning true, so target not in list



# ---MAIN PROGRAM---

#for PART A
num_listA = [1, 2, 4, 9, 11, 15, 22, 23, 27, 38, 41, 44, 47, 48, 58, 72, 77, 82, 86, 90, 91, 93, 99, 106, 108, 118, 119, 122, 128, 138, 158, 172, 175, 177, 185, 187, 188, 193, 199, 217, 225, 230, 233, 238, 248, 253, 263, 264, 266, 287]
#for PART B
num_list = [1,2,3,3,6,6,6,14,14,14,14,15,15,17,17,20,20,22,24,28,28,28,29,31,31,33,34,34,35,36,37,39,39,43,46,49,50,51,53,53,54,55,55,56,59,64,65,68,68,68,69,70,71,72,72,74,75,76,77,80,80,82,85,86,86,87,88,89,89,90,90,91,91,92,93,94,97,98,98,99,102,104,105,106,108,110,110,112,112,114,115,117,118,119,119,121,123,124,124,125,125,127,128,132,134,138,142,143,145,146,148,149,150,150,150,151,153,156,157,158,158,160,160,162,168,169,171,173,173,176,177,177,178,178,178,179,179,181,181,182,189,189,190,192,193,193,194,195,198,199,200,200,200,200,202,202,202,203,203,204,207,208,209,209,215,215,217,217,218,218,219,220,221,222,223,224,228,229,231,234,235,236,240,240,241,242,243,246,246,247,247,249,251,252,252,253,254,256,256,256,259,261,265,265,265,268,268,271,273,274,274,275,280,282,282,283,284,284,286,286,288,289,292,293,295,298,303,304,304,305,305,307,309,311,312,314,314,316,317,319,319,320,321,322,323,324,324,329,333,333,333,333,333,341,342,345,346,346,347,348,348,349,350,353,354,354,355,355,358,359,360,360,361,362,364,365,369,372,373,376,376,378,378,379,380,381,383,385,385,386,387,389,389,392,394,394,396,397,399,405]
#for PART C
words = ["apple", "big", "carrot", "cram", "dear", "dingo", "dire", "elephant", "ellipse", "frank", "fun", "ginger", "grade", "graduate", "ice cream", "icky", "jingle", "juggle", "kangaroo", "kazoo", "kite", "koala", "lion", "lone", "magic", "mango", "mississippi", "mystify", "need", "nod", "nun", "oh", "omen", "paper", "pepper", "peppy", "popper", "poppy", "puppy", "quit", "quit", "rail", "ring", "roll", "saucy", "tame", "taunt", "violin", "waiter", "water", "yaaas!", "zebra", "zzz"]


# write your test code FOR PART A:
"""
print(binary_search(num_listA, 99))   #Prints True or False depending on whether the number 99 is found in the list
print(binary_search(num_listA, 72)) 
print(binary_search(num_listA, 238)) 
print(binary_search(num_listA, 1))    #Prints that 1, the first element in the list, is in the list
print(binary_search(num_listA, 287))    #Prints that 287, the final element in the list, is in the list
print(binary_search(num_listA, 250)) 
print(binary_search(num_listA, 14)) 
"""

# test code FOR PART B:
"""
print(binary_search(num_listB, 323))
print(binary_search(num_listB, 97)) 
print(binary_search(num_listB, 333))   #Prints True or False like above, but this number appears multiple times in the list!
print(binary_search(num_listB, 191)) 
"""

# test code FOR PART C: 
"""
print(binary_search(words, "fun"))   #Prints True or False depending on whether the word "fun" is found in the list
print(binary_search(words, "water"))
print(binary_search(words, "mississippi"))
print(binary_search(words, "queen"))
"""

# test code FOR CHALLENGE
descending = [50, 48, 44, 39, 34, 33, 31, 29, 25, 25, 22, 21, 18, 14, 13, 13, 10, 8, 5, 3, 2, 1]

print(binary_search_descending(descending, 50))   #Prints True or False depending on whether 50, the first digit is found in the list
print(binary_search_descending(descending, 1))   #last digit in the list
print(binary_search_descending(descending, 21))   #digit in the middle of the list
print(binary_search_descending(descending, 27))   #value NOT in the list