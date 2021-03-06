statebasedml
========

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

statebasedml is a Python library for training data with state based machine learning. The documentation below should help you understand the parameters passed to the statebasedml functions and what they return, but I recommend starting with examples. Check out the examples in the [samples folder](/samples)

Installation instructions
-------------------------

    python3 -m pip install --upgrade pip
	python3 -m pip install statebasedml

## Classes
The statebasedml library has two classes:
   - `bitfold`: [compresses states in order to shrink big data](https://medium.com/swlh/shrinking-big-data-with-bit-folding-4ea0aa6a055d)
   - `data`: trains, tests, and classifies input datasets 

# bitfold

*import statebasedml.bitfold*

```python
	from statebasedml import bitfold
```

*bitfold has 2 methods*
   - `gen_param()`: generates the parameters for a fold
   - `fold()`: actually folds the input data

## gen_param

*request syntax*

```python

    fold_parameters = bitfold.gen_param(
        size = 256
    )

```

*parameters*
   - `size` *(integer)*: The number of bits of the largest sized string that you want to fold. You can determine the bit size of a string with `8*len(string)`

*response syntax*

```python

    {
        "mapping":mapping,
        "ops":ops
    }

```


## fold

*request syntax*

```python

    folded_value = bitfold.fold(
        value = string,
        new_size = 123,
        mapping = [1, 2, 3],
        ops = [1, 2, 3]
    )

```

*parameters*
   - `value` *(string)*: This is simply the input value that you want to shrink.
   - `new_size` *(integer)*: The number of bits of the new string that you want to be generated. If you want to output strings of length `l` then this value is `l * 8`.
   - `mapping` *(list)*: This is a mapping of the bits to be folded. This paramater is generated with `fold_parameters = bitfold.gen_param()`. Then you should have `mapping = fold_parameters["mapping"]`.
   - `ops` *(list)*: This is a list of the operations to be perfomed on the mapping. This paramater is generated with `fold_parameters = bitfold.gen_param()`. Then you should have `ops = fold_parameters["ops"]`.

*response syntax*

The `fold()` function simply outputs a folded string.

# data

*import statebasedml.data*

```python
	from statebasedml import data
```

*data has 4 methods*
   - `train()`: generates a model based on tagged input data
   - `update()`: updates a model with new tagged input data
   - `test()`: tests a trained model based on additional tagged input data
   - `classify()`: classifies untagged data using a provided model

## train

*request syntax*

```python

    trained_model = data.train(
        datalist = [
            {
                "key1": {
                    "result": string,
                    "options": [option1, option2, ..., optionN],
                    "choice": optionN
                }
            },
            {
                ...
            },
            {
                "keyN": ...
            }
        ]
    )

```

*parameters*

* `datalist` *(list)*: The function takes a single list of dictionaries with the below key/value pairs.
   * `key` *(string)*: Each dictionary should include one or more keys. The key is the measured *state* of the system that you want to capture. One key per list item is recommended, but the function will accept multiple keys per list item.
      * `result` *(string)*: The result is the *tag* associated with that key. If you are using options, then the tag is associated with the key/choice pair.
      * `options` *(list)* \[OPTIONAL\]: Only use options if you have additional options associated with your state. One example of when to use options is for teaching the model to play board games. In this case, the state is the configuration of the board and options are possible moves.
      * `choice` *(string)* \[OPTIONAL\]: The choice parameter is required if you are using options. The choice must be a member of the options list. The choice parameter is the choice made to achieve the provided result. 

*response syntax*

```python

    {
        "key1": {
            "option_dict": {
                "option1": {
                    "count": 123,
                    "result_dict": {
                        "result1":count1,
                        "result2":count2,
                        ...,
                        "resultN":countN
                    }
                }, 
                ...,
                "optionN": ...
            }
        },
        ...,
        "keyN": {
            "count": 123,
            "result_dict": {
                "result1": count1,
                ...,
                "resultN": countN
            }
        }
    }

```

## update

The update function is similar to the train function, except you add a model to the second argument. In fact, the train function can operate as the update function if you pass a model to it as a `model=model` argument. I just added `update()` for syntatic convenience.

*request syntax*

```python

    updated_model = data.update(
        datalist = datalist,
        model = model
    )

```

*parameters*

* `datalist` *(list)*: This takes the same format as the input specified in the `train()` function above.
* `model` *(dict)*: This takes the same format as the output specified in the `train()` function above.

*response syntax*

The `update()` function outputs a model with the same format as the `train()` function above.

## test

*request syntax*

```python

    model_performance = data.test(
        datalist = datalist,
        model = model
    )

```

*parameters*

* `datalist` *(list)*: This takes the same format as the input specified in the `train()` function above.
* `model` *(dict)*: This takes the same format as the output specified in the `train()` function above.

*response syntax*

```python

    {
        "accuracy": 0.123,
        "loss": 1.23
    }

```


## classify

*request syntax*

```python

    classifications = data.classify(
        datalist = [
            {
                "key1": {
                    "options": [option1, option2, ..., optionN],
                    "desired_result": result
                },
                ...,
                "keyN": {
                    "results": [result1, result2, result3]
                }
            },
        ]
        model = model
    )

```

*response syntax*

```python

    [
        {"key1": "string"},
        ...,
        {"keyN": "string"}
    ]

```
