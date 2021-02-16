statebasedml
========

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

statebasedml is a Python library for training data on state based machine learning data. 

Installation instructions
-------------------------

    python3 -m pip install --upgrade pip
	python3 -m pip install statebasedml

## Classes
The statebasedml library has two classes:
   - `bitfold`: [compresses states in order to shrink big data](https://medium.com/swlh/shrinking-big-data-with-bit-folding-4ea0aa6a055d)
   - `data`: trains, tests, and classifies input datasets 

# bitfold

*Import statebasedml.bitfold*

```python
	from statebasedml import bitfold
```

*bitfold has 2 methods*
   - `gen_param()`: generates the parameters for a fold
   - `fold()`: actually folds the input data

#### gen_param

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


#### fold

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

### Import statebasedml.data

```python
	from statebasedml import data
```

*data has 2 methods*
   - `train()`: generates a model based on tagged input data
   - `update()`: updates a model with new tagged input data
   - `test()`: tests a trained model based on additional tagged input data
   - `classify()`: classifies untagged data using a provided model

#### train

*request syntax*

```python

    trained_model = data.train(
        datadict = {
            "key1": {
                "result": string,
                "options": [option1, option2, ..., optionN],
                "choice": optionN
            },
            ...,
            "keyN": ...
        }
    )

```

*parameters*

          * Bullet list
              * Nested bullet
                  * Sub-nested bullet etc
          * Bullet list item 2
   * `datadict` *(dict)*: This is simply the input value that you want to shrink.
       *   `key` *(string)*: .
          * `result` *(string)*: .
          * `options` *(list)*: .
          * `choice` *(string)*: .

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

#### update

#### test

#### classify

*request syntax*

```python

    classifications = data.classify(
        datadict = {
            "key1": {
                "options": [option1, option2, ..., optionN],
                "preferred_result": result
            },
            ...,
            "keyN": ...
        },
        model = model_dict
    )

```
