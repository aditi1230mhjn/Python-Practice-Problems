import math

if __name__ == "__main__":
    n = int(input())
    curr_state = ["44", "55", "66"]
    next_state = []
    all_states = ["44", "55", "66"]
    chars = ["4", "5", "6"]
    count = 3
    while True:
        for i in range(len(chars)):
            for j in range(len(curr_state)):
                num = chars[i] + curr_state[j] + chars[i]
                next_state.append(num)
                all_states.append(num)
                count += 1
                if count == n:
                    print("Nth number is: " + num)
                    print("The entire sequence: " + str(all_states))
                    exit()
        curr_state = next_state
        next_state = []