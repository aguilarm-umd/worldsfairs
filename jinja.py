#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

template = env.get_template("browse.html.jinja")

print(template.render({"fairs": [
    {"name": "Fair A", "items": [{"title": "Item 1", "pid": "umd:1"}]},
    {"name": "Fair B & C", "items": [{"title": "Item 2", "pid": "umd:2"}, {"title": "Item <3>", "pid": "umd:3"}]},
    {"name": "Centennial Exhibition (1876 : Philadelphia, Pa.)", "items": [{"title": "Singer still triumphant!", "pid": "umd:127"}]},
    {"name": "Exhibition of Art and Art-Industry (1853 : Dublin, Ireland)",
     "items": [
        {"title": "Exposition interior", "pid": "umd:778"},
        {"title": "Dublin 1853 Main Hall", "pid": "umd:986"},
     ]},
]}))
