
## Functions
# Local Linear Regression for estimating time series data
def LLR_test(model_1, model_2, DF = 1):
    # log likelihood of a model 1
    llf1 = model_1.llf
    llf2 = model_2.llf
    LLR = (2*(llf2-llf1))    
    p = chi2.sf(LLR, DF).round(5)
    return p

# create a differenced series
def difference(dataset, interval=1):
    diff = list()
    for i in range(interval, len(dataset)):
        value = dataset[i] - dataset[i - interval]
        diff.append(value)
    return np.array(diff)

# Invert differenced value
def inverse_difference(history, y_predicted, interval=1):
    history = list(history)
    n = len(y_predicted)
    if len(y_predicted) == 1:
        value = y_predicted[i] + history[-interval]
        history.append(value)
    else:
        value = y_predicted[0] + history[-interval]
        history.append(value)
        
        for i in range(1, n):
            value = y_predicted[i] + history[-interval]
            history.append(value)
    return np.array(history[-n:])
