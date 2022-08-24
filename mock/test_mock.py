from unittest.mock import Mock

mock = Mock()
print(mock)

import json

data = json.dumps({'a': 1})
json = mock
data = json.dumps({'a': 1})

print(dir(json))
print(data)
