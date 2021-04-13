from battleshipPretty import create_board
import pandas as pd
from pandas import DataFrame
import numpy as np

def test_create_board():
    np.random.seed(1)
    board = DataFrame(np.random.rand()*100,
               index=list('abcdefghij'),columns=list(range(1,11)), dtype=np.int64)
    df = create_board()
    assert pd.testing.assert_frame_equal(board,df) == None