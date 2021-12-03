import loader

if __name__ == '__main__':
    measurements = loader.load_advent_input_as_dict('1.txt')
    increase_count = 0

    if measurements[2] > measurements[111]:
        print("I don't know")

    print("Number of increases: "+str(increase_count))
