from statistics import mean

if __name__ == '__main__':

    NUMBER_OF_MARKS = 5

    marks = []

    for counter in range(NUMBER_OF_MARKS):
        mark = int(input('Enter next Mark '))
        marks.append(mark)

    highest = max(marks)
    lowest = min(marks)
    average = mean(marks) / NUMBER_OF_MARKS
    
    print()
    print(f'Highest mark: {highest}')
    print(f'Lowest mark: {lowest}')
    print(f'Average mark: {average}')
    
    
