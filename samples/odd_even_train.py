def odd_even_test():
    model = {}
    for i in range(10000):
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
        model = data.update(datadict=test_dict,model=model)
    accuracy = 0
    for i in range(1000):
        x = random.randint(0,9)
        test_dict = {
            str(x) : {
                "options": ["0","1"],
                "desired_result": "correct"
            }
        }
        classify_dict = data.classify(datadict=test_dict,model=model)
        classification = classify_dict[str(x)]
        if classification == str(x%2):
            accuracy = (accuracy*i + 1)/(i+1)
        else:
            accuracy = (accuracy*i)/(i+1)
    return accuracy

print(odd_even_test())