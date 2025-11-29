#!/bin/env python

import jinja2
import os
from pathlib import Path


if __name__ == "__main__":

    root_dir = Path(__file__).parent
    templates_dir = root_dir / "templates"

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(templates_dir)),
        autoescape=False
    )

    for src_path in templates_dir.rglob("*.html"):
        relative_src_path = src_path.relative_to(templates_dir)

        template = env.get_template(str(relative_src_path))
        content = template.render(
            rel_path=os.path.relpath(".", relative_src_path.parent)
        ).strip()

        dst_path = root_dir / relative_src_path
        print(f"Rendering {dst_path}")
        with open(dst_path, "w") as f:
            f.write(content)
