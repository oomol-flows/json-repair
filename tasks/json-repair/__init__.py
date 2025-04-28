import json
import json_repair
#region generated meta
import typing
class Inputs(typing.TypedDict):
    content: str
    indent: int
    preview: bool
class Outputs(typing.TypedDict):
    output: str
#endregion

from oocana import Context

def main(params: Inputs, context: Context) -> Outputs:
    content = params.get("content")
    parsed = json_repair.loads(content)

    indent = params.get("indent")
    if indent == 0:
        indent = None

    result = json.dumps(parsed, indent=indent)

    if params.get('preview'):
        context.preview({
            "type": "text",
            "data": result
        })

    return { "output": result }
