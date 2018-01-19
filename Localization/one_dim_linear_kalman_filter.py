######################################################
# 1-dim linear kalman filter
# ----------------------------
# Descr. : Most simplest Kalman filter
# Author : Akiyuki Beauduin, University of Tokyo, 2018
######################################################

import sys      # For comandline input
import unittest # For Unit Test

class Parameters(object):
    def __init__(self):
        self.measured_pos = [0., 1.2, 2.3, 4.1, 3.0, 6.1]
        self.motionref_vel = [1., 1., 2., -1., 3., 3.]
        self.mu = 0.                     # initial value of mu
        self.sig = 10000.                # initial value of sig
        self.measurement_sig = 4.
        self.motion_sig = 2.

    def set_sigma(self, msr_sig, mtn_sig):
        self.measurement_sig = msr_sig
        self.motion_sig = mtn_sig

def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

def kalman_filter(parameters):

    measured_pos = parameters.measured_pos
    motionref_vel = parameters.motionref_vel
    mu = parameters.mu               # initial value of mu
    sig = parameters.sig             # initial value of sig
    measurement_sig = parameters.measurement_sig
    motion_sig = parameters.motion_sig

    # avoid division by 0 or negative number
    epsilon = 0.0000001
    if measurement_sig <= 0.0:
        measurement_sig = epsilon
    if motion_sig <= 0.0:
        motion_sig = epsilon

    print('-----------------------------------------------------------------')
    print('measured_pos    :',measured_pos)
    print('motionref_vel   :  ',motionref_vel)
    print('initial_mu      :',mu)
    print('initial_sig     :',sig)
    print('measurement_sig :',measurement_sig)
    print('motion_sig      :',motion_sig)
    print('-----------------------------------------------------------------')
    print('             | position |  sigma  |')


    for i in range(len(measured_pos)):
        [mu, sig] = update(mu, sig, measured_pos[i], measurement_sig)
        print('update [',i,']',':',' %03.3f     ' % mu ,'%03.3f' % sig)
        [mu, sig] = predict(mu, sig, motionref_vel[i], motion_sig)
        print('predict[',i,']',':',' %03.3f     ' % mu ,'%03.3f' % sig)


if __name__ == '__main__':
    args = sys.argv

    if len(args) == 1:
        test_paras = Parameters()
        kalman_filter(test_paras)
    elif len(args) == 3:                              # set my sigma
        my_paras = Parameters()
        my_paras.set_sigma(float(args[1]), float(args[2]))
        kalman_filter(my_paras)
    elif args[1] == '-v':
        print('1-dim linear kalman filter 1.0.0')

    else:
        print('error')
