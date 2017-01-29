#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function, unicode_literals

import json
import sys
import re

from workflow import Workflow, ICON_WARNING, web, ICON_ERROR
import workflow

def main(wf):
    query = None
    if len(wf.args):
        query = wf.args[0]

    if not query:
        wf.add_item(
                'No query specified',
                'Paste a query',
                icon=ICON_WARNING)
    else:
        f = open('data.json', 'r')
        jsonData = json.load(f).iteritems()
        # cached_json = wf.cached_data('cj', jsonData, max_age=5)
        # hits = wf.filter(query, jsonData, jsonData.key())
        if query:
            jsonData = wf.filter(query, jsonData, key=lambda x: " ".join(x))
        for k, v in jsonData:
            wf.add_item(
                k, v,
                arg=v,
                valid=True,
                icon='host.png')
            wf.send_feedback()

        # for k, v in jsonData.items():
        #     if re.compile(query).search(k):
        #         wf.add_item(
        #                 k, jsonData[k],
        #                 arg=k,
        #                 valid=True,
        #                 icon='host.png')
        #                 # uid=query,
        #                 # type='file',
        #         wf.send_feedback()
        #         return
        #         # print(jsonData[k])

    # wf.add_item('No matches', 'hoge', icon='host.png')
    # wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
