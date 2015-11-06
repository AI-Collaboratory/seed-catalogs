#!/usr/bin/env python

"""
fetch.py will fetch metadata for the Seed Catalog collection at 
Internet Archive.
"""

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

    print item_dir
