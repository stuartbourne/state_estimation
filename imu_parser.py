import sys
import re
from imu_data import IMUData
from decimal import Decimal


class IMUFileParser():
    @staticmethod
    def parseRawFile(rawFile):
        timestamp_vals = []
        accel_vals = []
        gyro_vals = []
        mag_vals = []
        data_list = []
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
        for idx, val in enumerate(accel_vals):
            data_list.append(IMUData(timestamp_vals[idx], 
                            accel_vals[idx][0], accel_vals[idx][1], accel_vals[idx][2],
                            gyro_vals[idx][0], gyro_vals[idx][1], gyro_vals[idx][2],
                            mag_vals[idx][0], mag_vals[idx][1], mag_vals[idx][2]))
        return data_list

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise NameError("Please supply an input imu.txt file to read from!")
        exit()
    data_list = IMUFileParser.parseRawFile(sys.argv[1])
    print(data_list[-1])