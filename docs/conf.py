import os
import sys
from datetime import datetime

# -- Project information -----------------------------------------------------
project = 'Handwritten Graph Library'
copyright = f'{datetime.now().year}, Lilanga Gamage'
author = 'Lilanga Gamage'
release = '1.0.5'
version = '1.0.5'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'sphinx_tabs.tabs',
    'myst_parser',
    'sphinx_design',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_build', 
    'Thumbs.db', 
    '.DS_Store',
    'node_modules',           # Exclude npm dependencies
    'node_modules/**',        # Exclude all npm subdirectories  
    '**node_modules**',       # Exclude node_modules anywhere
    '*.md',                   # Exclude markdown files from npm packages
    'package*.json',          # Exclude npm package files
    '.git',                   # Exclude git directory
    '.gitignore',             # Exclude git files
    '**/*.log',               # Exclude log files
    'yarn.lock',              # Exclude yarn lock file
    'package-lock.json'       # Exclude npm lock file
]

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'
html_title = "Handwritten Graph Library Documentation"

html_theme_options = {
    "sidebar_hide_name": True,
    "source_repository": "https://github.com/Lilanga/handwritten-graph-docs/",
    "source_branch": "main",
    "source_directory": "docs/",
}

html_static_path = ['_static']

# -- Options for MyST parser ------------------------------------------------
# FIXED: Removed 'linkify' which requires additional dependency
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    # "linkify",  # Removed - requires linkify-it-py
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# -- Options for copy button ------------------------------------------------
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# -- Options for intersphinx -------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# Reduce intersphinx timeout and suppress warnings
intersphinx_timeout = 5
suppress_warnings = [
    'ref.python',
    'toc.not_readable',      # Suppress "document isn't included in any toctree"
    'toc.excluded',          # Suppress excluded document warnings
]

# -- Options for autodoc -----------------------------------------------------
autodoc_typehints = "description"
autodoc_member_order = "bysource"

# -- REMOVED: rst_prolog that was causing substitution errors ---------------
# The substitution definitions were causing illegal element errors
# We'll use direct links in the documentation instead

# -- Setup function ----------------------------------------------------------
def setup(app):
    # Only add CSS if file exists
    css_file = os.path.join(app.srcdir, '_static', 'custom.css')
    if os.path.exists(css_file):
        app.add_css_file('custom.css')
    
    # Only add JS if file exists  
    js_file = os.path.join(app.srcdir, '_static', 'custom.js')
    if os.path.exists(js_file):
        app.add_js_file('custom.js')