from random import randint


def splash():
    print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              Biathlon
              
         a hit or miss game
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

def open():
    return 0

def closed():
    return 1

def is_open(target):
    return target is open()

def is_closed(target):
    return target is closed()

def new_targets():
    return [open(), open(), open(), open(), open()]





def close_target(target, targets):
    targets[target] = closed()
    return targets





#def hits(targets):
#    return targets.count(1)
def hits(targets):
    counter = 0
    for i in targets:
        counter += is_closed(i)
    return counter





#def target_to_string(target):
#    return "* " if is_open(target) else "O "
def target_to_string(target):
    if is_open(target) is True:
        return "* "
    elif is_closed(target) is True:
        return "O "

def targets_to_string(targets):
    return  str(target_to_string(targets[0]) +
                target_to_string(targets[1]) +
                target_to_string(targets[2]) +
                target_to_string(targets[3]) +
                target_to_string(targets[4]))

def view_targets(targets):
    print("\n0 1 2 3 4\n" + targets_to_string(targets))





def random_hit():
    return [True, False][randint(0, 1)]

def shoot(targets, target):
    if random_hit() is True:
        if is_open(targets[target]) is True:
            close_target(target, targets)
            return "Hit on open target"
        elif is_closed(targets[target]) is True:
            return "Hit on closed target"
    else:
        return "Miss"


goal = new_targets()
print(goal)
print(close_target(3, goal))
print(targets_to_string(goal))
view_targets(goal)

print(shoot(goal, 1))
print(shoot(goal, 1))
print(shoot(goal, 1))