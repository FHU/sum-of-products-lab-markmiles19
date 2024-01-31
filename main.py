#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    math_sum = 0
    for i in range(len(list1)):
        math_sum += (int(list1[i]) * int(list2[i]))
    return math_sum

if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    in1 = (input()).replace(' ', '')
    in2 = (input()).replace(' ', '')
    if len(in1) == len(in2):
        result = sum_of_products(in1, in2)
        print(result)
    else:
        print('Error.')
