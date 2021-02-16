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
   - `data`: trains tests and classified 

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

