import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.stats import norm


#######################################################################################################
# Activity 1
#######################################################################################################

# open the file in read mode
filename = open('Raw Data.csv', 'r')

# creating dictreader object
file = csv.DictReader(filename)

# create empty list
gyro_x = []

# append values to list
for col in file:
    gyro_x.append(col['Gyroscope x (rad/s)'])

gyro_x = [float(i) for i in gyro_x]

# find mean and std of gyro_x
gyro_x_mean = np.mean(gyro_x)
gyro_x_std = np.std(gyro_x)

# print values
print(f'Mean of the data is {gyro_x_mean:0.6f}')
print(f'Standard deviation of the data is {gyro_x_std:0.6f}')

# plotter
fig = plt.figure()

sub1 =  fig.add_subplot(2,1,1)
sub2 =  fig.add_subplot(2,1,2)

x = np.arange(-0.1, 0.1, 1e-5)
t = np.arange(0, len(gyro_x), 1)

sub1.plot(gyro_x)
sub1.set_title('Gyroscope X-axis Data')
sub1.hlines(0.0, 0, t[-1], colors='black', )
sub1.set_ylabel('rad/s')

#plot normal distribution 
sub2.plot(x, norm.pdf(x, gyro_x_mean, gyro_x_std), label=f'$mean={gyro_x_mean:.6f}, std={gyro_x_std:.6f}$')
sub2.legend()

plt.show()

#######################################################################################################
# Activity 2
#######################################################################################################

# # TODO Step 1: Fill these out from the worksheet prompt
# # Compute for both Cases 1 and 2 at the same time.
# # initial state: mean and covariance
# mu_x0 = [,]          # init state mean
# sigma_x0 = [,]       # init state std
# # process model parameters 
# v =  [,]             # velocity (m/s)
# dt = [,]             # time delta (s)
# sigma_f = [,]        # std of motion/process model 
# # measurement model parameters
# mu_z = [,]           # sensor reading
# sigma_z = [,]        # std of measurement model


# # TODO Step 2: Fill in values from your worksheet
# ## prediction step
# mu_x_hat = [,]
# sigma_x_hat = [,]


# # TODO Step 3: Fill these out from the worksheet prompt
# ## update step
#     # kalman gain
#     # K = ?
#     # compute residual
#     # y = ?
#     # correct with measurement
# mu_x = [,]
# sigma_x = [,]



# #x-axis ranges
# x = np.arange(-3, 9, 0.001)

# fig = plt.figure()

# sub1 =  fig.add_subplot(1,3,1)
# sub2 =  fig.add_subplot(1,3,2)
# sub3 =  fig.add_subplot(1,3,3)

# #plot normal distribution with mean 0 and standard deviation 1
# sub1.plot(x, norm.pdf(x, mu_x0[0], sigma_x0[0]), label='initial state ' + f'$(mean={mu_x0[0]:.3f}, std={sigma_x0[0]:.3f})$')
# sub1.plot(x, norm.pdf(x, mu_x_hat[0], sigma_x_hat[0]), label='prediction ' + f'$(mean={mu_x_hat[0]:.3f}, std={sigma_x_hat[0]:.3f})$')
# sub1.plot(x, norm.pdf(x, mu_z[0], sigma_z[0]), label='measurement ' + f'$(mean={mu_z[0]:.3f}, std={sigma_z[0]:.3f})$')
# sub1.plot(x, norm.pdf(x, mu_x[0], sigma_x[0]), label='new state ' + f'$(mean={mu_x[0]:.3f}, std={sigma_x[0]:.3f})$')
# sub1.set_title('Case 1')
# sub1.set_ylim(0, 4)
# sub1.legend()

# sub2.plot(x, norm.pdf(x, mu_x0[1], sigma_x0[1]), label='initial state ' + f'$(mean({mu_x0[1]:.3f}, std={sigma_x0[1]:.3f})$')
# sub2.plot(x, norm.pdf(x, mu_x_hat[1], sigma_x_hat[1]), label='prediction ' + f'$(mean={mu_x_hat[1]:.3f}, std={sigma_x_hat[1]:.3f})$')
# sub2.plot(x, norm.pdf(x, mu_z[1], sigma_z[1]), label='measurement ' + f'$(mean={mu_z[1]:.3f}, std={sigma_z[1]:.3f})$')
# sub2.plot(x, norm.pdf(x, mu_x[1], sigma_x[1]), label='new state ' + f'($mean={mu_x[1]:.3f}, std={sigma_x[1]:.3f})$')
# sub2.set_title('Case 2')
# sub2.set_ylim(0, 4)
# sub2.legend()

# sub3.plot(x, norm.pdf(x, mu_x0[0], sigma_x0[1]), label='initial state ' + f'$mean=({mu_x0[0]:.3f}, std={sigma_x0[0]:.3f})$')
# sub3.plot(x, norm.pdf(x, mu_x[0], sigma_x[0]), label='new state ' + f'$mean=({mu_x[0]:.3f}, std={sigma_x[0]:.3f})$')
# sub3.plot(x, norm.pdf(x, mu_x[1], sigma_x[1]), label='new state ' + f'$mean=({mu_x[1]:.3f}, std={sigma_x[1]:.3f})$')
# sub3.set_title('Comparison of Cases 1 & 2')
# sub3.set_ylim(0, 4)
# sub3.legend()



# plt.show()
