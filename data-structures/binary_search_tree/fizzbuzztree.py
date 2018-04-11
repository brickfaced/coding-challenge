def fizzbuzztree(node):
    """
    Goes through each node in a binary search tree and sets node values to
    either Fizz, Buzz, FizzBuzz or skips through them depending if they're
    divisible by 3, 5 or both. The best way to use this function is to
    apply it to a traversal method. For example: BST.in_order(fizzbuzztree)
    """
    if node.val % 3 == 0 and node.val % 5 == 0:
        node.val = 'FizzBuzz'
        return

    if node.val % 5 == 0:
        node.val = 'Buzz'
        return

    if node.val % 3 == 0:
        node.val = 'Fizz'
        return

    else:
        pass

    return
