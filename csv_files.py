import csv

with open('file.csv') as csvFile:
    readCsv = csv.reader(csvFile, delimiter=',')

    dates = []
    colors = []

    for row in readCsv:
        # print(row)
        color = row[3]
        date = row[0]

        # Store all the dates and colors in lists.
        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    try:
        # Get the user's color of choice.
        whatColor = input('What color do you want to know the date for ?\n')

        if whatColor in colors:
            coldex = colors.index(whatColor.lower())

            theDate = dates[coldex]
            print('The date of', whatColor, 'is', theDate)

        else:
            print('Color not found!')

    except Exception as e:
        print(e)

    print('continuing')