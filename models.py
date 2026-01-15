import pandas as pd
from pydantic import BaseModel
from db import Terrorists

data = pd.read_csv("terrorists_data.csv")
df = pd.DataFrame(data)
print (df.head(5))


def to_json(data: Terrorists):
    data_json = data.model_dump_json()
    