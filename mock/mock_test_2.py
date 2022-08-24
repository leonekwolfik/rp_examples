from unittest.mock import Mock
import json

json = Mock()
json.dumps({'a': 1})
json.dumps({'a': 1})
json.dumps({'a': 1})
json.loads('{"a": 1}')
# json.dumps({'a': 1})
# print(dir(json))

print(json.dumps.assert_called())
# print(json.dumps.assert_called_once())
print(json.dumps.assert_called_with({'a': 1}))
print(json.dumps.call_args)
print(json.dumps.call_count)
print(json.dumps.method_calls)
print(json.method_calls)
