# seed-catalogs

The National Agriculture Library and the Internet Archive have digitized
a collection of [18,390 seed catalogs] that were selected from a [collection]
of over 200,000 American and foreign catalogs dating from the 1700s. 
This repository is a scratch space for the Digital Curation and Innovation 
Center ([DCIC]) at the University of Maryland to play with the data.

## Utilities:

Before you run anything here make sure you've installed any Python dependencies:

    pip install -r requirements.txt

* fetch.py - download the metadata for all the items in the collection and store it in a [pairtree] directory named `items`.


[18,390 seed catalogs]: https://archive.org/details/usda-nurseryandseedcatalog
[collection]: http://specialcollections.nal.usda.gov/guide-collections/henry-g-gilbert-nursery-and-seed-trade-catalog-collection
[DCIC]: http://dcic.umd.edu/
[pairtree]: https://wiki.ucop.edu/display/Curation/PairTree
