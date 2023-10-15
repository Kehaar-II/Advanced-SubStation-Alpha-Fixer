import sys, os.path

startTimestampOffset = 12
endTimestampOffset = startTimestampOffset + 11

def offsetTimestamp(timestamp, offset):
    '''str, int -> str
    offsets a timestamp in the h:mm:ss.cc format by the given number of milliseconds'''

    hour = int(timestamp[0:1])
    minutes = int(timestamp[2:4])
    seconds = int(timestamp[5:7])
    centiseconds = int(timestamp[8:10])

    offset //= 10 # convertion from milliseconds to centiseconds
    for i in range(offset):
        centiseconds += 1
        if centiseconds > 99:
            centiseconds = 0
            seconds += 1
        if seconds > 59:
            seconds = 0
            minutes += 1
        if minutes > 59:
            minutes = 0
            hour += 1 if hour >= 9 else 9

    print(timestamp)
    print(str(hour) + ":" + str(minutes) + ":" + str(seconds) + "." + str(centiseconds) + "\n")

    return str(hour) + ":" + str(minutes) + ":" + str(seconds) + "." + str(centiseconds)


def main():
    ''' '''
    if (len(sys.argv) == 1):
        return 1
    if (not os.path.isfile(sys.argv[1])):
        return 1
    file = open(sys.argv[1], "r")

    count = 0
    lines = file.readlines()
    for line in lines:
        # print(line[startTimestampOffset:], end = '')
        # print(line[endTimestampOffset:])

        if count >= 39:
            offsetTimestamp(line[startTimestampOffset:startTimestampOffset + 10], 100)
        count += 1

    return 0

exit(main())
