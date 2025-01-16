import numpy as np

#this function calculate statistics
def calculate(x):  
    statistics = {}
    statistics["mean"] = np.mean(x)
    statistics["median"] = np.median(x)
    statistics["var"] = np.var(x)
    statistics["std"] = np.std(x)
    statistics['max'] = np.max(x)
    statistics['min'] = np.min(x)
    statistics['sum'] = np.sum(x)
    statistics['prod'] = np.prod(x)
    statistics['diff'] = np.diff(x).tolist()
    statistics['LCM'] = np.lcm.reduce(x)
    statistics['GCD'] = np.gcd.reduce(x)

    return statistics
  
# Convert input string to a list of integers
numeric_input = list(map(int, input('Insert your numbers separated by spaces: ').split()))
statistics_calculation = calculate(numeric_input)
print(statistics_calculation)


#this line of code turn int to float
integer = int(input('your number: '))
print(float(integer))