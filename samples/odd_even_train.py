import random
from statebasedml import data

def odd_even_test():
    model = {}
    for j in range(100):
        test_list = []
        for i in range(100):
            x = random.randint(0,9)
            guess = random.randint(0,1)
            if guess == x%2:
                result = "correct"
            else:
                result = "wrong"
            test_dict = {
                str(x): {
                    "result": result,
                    "options": ["0","1"],
                    "choice": str(guess)
                }
            }
            test_list.append(test_dict)
        model = data.update(datalist=test_list,model=model)
    test_list = []
    for i in range(100):
        x = random.randint(0,9)
        guess = random.randint(0,1)
        if guess == x%2:
            result = "correct"
        else:
            result = "wrong"
        test_dict = {
            str(x): {
                "result": result,
                "options": ["0","1"],
                "choice": str(guess)
            }
        }
        test_list.append(test_dict)
    #Now that we have another test list, we can use it to test our model with some new numbers
    performance = data.test(datalist=test_list,model=model)
    #Now let's classify a random number
    random_value = random.randint(0,9)
    value_class = data.classify(datalist=[
        {
            str(random_value): {
                "options": ["0","1"],
                "desired_result": "correct"
            }
        }
    ],
    model=model
    )
    return performance,value_class

print(odd_even_test())