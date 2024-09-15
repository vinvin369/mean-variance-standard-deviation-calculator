import numpy as np

def calculate(arr):
    """
    Convert the input into a 3x3 matrix
    Calculate mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
    """

    # Check the input and raise error
    if len(arr) != 9:
        raise ValueError("List must contain nine numbers.")

    # Reshaping the input into a 3x3 matrix
    matrix = np.array(arr).reshape(3, 3)

    # Mean
    mean_flattened = np.mean(matrix)
    mean_axis1 = list(np.mean(matrix, axis=0))
    mean_axis2 = list(np.mean(matrix, axis=1))

    # Variance
    variance_flattened = np.var(matrix)
    variance_axis1 = list(np.var(matrix, axis=0))
    variance_axis2 = list(np.var(matrix, axis=1))

    # Standard Deviation
    sd_flattened = np.std(matrix)
    sd_axis1 = list(np.std(matrix, axis=0))
    sd_axis2 = list(np.std(matrix, axis=1))

    # Max
    max_flattened = np.max(matrix)
    max_axis1 = list(np.max(matrix, axis=0))
    max_axis2 = list(np.max(matrix, axis=1))

    # Min
    min_flattened = np.min(matrix)
    min_axis1 = list(np.min(matrix, axis=0))
    min_axis2 = list(np.min(matrix, axis=1))

    # Sum
    sum_flattened = np.sum(matrix)
    sum_axis1 = list(np.sum(matrix, axis=0))
    sum_axis2 = list(np.sum(matrix, axis=1))

    # Prepare the output dictionary with desired formatting
    calculations = {
        'mean': [mean_axis1, mean_axis2, mean_flattened],
        'variance': [variance_axis1, variance_axis2, variance_flattened],
        'standard deviation': [sd_axis1, sd_axis2, sd_flattened],
        'max': [max_axis1, max_axis2, max_flattened],
        'min': [min_axis1, min_axis2, min_flattened],
        'sum': [sum_axis1, sum_axis2, sum_flattened]
    }

    return calculations

# Example call
result = calculate([0,1,2,3,4,5,6,7,8])

# Print result with exactly 6 square brackets
print(f"mean: {result['mean']}")
print(f"variance: {result['variance']}")
print(f"standard deviation: {result['standard deviation']}")
print(f"max: {result['max']}")
print(f"min: {result['min']}")
print(f"sum: {result['sum']}")
