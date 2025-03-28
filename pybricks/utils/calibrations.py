
def measure_many(measurement_func, parameters=None, measure_num=100) -> float:
    measurements = []
    for _ in range(measure_num):
        if parameters is None:
            measurements.append(measurement_func())
        else:
            measurements.append(measurement_func(parameters))
    return measurements


def min_max_measure(measurement_func, parameters=None, measure_num=100) -> float:
    measurements = measure_many(measurement_func, parameters, measure_num)
    return (min(measurements), max(measurements))