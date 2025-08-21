# Configuration file for the Sphinx documentation builder.

project = "ServiceX Local"
copyright = (
    "2025 Institute for Research and " "Innovation in Software for High Energy Physics (IRIS-HEP)"
)
author = "Institute for Research and Innovation in Software for High Energy Physics (IRIS-HEP)"
release = "1.0.0"

extensions = [
    "myst_parser",
    "sphinx.ext.doctest",
    "sphinx_copybutton",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

exclude_patterns = []

html_theme = "furo"
