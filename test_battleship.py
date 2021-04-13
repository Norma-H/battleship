from battleshipPretty import create_board
import pandas as pd
from pandas import DataFrame

def test_create_board():
    board = DataFrame(index=list('abcdefghij'),columns=list(range(1,11))))
    df = create_board()
    assert df == board