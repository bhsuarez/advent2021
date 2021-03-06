import loader

if __name__ == '__main__':
    directions = loader.load_advent_input_as_dict('2.txt')
    horizonal = 0
    depth = 0
    count = 0
    aim = 0
    while count < len(directions):
        direction = directions[count].split(" ")
        if direction[0] == 'down':
            aim += int(direction[1])
        elif direction[0] == 'forward':
            horizonal += int(direction[1])
            depth += aim*int(direction[1])
        elif direction[0] == 'up':
            aim -= int(direction[1])
        print(f"moving {directions[count]}")
        count+=1
    print(f"Horizonal total: {horizonal}")
    print(f"Depth total: {depth}")
    print(f"Answer: {depth*horizonal}")