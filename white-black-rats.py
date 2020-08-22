def countWhites(years, rats):
    current_state = [0]*3
    current_state[0] = rats
    while years > 0:
        current_state[2] = current_state[1]
        current_state[1] = current_state[0]
        current_state[0] = (current_state[1]*2 + current_state[2]*3)
        years -= 1
    return sum(current_state)


def countBlacks(years, rats):
    current_state = [0] * 2
    current_state[0] = rats
    while years > 0:
        current_state[1] = current_state[0]
        current_state[0] = (current_state[1]*3)
        years -= 1
    return sum(current_state)


if __name__ == "__main__":
    years, rats = input().split(" ")
    whites = countWhites(int(years), int(rats))
    print(whites)
    blacks = countBlacks(int(years), int(rats))
    print(blacks)
    diff = abs(whites - blacks)
    print(diff)