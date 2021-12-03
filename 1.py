import loader

if __name__ == '__main__':
    measurements = loader.load_advent_input_as_dict('1.txt')
    increase_count = 0
    count = 2
    last_sum = 0
    while count < len(measurements):
        sum = int(measurements[count]) + int(measurements[count+1]) + int(measurements[count+2])
        count += 1
        if last_sum == 0:
            print(f"Round {count}: "+str(sum)+" no previous sum")
            last_sum = sum
        else:
            if sum > last_sum:
                print(f"Round {count}: {sum} (increase)")
                increase_count += 1
            elif sum == last_sum:
                print(f"Round {count}: {sum} (no change)")
            else:
                print(f"Round {count}: {sum} (decrease)")
            last_sum = sum
    print("Number of increases: "+str(increase_count))
