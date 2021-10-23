"""Mako templates."""
from mako.lookup import TemplateLookup


lookup = TemplateLookup(
    directories=[
        "templates",
    ],
)

example = lookup.get_template("example.mako.txt")
