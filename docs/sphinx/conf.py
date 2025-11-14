import re
import shutil
from datetime import date
from glob import glob
from walkmate import tree

project = "Convert case"
package = "convert-case"
version = "1.2.3"

project_copyright = f"{date.today().year} Joel Lefkowitz"

extensions = [
    "autoapi.extension",
    "myst_parser",
    "sphinxext.opengraph",
]

autoapi_dirs = ["../../src"]
autoapi_options = [
    "members",
    "private-members",
    "show-inheritance",
    "undoc-members",
]

myst_all_links_external = True

theme = {
    "color-problematic": "#4165FF",
    "color-brand-content": "#4165FF",
    "color-brand-primary": "#914FF5",
    "font-stack": "Space Grotesk, sans-serif",
    "font-stack--monospace": "CQ Mono, monospace",
}

html_theme = "furo"
html_title = project
html_static_path = [""]
html_js_files = ["scripts.js"]
html_css_files = ["styles.css"]
html_theme_options = {
    "light_css_variables": {
        **theme,
        "color-highlight-on-target": "#E0E0E0",
    },
    "dark_css_variables": {
        **theme,
        "color-highlight-on-target": "#202020",
    },
}


def build(app, build):
    shutil.copytree("docs/images", "docs/dist/docs/images", dirs_exist_ok=True)
    shutil.move("docs/dist/autoapi/src", f"docs/dist/autoapi/{package}")

    pattern = re.compile(r"src(?!\=)")

    for file in [*tree("docs/dist", r"\.html"), "docs/dist/searchindex.js"]:
        with open(file, "r", encoding="utf8") as stream:
            text = pattern.sub(package, stream.read())

        with open(file, "w", encoding="utf8") as stream:
            stream.write(text)

    for path in glob(f"*.md"):
        shutil.copyfile(path, f"docs/dist/{path}")


def setup(app):
    app.connect("build-finished", build)
