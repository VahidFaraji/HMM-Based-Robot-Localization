import numpy as np
from models import *

class HMMFilter:
    def __init__(self, probs, tm, om, sm):
        """
        Initialize the HMM forward filter.
        :param probs: Initial probability distribution
        :param tm: Transition model (state transition probabilities)
        :param om: Observation model (sensor likelihoods)
        :param sm: State model (grid properties)
        """
        self.__tm = tm
        self.__om = om
        self.__sm = sm
        self.__f = probs  # Prior belief over states

    def filter(self, sensorR: int) -> np.array:
        """
        Perform one step of forward filtering in the HMM.
        :param sensorR: Sensor reading at the current time step (can be None)
        :return: Updated belief over states
        """
        # Step 1: Predict next state (belief propagation)
        predicted_f = self.__tm.get_T() @ self.__f

        # Step 2: Update using observation model
        if sensorR is not None:
            observation_prob = self.__om.get_o_reading(sensorR)  # Likelihood of observation
            updated_f = observation_prob @ predicted_f  # Bayesian update
        else:
            updated_f = predicted_f  # No sensor reading, propagate belief

        # Step 3: Normalize
        self.__f = updated_f / np.sum(updated_f)
        return self.__f

class HMMSmoother:
    def __init__(self, tm, om, sm):
        """
        Initialize the HMM forward-backward smoother.
        :param tm: Transition model
        :param om: Observation model
        :param sm: State model
        """
        self.__tm = tm
        self.__om = om
        self.__sm = sm

    def smooth(self, sensor_r_seq: np.array, f_k_seq: np.array) -> np.array:
        """
        Perform forward-backward smoothing over a sequence of time steps.
        :param sensor_r_seq: Sequence of sensor readings
        :param f_k_seq: Sequence of forward probabilities (from forward filter)
        :return: Smoothed probabilities for all states over time
        """
        T = len(sensor_r_seq)  # Total time steps
        smoothed_probs = np.copy(f_k_seq)
        b = np.ones_like(f_k_seq[-1])  # Backward messages initialized to 1

        # Backward pass for smoothing
        for t in reversed(range(T - 1)):
            # Backward message update
            b = self.__tm.get_T_transp() @ (self.__om.get_o_reading(sensor_r_seq[t + 1]) @ b)
            # Combine forward and backward messages
            smoothed_probs[t] *= b
            smoothed_probs[t] /= np.sum(smoothed_probs[t])  # Normalize

        return smoothed_probs
