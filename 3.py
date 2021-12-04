import loader

if __name__ == '__main__':
    # power_consumption = gamma_rate * epsilon_rate
    report = loader.load_advent_input_as_dict("3.txt")
    count = 0
    gamma = ""
    first,second,third,fourth,fifth=0,0,0,0,0
    while count < len(report):
        print(report[count])
        first += int(report[count][0])
        second += int(report[count][1])
        third += int(report[count][2])
        fourth += int(report[count][3])
        fifth += int(report[count][4])
        count +=1