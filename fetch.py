#!/usr/bin/env python

import os
import json
import ptree

from internetarchive import search_items, Item

for result in search_items('collection:usda-nurseryandseedcatalog'):
    id = result['identifier']
    item = Item(id)
    metadata = item.get_metadata()
    item_dir = os.path.join('items', ptree.id2ptree(id).lstrip("/"))
    if not os.path.isdir(item_dir):
        os.makedirs(item_dir)
    with open(os.path.join(item_dir, 'metadata.json'), 'w') as fh:
        fh.write(json.dumps(metadata, indent=2))

    total_bytes += sum([f.size for f in item.iter_files()])
    print item_dir
