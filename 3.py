import loader

if __name__ == '__main__':
    # power_consumption = gamma_rate * epsilon_rate
    report = loader.load_advent_input_as_dict("3.txt")
    count = 0
    gamma = ""
    while count < len(report):
        for digit in len(report[count]):
            print(report[digit])
        count +=1