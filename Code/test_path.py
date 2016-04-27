from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import pytest
import numpy as np
import pandas as pd

from mousestyles import data
from mousestyles.path_index import path_index

def test_path_input():
	movement = data.load_movement(0, 0, 0)

    # checking functions raise the correct errors
	with pytest.raises(ValueError) as excinfo: 
		path_index(movement, -1, -1)
	assert excinfo.value.args[0] == "Input values need to be positive"

	with pytest.raises(TypeError) as excinfo:
		path_index(movement, 1.5, 1.5)
	assert excinfo.value.args[0] == "Input values need to be integer"

def test_path():
	movement = data.load_movement(0, 0, 0)

	# Checking functions output the correct path
	paths = path_index(movement, 1, 1)
	assert paths[:5] == [[22, 53], [55, 59], [67, 89], [91, 95], [96, 114]]
