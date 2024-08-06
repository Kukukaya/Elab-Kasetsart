# Example Test Case 1

# 3
# G.E
# ...
# ...
# 1

# Example Test Case 2

# 5 
# G...E
# .....
# .....
# E....
# .....
# 0

# Example Test Case 3

# 7
# G.E...E
# E......
# ......G
# .......
# ....E..
# .......
# E......
# 4


def inputArea(n):
    list_area = []
    for i in range(n):
        oneline_area = list(input(""))
        list_area.append(oneline_area)
    return list_area

def explosiveFinder(m):
    x_axis = 0
    y_axis = 0
    bombpin_y = []
    bombpin_x = []
    bomb_count = 0
    # check = False
    for i in m:
        # if check == True:
        #     break
        x_axis = 0
        y_axis += 1
        for j in i:
            x_axis += 1
            if j == 'G':
                bombpin_y.append(y_axis)
                bombpin_x.append(x_axis)
                bomb_count += 1
                # check = True
                # break
    return bombpin_y,bombpin_x,bomb_count

def manFinder(m):
    x_axis = 0
    y_axis = 0
    bombpin_y = []
    bombpin_x = []
    man = 0
    # check = False
    for i in m:
        # if check == True:
        #     break
        x_axis = 0
        y_axis += 1
        for j in i:
            x_axis += 1
            if j == 'E':
                bombpin_y.append(y_axis)
                bombpin_x.append(x_axis)
                man += 1
                # check = True
                # break
    return bombpin_y,bombpin_x,man

def casualtyonhit(m):
    y_bp,x_bp,bomb = explosiveFinder(m)
    y_man,x_man,man = manFinder(m)
    victim_count = 0
    b = []
    for j in range(bomb):
        y_count = -2
        x_count = -2
        while y_count <= 2:
            x_count = -2
            while x_count <= 2:
                cb = [y_bp[j]+y_count,x_bp[j]+x_count]
                b.append(cb)
                x_count += 1
            y_count += 1
    for i in range(man):
        m = [y_man[i],x_man[i]]
        if m in b:
            victim_count += 1
    return victim_count


n_area = int(input(""))
area = inputArea(n_area)
print(casualtyonhit(area))

