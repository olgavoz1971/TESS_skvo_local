class PipeException(Exception):
    # print(f'My exception {Exception} occurred')
    pass


def normalize(arr):
    return (arr - arr.min()) / (arr.max() - arr.min())


def log_gamma(data, gamma=0.9, log=True):
    """
    Gamma correction to enhance dark regions
    :param log: disable if False
    :param data:
    :param gamma: Adjust gamma to control the contrast in dark regions
    :return:
    """
    import numpy as np
    if not log:
        return data
    # data = normalize(data)
    # log_data = normalize(np.log1p(data))
    log_data = np.log1p(data)
    # return normalize(np.power(log_data, gamma))
    return np.power(log_data, gamma)


def safe_none(value):
    return '' if value is None else value

