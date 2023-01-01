# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'test-pages'
copyright = '2023 gesshi'
author = 'gesshi'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_static_path = ['_static']
html_css_files = [
]

html_context = {
    'github_user': 'gesshi',
    'github_repo': 'test-pages',
}

html_theme = 'furo'
html_theme_options = {
    "footer_icons": [
    ],
}

myst_enable_extensions = [
    'colon_fence',
    'tasklist',
]

myst_html_meta = {
}
