import contractParse as parse
import json
def Add(x):
		return parse.functionGet(x,js)
global js
js = json.loads(str(parse.reader("takeIt.json")).replace("'",'"'))
js = Add("function updateManagers(address newVal) external onlyOwner ")
parse.pen(js,"takeIt.json")