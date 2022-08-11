# CETONI Elements Manual Source

Sphinx source code for CETONI Elements Manual documentation

## Building

Create a virtual environment for a project:

```bash
cd project_folder
virtualenv venv
````

Activate the virtual environment

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv/Scripts/activate
```
Then install the Python requirements:

```bash
pip install -r requirements.txt
```

To build the documentation, execute:

```bash
make_all.bat
```

## Adding requirements

```bash
pip freeze > requirements.txt
```
