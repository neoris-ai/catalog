# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

TITLE = "Solutions Catalog"
project = 'solutions-catalog'
copyright = '2023, neoris-ai'
author = 'neoris-ai'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_static_path = ['_static']

## monokai, sphinx, native
pygments_style = 'sphinx'                                                                                                                     
todo_include_todos = True

# rtd theme
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {"collapse_navigation": False,
                      "style_external_links": True,
                      'logo_only': True,
                      'style_nav_header_background': '#000000',
                      }

# pdj_theme
#import sphinx_pdj_theme
#html_theme = 'sphinx_pdj_theme'
#html_theme_path = [sphinx_pdj_theme.get_html_theme_path()]

html_title = TITLE
html_logo = os.path.join('images', "neoris-logo-1.png")
html_show_copyright = False
html_show_sourcelink = False