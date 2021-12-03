import loader

if __name__ == '__main__':
    measurements = loader.load_advent_input_as_dict('1.txt')
    increase_count = 0

    for measurement in measurements.values():
        if measurement[0] > measurement[3]:
            print(str(measurement) + str(" no previous measurement"))
            last_measurement = measurement

    print("Number of increases: "+str(increase_count))
