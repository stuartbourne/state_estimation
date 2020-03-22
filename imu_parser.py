import sys
import re

if len(sys.argv) < 2:
    raise NameError("Please supply an input imu.txt file to read from!")
    exit()

timestamp_vals = []
accel_vals = []
gyro_vals = []
mag_vals = []

with open(sys.argv[1]) as fp:
    line = fp.readline()
    cnt = 1
    accel_pattern = 'accelerometers'
    gyro_pattern = 'gyroscopes'
    mag_pattern = 'magnetometer'
    header_pattern = 'header'
    while line:
        if (re.match(header_pattern, line)):
            fp.readline() #seq
            fp.readline() #stamp
            timestamp_vals.append(fp.readline().rsplit()[-1] + '.' + fp.readline().rsplit()[-1]) #append seconds and nanoseconds
        else:
            #not the first line
            if re.match(accel_pattern, line):
                accel_vals.append([fp.readline().rsplit()[-1], fp.readline().rsplit()[-1], fp.readline().rsplit()[-1]])
            if re.match(gyro_pattern, line):
                gyro_vals.append([fp.readline().rsplit()[-1], fp.readline().rsplit()[-1], fp.readline().rsplit()[-1]])
            if re.match(mag_pattern, line):
                mag_vals.append([fp.readline().rsplit()[-1], fp.readline().rsplit()[-1], fp.readline().rsplit()[-1]])
        cnt += 1
        line = fp.readline()
    print(len(accel_vals))
    print(len(gyro_vals))
    print(len(mag_vals))
    print(len(timestamp_vals))
    print(accel_vals[-1])
    print(gyro_vals[-1])
    print(mag_vals[-1])
    print(timestamp_vals[-1])