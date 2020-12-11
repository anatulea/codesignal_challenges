'''
While migrating to a new operation system, you faced an unexpected problem: now you need to create a new build command for your favorite text editor plugin. The build command is stored as a JSON file that you should now update. In order to make the transition simpler, you decided to write a program that will create a template of the build command by replacing everything but dictionaries in given jsonFile with their default values: numbers with 0, strings with "" and lists with [].

It is guaranteed that there are only aforementioned types in the given JSON file.

Example

For

jsonFile =
"""
{
    "version": "0.1.0",
    "command": "c:python",
    "args": ["app.py"],
    "problemMatcher": {
        "fileLocation": ["relative", "${workspaceRoot}"],
        "pattern": {
            "regexp": "^(.*)+s$",
            "message": 1
        }
    }
}
"""
the output should be

buildCommand(jsonFile) =
"""
{
    "version": "",
    "command": "",
    "args": [],
    "problemMatcher": {
        "fileLocation": [],
        "pattern": {
            "regexp": "",
            "message": 0
        }
    }
}
"""
'''
import json
def buildCommand(jsonFile):
    data= json.loads(jsonFile)
    print(data)
    for k,v in data.items():
        # print(v)
        if isinstance(v, str):
            data[k] = ''
        elif isinstance(v, int):
            data[k]= 0
        elif isinstance(v, float):
            data[k]=0
        elif isinstance(v,list):
            data[k]= []
        elif isinstance(v, dict):
            # print(v)
            v2=json.dumps(v)
            data[k]= json.loads(buildCommand(v2))
    
    print(data)
    return json.dumps(data)

'''
def buildCommand(jsonFile):
    return json.dumps(clean(json.loads(jsonFile, object_pairs_hook=OrderedDict)))
        
def clean(x):
    if type(x) is int or type(x) is float:
        return 0
    elif type(x) is str:
        return ""
    elif type(x) is list:
        return []
    elif type(x) is OrderedDict:
        res = OrderedDict()
        for k, v in x.items():
            res[k] = clean(v)
        return res

'''

