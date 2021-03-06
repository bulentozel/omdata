# OpenMaker Community Data Standardization

It aims data standardization and interoperability between oinsight modules and its third party clients. `oinsight` is a set of data mining and machine learning functionalities developed under the OpenMaker Project: [http://openmaker.eu/](http://openmaker.eu/)

#### Current functionalities
Current version provides a set of command-line tools as well as a python module 
* to be able to validate a JSON file against its predesigned schema
* to be able to inspect and query the design of a JSON schema 

## Install

### Via Python's standard distribution channel PyPI 
```bash
pip install omdata
```
### Via its GitHub source 
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

#### Validating a json file against its schema:

```bash
om-json validate -q <jsonfile> -s <schemafile>
```

#### Inspecting top level major fields/dictionary entries of the data file:
```bash
om-schema inspect fields-top -s <schemafile> 
```

#### Listing all -including the nested ones- fields of an expected data file:
```bash
om-schema inspect fields-all -s <schemafile> 
```

#### Listing all required fields of a json file to be generated:
```bash
om-schema inspect fields-required -s <schemafile> 
```

#### Querying description of each fields:
```bash
om-schema inspect questions -s <schemafile> 
```
In the case of OpenMaker survey data implementation this corresponds to a query to see the mapping between a survey question and the corresponding json entry.

### In other applications
```python
>>> import omdata
```
#### For the details see the tutorial on [Jupyter Notebook](https://github.com/bulentozel/omdata/blob/master/tutorial.ipynb)

## ToDo

* Publishing the Docstring documentation on GitHub pages
* Adding editing functionalities on a given schema file
* Updating the test suits for command-line entry points.

------------------------------------------------------------
Learn more about the OpenMaker project: http://openmaker.eu/

------------------------------------------------------------

