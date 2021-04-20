#JSON stuff

import json

stringOfJsonData = '{"name": "Zophie", "isCat":true, "miceCaught": 0, "felineIQ":null}'

jsonDataAsPythonValue =json.loads(stringOfJsonData)
jsonDataAsPythonValue
