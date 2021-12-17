import numpy as np

def mostCommonBit(measurements, position):
    numberOfMeasurements = len(measurements)
    return 1 if sum([(measurement & 2**position) / 2**position for measurement in measurements ]) >= numberOfMeasurements/2 else 0

def leastCommonBit(measurements, position):
    numberOfMeasurements = len(measurements)
    return 1 if sum([(measurement & 2**position) / 2**position for measurement in measurements ]) < numberOfMeasurements/2 else 0

def filterByBit(measurements, position, bit):
    if bit == 0:
        return np.extract(np.bitwise_and(measurements, 2**position) == 0, measurements)
    else:
        return np.extract(np.bitwise_and(measurements, 2**position) > 0, measurements)

def filterMeasurementsByfunc(measurements, numberOfBits, func):
    filtered_measurements = measurements

    position = numberOfBits - 1
    while len(filtered_measurements)>1 and position>=0:
        filtered_measurements=filterByBit(filtered_measurements, position, func(filtered_measurements, position))
        position = position - 1

    if len(filtered_measurements) != 1:
        raise 'Not exactly one element left'

    return filtered_measurements[0]

with open('input.txt') as f:
    report = [x.strip() for x in f.readlines()]
    # report = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

    numberOfBits = len(report[0])
    measurements = np.array([int(x,2) for x in report])

    gamma_rate = sum([mostCommonBit(measurements, position) * 2**position for position in range(numberOfBits)])
    epsilon_rate = gamma_rate^(2**numberOfBits-1)
    print(f"Part 1: Power consumption: {gamma_rate*epsilon_rate}")

    filtered_measurements_oxygen=filterMeasurementsByfunc(measurements, numberOfBits, mostCommonBit)
    filtered_measurements_c02=filterMeasurementsByfunc(measurements, numberOfBits, leastCommonBit)

    print(f"Part 2: Power consumption: {filtered_measurements_oxygen*filtered_measurements_c02}")



