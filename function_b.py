# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    silly_sum = 0
    while silly_sum < 1000 or num == 0:
        num = int(input('Enter a number to add to the sum,\n hit 0 to quit\n'))
        silly_sum += num
        print(f'The sum is now {silly_sum}')

    
    print('gbye!')

if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
