import sys
from imu_parser import IMUFileParser
from imu_data import IMUData
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

#this class handles executing and plotting the kalman filter on the IMU data
class IMUKalman:
    G_VECTOR = np.array([0, 0, Decimal(-9.81)])    #Assuming NED coordinate frame is positive global frame
    ROT_VECTOR = np.array([1, -1, -1])
    def __init__(self, data_list):
        self.imu_data = data_list
    
    def estimatePosition(self):

        for idx, data in enumerate(self.imu_data):
            if idx == 0:
                #TODO: Use FQA or some other method to achieve initial orientation
                #initial conditions NOTE: b denotes body frame, g denotes global frame (NED)
                data.accel = data.accel * self.ROT_VECTOR
                #TODO: change this once orientation estimation is introduced
                a_b0 = data.accel
                v_b0 = np.array([Decimal(0), Decimal(0), Decimal(0)]) 
                w_b0 = np.array([Decimal(0), Decimal(0), Decimal(0)])
                s_b0 = np.array([Decimal(0), Decimal(0), Decimal(0)])        #origin is 0, 0, 0
                t_lst = np.array([Decimal(0)])
                ag_lst = [a_b0]
                vg_lst = [v_b0]
                sb_lst = [s_b0]
                t_0 = data.timestamp
                t_prev = t_0
                v_prev = v_b0
                a_prev = a_b0 
                s_prev = s_b0
                continue
            # TODO: get body frame rotation *?to?* inertial frame
            #For now, manually encode a 180 degree rotation about the x by flipping z and y
            data.accel = data.accel * self.ROT_VECTOR
            # TODO: apply to gravity vector g

            #update displacement using previous acceleration values and timestamp
            #currently we will use body frame with global scale. E.g. start at 0, 0, 0 and move at rates of accel in global frame
            #This will be eventually offset by mine coordinate system input to translate into mine coordinate system
            sb = s_prev + v_prev * t_prev

            # subtract gravity vector acceleration in body frame from body acceleration
            ag = data.accel - self.G_VECTOR

            #  convert to linear velocity
            delta_t = data.timestamp - t_prev
            vg = ag * delta_t + v_prev

            #set up for next iteration
            ag_lst.append(ag)
            vg_lst.append(vg)
            sb_lst.append(sb)

            a_prev = ag
            v_prev = vg
            t_prev = data.timestamp
   

    #This function handles plotting the data via pyplot
    def plot(self):
        #lets start by just plotting x values
        x_accel = []
        y_accel = []
        z_accel = []
        timestamps = [0]
        time = 0
        for idx, data in enumerate(self.imu_data):
            #data.accel = data.accel * self.ROT_VECTOR #- self.G_VECTOR
            ag = data.accel - self.G_VECTOR
            x_accel.append(ag[0])
            y_accel.append(ag[1])
            z_accel.append(ag[2])
            if idx >= 1:
                time += (data.timestamp - self.imu_data[idx - 1].timestamp)
                timestamps.append(time)
        fig = plt.figure()
        ax = plt.subplot(111)
        ax.plot(timestamps, x_accel, label="x accel")
        ax.plot(timestamps, y_accel, label="y accel")
        ax.plot(timestamps, z_accel, label="z accel")
        plt.title("Acceleration plot")
        ax.legend()
        plt.show()


#gets gaussian value associated with variable x given mean and variance
def gaussian(x, mean, var):
    return np.exp(-np.power(x - mean, 2)/var)/np.sqrt(2 * np.pi)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise NameError("Please supply an input imu.txt file to read from!")
    data_list = IMUFileParser.parseRawFile(sys.argv[1])
    kalman = IMUKalman(data_list)
    kalman.estimatePosition()
    kalman.plot()