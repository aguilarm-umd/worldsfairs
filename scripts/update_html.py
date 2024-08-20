#!/usr/bin/env python

import json
import os
from csv import DictReader

import requests
from bs4 import BeautifulSoup as bs
from bs4 import ResultSet, Tag

path = "html/worldsfairs/result/id/"

with open("data/mappings.json", "r") as f:
    mappings: dict = json.load(f)


def replace_iframe(iframe: Tag):
    id = iframe.get("src").split("/")[-2].replace("fedora2:", "")

    if id not in mappings:
        print(f"No link for {id} was found")
        return

    iiif_link = mappings[id]

    iframe["src"] = iiif_link


def replace_img(parsed_html: bs):
    img_dir = "html/worldsfairs/binaries/content/gallery/worlds-fairs/imgs/"
    relative_path = "../../binaries/content/gallery/worlds-fairs/imgs/"

    tags: ResultSet = [
        t for t in parsed_html.find_all("img") if "fedora2:umd" in t.get("src")
    ]

    tag: Tag
    for tag in tags:
        img_url = tag.get("src")
        r = requests.get(img_url)

        if not r.ok:
            raise Exception(f"Could not retrieve url: {img_url}")

        name = img_url.split("/")[4].replace("fedora2:", "")

        with open(img_dir + name + ".jpg", mode="wb") as f:
            f.write(r.content)

        tag["src"] = relative_path + name + ".jpg"
        tag["style"] = "margin-bottom: 20px;"

    tag.parent["style"] = "text-align: center;"


def add_download_link(parsed_html: bs, filename: str):
    relative_path = "../../binaries/content/gallery/worlds-fairs/essays/"

    with open("data/inventory.csv", "r") as f:
        inventory = DictReader(f)
        row: dict = next(
            (r for r in inventory if r["pid"] == filename.removesuffix(".html"))
        )
        title = row["title"]

    download_link = parsed_html.new_tag(
        name="a",
        attrs={
            "href": relative_path + filename.replace(".html", ".xml"),
            "download": title + ".xml",
        },
    )
    download_link.string = "Download Essay"

    tag = parsed_html.find("div", attrs={"class": "respStmt"})

    tag.insert(2, download_link)


for file in os.listdir(path):
    with open(path + file) as f:
        parsed_html = bs(f, "html.parser")

    iframe = parsed_html.find("iframe")

    # The tei pages don't have iframes
    if iframe is None:
        replace_img(parsed_html)
        add_download_link(parsed_html, file)

    else:
        replace_iframe(iframe)

    with open(path + file, "wb") as f:
        f.write(parsed_html.prettify("utf-8"))
