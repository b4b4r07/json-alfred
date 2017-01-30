import sys
import json
import os.path
from workflow import Workflow, ICON_WARNING

def main(wf):
    db = os.path.expanduser('~/.json-alfred.json')

    with open(db, 'r') as f:
        data = json.load(f)

    query = None
    if len(wf.args):
        query = wf.args[0]

    items = data
    if query:
        items.append(dict(key=query, value=query))

    with open(db, 'w') as f:
        json.dump(data, f)

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
