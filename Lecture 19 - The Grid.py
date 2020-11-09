"""
What do I want to talk about today?

Branching recursion problem, pathfinding.

Start sorting stuff
"""

from random import choice, random, randint

SPACE = '_'
OCCUPIED = 'X'
THE_END = 'E'
THE_START = 'S'


def build_grid(rows, cols, p):
    grid = []

    for i in range(rows):
        grid.append([])
        for j in range(cols):
            if random() < p:
                grid[i].append(SPACE)
            else:
                grid[i].append(OCCUPIED)

    grid[randint(0, rows - 1)][randint(0, cols - 1)] = THE_END
    x = randint(0, rows - 1)
    y = randint(0, cols - 1)
    while grid[x][y] == THE_END:
        x = randint(0, rows - 1)
        y = randint(0, cols - 1)

    grid[x][y] = THE_START

    return grid


def display(the_grid):
    #  wow look at that
    # the_grid = build_grid(10, 10, .75)
    for i in range(len(the_grid)):
        print(' '.join([str(x).ljust(4) for x in the_grid[i]]))


"""
    What do we want to do with this? find an exit.
    make an exit (E)
    
    Robovac recursion is the right way to do it.
    Robovac got stuck in corners when shapes were "bad"
    backtrack
"""


def find_start(the_grid):
    for i in range(len(the_grid)):
        for j in range(len(the_grid[i])):
            if the_grid[i][j] == THE_START:
                # remember that this is a tuple
                return (i, j)
    return None


def find_path(the_grid, current_pos, step=0):
    """
    depth first search
    track through the grid until it finds end, start at the start position
    :param the_grid: the grid
    :return: the path from the start to the end

    consider all possibilities for moves
    """
    # this must be a two element array (list, tuple)
    print('entering', current_pos)
    x, y = current_pos
    display(the_grid)
    if input('continue? ') != 'y':
        # quit is forbidden
        quit()
    if the_grid[x][y] == THE_END:
        # non-recursive case, if we find the end
        return True
    the_grid[x][y] = str(step)
    # go up
    if x - 1 >= 0 and the_grid[x - 1][y] in [SPACE, THE_END]:
        if find_path(the_grid, (x - 1, y), step + 1):
            return True
        print('going up didnt work')
        the_grid[x - 1][y] = "BAD"
    # if not then go left
    if y - 1 >= 0 and the_grid[x][y - 1] in [SPACE, THE_END]:
        if find_path(the_grid, (x, y - 1), step + 1):
            return True
        print('going left didnt work')
        the_grid[x][y - 1] = "BAD"
    # if not then go right
    if y + 1 < len(the_grid[x]) and the_grid[x][y + 1] in [SPACE, THE_END]:
        if find_path(the_grid, (x, y + 1), step + 1):
            return True
        print('going right didnt work')
        the_grid[x][y + 1] = "BAD"
    # else go down
    if x + 1 < len(the_grid) and the_grid[x + 1][y] in [SPACE, THE_END]:
        if find_path(the_grid, (x + 1, y), step + 1):
            return True
        print('going down didnt work')
        the_grid[x + 1][y] = "BAD"

""" to find the shortest path requires a breadth first search """

def breadth_first_search(the_grid):
    """
        think about the problem like this:
        search ALL positions at a distance d before you go to distance d + 1
    :param the_grid:
    :return:
    """
    the_start = find_start(the_grid)
    search_list = [(0, the_start)]

    while search_list:
        depth, (x, y) = search_list[0]
        search_list.remove(search_list[0])

        if (the_grid[x][y] == THE_END):
            print('Found it')
            return

        the_grid[x][y] = depth

        if x - 1 >= 0 and the_grid[x - 1][y] in [SPACE, THE_END]:
            search_list.append((depth + 1, (x - 1, y)))
        if y - 1 >= 0 and the_grid[x][y - 1] in [SPACE, THE_END]:
            search_list.append((depth + 1, (x, y - 1)))
        if y + 1 < len(the_grid[x]) and the_grid[x][y + 1] in [SPACE, THE_END]:
            search_list.append((depth + 1, (x, y + 1)))
        if x + 1 < len(the_grid) and the_grid[x + 1][y] in [SPACE, THE_END]:
            search_list.append((depth + 1, (x + 1, y)))
        # search_list.sort()


if __name__ == '__main__':
    a_grid = build_grid(10, 10, .8)
    display(a_grid)
    # print(find_path(a_grid, find_start(a_grid)))
    breadth_first_search(a_grid)
    display(a_grid)
