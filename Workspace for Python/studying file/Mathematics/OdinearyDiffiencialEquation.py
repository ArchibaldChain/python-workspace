import numpy as np
import matplotlib.pyplot as plt

# Physical constants
g = 9.8
L = 2
mu = 0.1

THETA_0 = np.pi / 3  # 60 degree
THET_DOT_0 = 0  # No initialize value


# Definition of ODE
def get_theta_double_dot(theta, theta_dot):
    return -mu * theta_dot - (g/L) * np.sin(theta)


# Solution to the differential equation
def theta(t, theta_0, theta_dot_0):
    # Initialize changing value
    theta = theta_0
    theta_dot = theta_dot_0
    delta_t = 0.001  # Time Step
    theta_list = [theta]
    theta_dot_list = [theta_dot]

    for time in np.arange(0, t, delta_t):
        theta_double_dot = get_theta_double_dot(theta, theta_dot)
        theta += theta_dot * delta_t
        theta_dot += theta_double_dot * delta_t
        theta_list.append(theta)
        theta_dot_list.append(theta_dot)
    return theta_list, theta_dot_list


def get_theta(time):
    plt.xlabel('theta')
    plt.ylabel('theta_dot')

    for i in np.arange(-10, 10, 0.5):
        [theta1, theta_dot1] = theta(time, THETA_0, THET_DOT_0 + i)
        plt.plot(theta1, theta_dot1, '--')

    plt.show()


get_theta(50)
