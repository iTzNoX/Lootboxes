import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
name = "Lootboxes",
version = "0.0.1",
author = "iTzNoX",
author_email = "timothykropp39@gmail.com",
description = "A small Lootbox simulator",
long_description = long_description,
long_description_content_type = "text/markdown",
url = "https://github.com/iTzNoX/Lootboxes",
project_urls = {
"Bug Tracker": "https://github.com/iTzNoX/Lootboxes/issues"
},
license="MIT",
python_requires >= "3.11"
)
  
