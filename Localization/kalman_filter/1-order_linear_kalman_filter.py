######################################################
# 1-order linear kalman filter
# ----------------------------
# Descr. : Most simplest Kalman filter
# Author : Akiyuki Beauduin, University of Tokyo, 2018
######################################################

def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

def main():

    # parameters
    measured_pos = [0., 1., 2., 4., 3.]
    motionref_vel = [1., 1., 2., -1., 1.]
    measurement_sig = 4.
    motion_sig = 2.
    mu = 0.                              # initial value of mu
    sig = 10000.                         # initial value of sig
    print('             | position |  sigma  |')

    for i in range(len(measured_pos)):
        [mu, sig] = update(mu, sig, measured_pos[i], measurement_sig)
        print('update [',i,']',':',' %03.3f     ' % mu ,'%03.3f' % sig)
        [mu, sig] = predict(mu, sig, motionref_vel[i], motion_sig)
        print('predict[',i,']',':',' %03.3f     ' % mu ,'%03.3f' % sig)


if __name__ == '__main__':
    main()
