# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
import sphinx_fontawesome
from sphinx.roles import MenuSelection
import sys
import os


# -- Project information -----------------------------------------------------

project = 'CETONI Elements Manual'
copyright = '2022, CETONI GmbH'
author = 'CETONI GmbH'
html_show_copyright = True
html_show_sphinx = True
html_show_sourcelink = False

# The full version, including alpha/beta/rc tags
release = '20220504'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = [  
#    'breathe', 
#    'myst_parser', 
#    'sphinx.ext.autodoc', 
#    'sphinx.ext.autosummary', 
#    'sphinx_rtd_dark_mode' 
#]


extensions = [  
    'breathe', 
    'myst_parser', 
    'sphinx.ext.autodoc', 
    'sphinx.ext.autosummary',
    'sphinx_rtd_dark_mode',
    'sphinx_fontawesome',
    'sphinx_togglebutton',
    'sphinx.ext.autosectionlabel' 
]

# user starts in, light mode
default_dark_mode = False

# Breathe Configuration
breathe_projects = { 
    "python": "../doxygen/xml"
}
breathe_default_project = "python"
breathe_domain_by_extension = {"h": "cpp"}
breathe_implementation_filename_extensions = ['.c', '.cc', '.cpp']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build', 
    'Thumbs.db', 
    '.DS_Store', 
    'venv', 
    'ReadTheDocs.md',
    'Appendix_EN/content/*'
]

# get environment variables (set as part of make .bat files)
env_private = os.getenv("PRIVATE_DOC", "0")

if env_private == "1":
    print("private build")
    root_doc = 'index_private'
    exclude_patterns.append('index.rst')
else:
    print("public build")
    root_doc = 'index'
    exclude_patterns.append('index_private.rst')
    

# Set a bullet character for :menuselection: role
# easier to identify in non latin languages, e.g. japanese
from sphinx.roles import MenuSelection
#MenuSelection.BULLET_CHARACTER = '\u25BA' #'\N{BLACK RIGHT-POINTING POINTER}'
MenuSelection.BULLET_CHARACTER = '\u2192' #'\N{	rightwards arrow}'

# For inline code highlighting - does not work yet
#rst_prolog = """
#.. role:: python(code)
#    :language: python
#    :class: highlight
#"""

rst_prolog = """
.. role:: guinum
.. role:: step
"""


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# The extension sphinx_rtd_dark_mode provides the theme so theme selection is
# not required here
#html_theme = 'sphinx_typo3_theme'
#html_theme = 'rtd_qgis'
#html_theme = 'sphinx_rtd_theme'


# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#theme-options
# rtd / read the docs theme options:
html_theme_options = {
    # collapse_navigation: With this enabled, navigation entries are not expandable – the [+] icons next to each entry are removed. Default: True
    'collapse_navigation': True,
    # sticky_navigation: Scroll the navigation with the main page content as you scroll the page. Default: True
    'sticky_navigation': True,
    # navigation_depth: The maximum depth of the table of contents tree. Set this to -1 to allow unlimited depth. Default: 4
    'navigation_depth': 4,
    # includehidden:Specifies if the navigation includes hidden table(s) of contents – that is, any toctree directive that is marked with the :hidden: option. Default: True,
    # 'includehidden': True,
    # canonical_url: This will specify a canonical URL meta link element to tell search engines which URL should be ranked as the primary URL for your documentation. This is important if you have multiple URLs that your documentation is available through. The URL points to the root path of the documentation and requires a trailing slash.
    #'canonical_url': 'https://docs.qgis.org/latest/en/',
    # display_version: If True, the version number is shown at the top of the sidebar. Default: True,
    #'display_version': True,
    # logo_only: Only display the logo image, do not display the project name at the top of the sidebar. Default: False,
    'logo_only': False,
    # prev_next_buttons_location': Location to display Next and Previous buttons. This can be either bottom, top, both , or None. Default: 'bottom',
    'prev_next_buttons_location': 'bottom',
    # style_external_links': Add an icon next to external links. Default: False,
    'style_external_links': False,
    # style_nav_header_background': Changes the background of the search area in the navigation bar. The value can be anything valid in a CSS background property. Default: 'white',
    # 'style_nav_header_background': 'Gray',
    # Toc options
    # titles_only: When enabled, page subheadings are not included in the navigation. Default: False
    # 'titles_only': False,
    #'style_nav_header_background': '#ff0000'
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['./themes']



# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'cetoni_style_override_css/style_override.css',
    'cetoni_style_override_css/color_roles.css',
]

html_favicon = '_static/favicon.png'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/logo_cetoni_elements4.svg'
html_title = 'CETONI Elements Manual'
html_last_updated_fmt = '%b %d, %Y %H:%M'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'monokai'

# The name of a reST role to use as the default role, that is, for text marked
# up `like this`. The default role can always be set within individual
# documents using the standard reST default-role directive.
default_role = 'any'

# The default language to highlight source code.
highlight_language = 'cpp'

source_suffix = ['.rst', '.md']

suppress_warnings = ['autosectionlabel.*']

# -- Internationalisation ----------------------------------------------------

language = 'en'
#locale_dirs = ['locale/']   # path is example but recommended.
#gettext_compact = False     # optional.