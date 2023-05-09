"""Duplicate check for int array.

Different implementations. Array simulated with list.

Author:
    Wolfgang Funk <funk@dhbw-vs.de>
    
"""


def has_duplicate_version_one(a_list):
    """Checks for duplicate in array.

    Args:
        a_list (list): array (simulated with list)
        
    Returns:
        True if array contains duplicate, False otherwise
    
    """
    steps = 0
    for i in range(len(a_list)):
        for k in range(len(a_list)):
            if k != i and a_list[i] == a_list[k]:
                steps += 1                            
                print(steps)
                return True
            if i != k:
                steps += 1
    print(steps)
    return False
    

def has_duplicate_version_two(a_list):
    """Checks for duplicate in array.

    Args:
        a_list (list): array (simulated with list)
        
    Returns:
        True if array contains duplicate, False otherwise
    
    """
    steps = 0
    for i in range(len(a_list)):
        for k in range(i+1, len(a_list)):
            steps += 1
            if a_list[i] == a_list[k]:
                print(steps)
                return True
    print(steps)
    return False
    
    
def has_duplicate_version_three(a_list):
    """Checks for duplicate in array.

    Args:
        a_list (list): array (simulated with list)
        
    Returns:
        True if array contains duplicate, False otherwise
    
    """
    steps = 0
    checked = [False] * (max(a_list) + 1)
    for i in range(len(a_list)):
        steps += 1
        if checked[a_list[i]]:
            print(steps)
            return True
        else:
            checked[a_list[i]] = True
    print(steps)
    return False


if __name__ == "__main__":
    print(has_duplicate_version_one([22, 13, 19, 17, 25]))
    print(has_duplicate_version_one([22, 13, 19, 17, 25, 13]))

    print(has_duplicate_version_two([22, 13, 19, 17, 25]))
    print(has_duplicate_version_two([22, 13, 19, 17, 25, 13]))

    print(has_duplicate_version_three([22, 13, 19, 17, 25]))
    print(has_duplicate_version_three([22, 13, 19, 17, 25, 13]))
