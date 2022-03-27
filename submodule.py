
from pydantic import BaseModel
from typing import Optional


class Foo(BaseModel):
    count: int
    size: Optional[float] = None
    identifier: float = 0.0






class Bar(BaseModel):
    apple: str = 'x'
    banana: str = 'y'
    identifier: float = 0.0





class Spam(BaseModel):
    bars: list[Bar]
    name: str  = "Spam"
    identifier: float = 0.0


m = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
print(m)
