def sum_of_list(num_list):
    """
    This is to demonstrate some basic notions of debugging using pdb.

    Toy implementation of summing a list of numbers.  Unfortunately, it's
    crashing when we run it.
    """
    sum = 0

    # In the real world, use the sum() function instead.
    for i in num_list:
        sum += step_in(i)

    print(f"And the sum is... {sum}")


def step_in(num):
    """
    I don't do anything, I'm just here to demonstrate stepping in.
    """
    return num


if __name__ == "__main__":
    sum_of_list([2, 3, 5, "7", 9, 11, "13", 17])
