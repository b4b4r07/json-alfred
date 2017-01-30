import sys
import json
import os.path
from workflow import Workflow, ICON_WARNING

def load_json(path):
    with open(path) as f:
        return json.load(f)

def search_with_tags(item):
    ret = u'{} {}'.format(item.get('key'), item.get('value'))
    if item.get('tags'):
        ret += u' '.join(item.get('tags'))
    return ret

def main(wf):
    data = []
    query = None
    if len(wf.args):
        query = wf.args[0]

    db = os.path.expanduser('~/.json-alfred.json')
    try:
        data = load_json(db)
    except IOError as e:
        wf.add_item('Not found: %s' % db, icon=ICON_WARNING)
        wf.send_feedback()
        return 1

    """ Filter """
    items = data
    if query:
        items = wf.filter(query, items, key=search_with_tags)

    if not items:
        wf.add_item('No matching found', icon=ICON_WARNING)

    for item in items:
        wf.add_item(
                title=item.get('key'),
                subtitle=item.get('value'),
                icon='icon.png',
                arg=item.get('value'),
                valid=True)

    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
