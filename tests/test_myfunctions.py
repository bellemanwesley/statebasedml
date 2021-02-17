from statebasedml import bitfold
from statebasedml import data
import random

def simple_test():
    assert bitfold.transform(1,1,0) == 1
    test_dict_1 = {"hello": {"result":"win","options":["greeting","insult"],"choice":"greeting"}}
    test_dict_1_value = {'hello': {'option_dict': {'greeting': {'count': 1, 'result_dict': {'win': 1}}, 'insult': {'count': 0, 'result_dict': {}}}}}
    assert data.train(test_dict_1) == test_dict_1_value

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
    accuracy_list = []
    for i in range(100):
        test_list = []
        for j in range(100):
            x = random.randint(0,9)
            test_dict = {
                str(x) : {
                    "options": ["0","1"],
                    "desired_result": "correct"
                }
            }
            test_list.append(test_dict)
        class_list = data.classify(datalist=test_list,model=model)
        for j in range(len(test_list)):
            for x in test_list[j]:
                choice = class_list[j][x]
                accuracy_list.append(choice==str(int(x)%2))
    correct = len(list(filter(lambda x: x==True,accuracy_list)))
    total = len(accuracy_list)
    accuracy = float(correct)/total
    assert accuracy > 0.99
    return accuracy

print(odd_even_test())

