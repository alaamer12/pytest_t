from pprint import pprint
import pytest
pprint(dir(pytest))
print("%" * 50)
pprint(pytest.__doc__)
print("%" * 50)
pprint(pytest.__all__)
print(len(pytest.__all__))
