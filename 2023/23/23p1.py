import numpy as np
import copy

map = []
with open('small.txt') as file:
    for line in file:
        map.append(list(line.strip()))


class TreeNode():
    def __init__(self, w):
        self.w = w
        self.left = None
        self.right = None


class World():
    def __init__(self, map):
        self.map = map
        self.steps = 0
        self.h, self.w = map.shape
        self.good_to_go = {'.', '<', '>', '^', 'v'}
        self.y, self.x = self.find_start_pos()
        self.map[self.y, self.x] = 'O'
        self.finish_y, self.finish_x = self.find_finish_pos()

    def copy(self):
        return copy.deepcopy(self)

    def find_start_pos(self):
        x = list(self.map[0]).index('.')
        return (0, x)

    def find_finish_pos(self):
        x = list(self.map[self.h-1]).index('.')
        return (self.h-1, x)

    def printmap(self):
        print(f'\nPosition: {self.y}, {self.x}')
        print(f'Possible directions: {self.possible_dirs()}')
        print(f'Steps: {self.steps}\n')
        for row in self.map:
            print(''.join(row))

    def possible_dirs(self):
        result = ''
        if self.y > 0 and self.map[self.y-1, self.x] in self.good_to_go.difference({'v'}):
            result += 'N'
        if self.y < self.h-1 and self.map[self.y+1, self.x] in self.good_to_go.difference({'^'}):
            result += 'S'
        if self.x > 0 and self.map[self.y, self.x-1] in self.good_to_go.difference({'>'}):
            result += 'W'
        if self.x < self.w-1 and self.map[self.y, self.x+1] in self.good_to_go.difference({'<'}):
            result += 'E'
        assert len(result) <= 2
        return result

    def make_step(self, dir):
        if dir == 'N':
            self.y -= 1
        elif dir == 'S':
            self.y += 1
        elif dir == 'W':
            self.x -= 1
        elif dir == 'E':
            self.x += 1
        self.map[self.y, self.x] = 'O'
        self.steps += 1


    def go_to_next_junction(self):
        while True:
            dirs = self.possible_dirs()
            if len(dirs) == 1:
                self.make_step(dirs[0])
                continue
            else:
                break



def golr(root):
    dirs = root.w.possible_dirs()
    assert len(dirs) == 2
    new_node = TreeNode(root.w.copy())
    if root.left == None:
        new_node.w.make_step(dirs[0])
    elif root.right == None:
        new_node.w.make_step(dirs[1])
    new_node.w.go_to_next_junction()
    return TreeNode(new_node.w)



map = np.array(map)
w = World(map)
nodes = []

w.go_to_next_junction()

curr_node = TreeNode(w)
nodes.append(curr_node)

nodes[0].w.printmap()

nodes.append(golr(nodes[0]))

nodes[1].w.printmap()
nodes.append(golr(nodes[1]))
nodes[2].w.printmap()

nodes[0].w.printmap()
