OpenMaker Community Data Standardization
========================================

It aims data standardization and interoperability between oinsight *(a set of data mining and machine learning functionalities developed under the [OpenMaker Project's](http://openmaker.eu/)*) modules and its third party clients.

Current version provides a set of command-line tools as well as a python module 
* to be able to validate a JSON file against its predesigned schema
* to be able to inspect and query the design of a JSON schema 

## Install

### Via Python's standard distribution channel PyPI 
```bash
pip install omdata
```
### After downloading the repository
```bash
git clone https://github.com/bulentozel/omdata.git
```

```bash
cd omdata
```

```bash
pip install .
```
## Usage

### Command line tools

Validating a json file against its schema
```bash
validate -q <jsonfile> -s <schemafile>
```

### In other applications
```python
>>> import omdata
```

## ToDo

* Publishing the Docstring documentation on GitHub pages
* Editing functionalities on a given schema file

---------------
Learn more about the [OpenMaker project](http://openmaker.eu/).

---------------

