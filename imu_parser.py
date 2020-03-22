import sys
import re
from decimal import Decimal


class IMUFileParser():
    @staticmethod
    def parseRawFile(rawFile):
        timestamp_vals = []
        accel_vals = []
        gyro_vals = []
        mag_vals = []
        with open(rawFile) as fp:
            line = fp.readline()
            accel_pattern = 'accelerometers'
            gyro_pattern = 'gyroscopes'
            mag_pattern = 'magnetometer'
            header_pattern = 'header'
            while line:
                if (re.match(header_pattern, line)):
                    fp.readline() #seq
                    fp.readline() #stamp
                    timestamp_vals.append(Decimal(fp.readline().rsplit()[-1] + '.' + fp.readline().rsplit()[-1])) #append seconds and nanoseconds
                else:
                    #not the first line
                    if re.match(accel_pattern, line):
                        accel_vals.append([Decimal(fp.readline().rsplit()[-1]), Decimal(fp.readline().rsplit()[-1]), Decimal(fp.readline().rsplit()[-1])])
                    if re.match(gyro_pattern, line):
                        gyro_vals.append([Decimal(fp.readline().rsplit()[-1]), Decimal(fp.readline().rsplit()[-1]), Decimal(fp.readline().rsplit()[-1])])
                    if re.match(mag_pattern, line):
                        mag_vals.append([Decimal(fp.readline().rsplit()[-1]), Decimal(fp.readline().rsplit()[-1]), Decimal(fp.readline().rsplit()[-1])])
                line = fp.readline()
            assert(len(accel_vals) == len(gyro_vals))
            assert(len(gyro_vals) == len(mag_vals))
            assert(len(mag_vals) == len(timestamp_vals))
        return accel_vals, gyro_vals, mag_vals, timestamp_vals

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise NameError("Please supply an input imu.txt file to read from!")
        exit()
    accel_vals, gyro_vals, mag_vals, ts_vals = IMUFileParser.parseRawFile(sys.argv[1])
    print(accel_vals[-1])
    print(gyro_vals[-1])
    print(mag_vals[-1])
    print(ts_vals[-1])