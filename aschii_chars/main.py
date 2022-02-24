import re
import typing
from fastapi import FastAPI
import pandas as pd

CHAR_MULTIPLIER = 10

app = FastAPI()


@app.post("/convert", response_model=typing.List[int])
async def root(request: typing.List[str]) -> typing.List[int]:
    char_df = pd.DataFrame(request, columns=['chars'])
    chars_number_df = char_df.applymap(lambda x: convert_ascii_to_number(x))
    chars_number_df['char_number'] = chars_number_df['chars'] * CHAR_MULTIPLIER
    return chars_number_df['char_number'].tolist()


def convert_ascii_to_number(char):
    number = 0
    if re.match(r'^[a-g|A-G]$', char):
        number = ord(char)
    return number
