import sys, os.path

startTimestampOffset = 12
endTimestampOffset = 23

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

    return str(hour).zfill(1) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2) + "." + str(centiseconds).zfill(2)


def main():
    ''' '''
    if (len(sys.argv) < 4):
        return 1
    if (not os.path.isfile(sys.argv[1])):
        return 1

    file = open(sys.argv[1], "r")
    lines = file.readlines()

    offset = int(sys.argv[2])
    start = int(sys.argv[3]) - 1
    end = 4294967295
    if (len(sys.argv) == 5):
        end = int(sys.argv[4]) - 1
        end = min(end, len(lines))
    else:
        end = len(lines)

    # prints first untouched part of the file if it exists
    for i in range(0, start):
        print(lines[i], end = "")
    for i in range(start, end):
        line = lines[i]
        startStart = startTimestampOffset
        startEnd = startTimestampOffset + 10
        endStart = endTimestampOffset
        endEnd = endTimestampOffset + 10

        newStart = offsetTimestamp(line[startStart:startEnd], offset)
        newEnd = offsetTimestamp(line[endStart:endEnd], offset)
        print(line[:startStart] + newStart + "," + newEnd + line[endEnd:], end = "")
    # prints second untouched part of the file if it exists
    for i in range(end, len(lines)):
        print(lines[i], end = "")
    return 0

exit(main())
