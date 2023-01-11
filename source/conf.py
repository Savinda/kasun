# Configuration file for the Sphinx documentation builder.

import os
import sys

# Created directives inside _ext folder 
sys.path.append(os.path.abspath("./_ext"))


# Add all your newly created extensions here
extensions = ['rightquote', 'sphinx_carousel.carousel', 'redsection']

#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'python sphinx project'
copyright = '2023'
author = 'kasun'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
