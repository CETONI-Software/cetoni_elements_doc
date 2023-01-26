# CETONI Elements Manual Source

Sphinx source code for CETONI Elements Manual documentation

## Building

Create a virtual environment in root folder:

```bash
virtualenv venv
````
Activate the virtual environment

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
.\\venv\\Scripts\\activate
```

Then install the Python requirements:

```bash
pip install -r requirements.txt
```

Build doxygen documentation:

```bash
make_doxygen.bat
```

Build manual:

```bash
cd CETONI_Elements_Manual_DE
make_all.bat
```

## Adding requirements

```bash
pip freeze > requirements.txt
```

## Open Documentation Issues

- added Try /Catch script function for improved error handling
- added Throw Error function to raise errors
- added support for jumping to a script function in script editor by clicking on a log message in the event log
- Log Message Function
- inline JavaScript
