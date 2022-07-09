#!/usr/bin/env python3

import logging
from pathlib import Path

try:
    import fire
except ImportError:
    logging.error("pip install fire")
try:
    from mako.lookup import TemplateLookup
    from mako.template import Template
except ImportError:
    logging.error("pip install mako")
try:
    from attrdict import AttrDict as adict
except ImportError:
    logging.error("pip install attrdict3")
try:
    import yaml
except ImportError:
    logging.error("pip install pyyaml")

cwd = Path(__file__).parent


def yaml_load(stream, Loader=yaml.SafeLoader, object_pairs_hook=adict):
    class AttrLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    AttrLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping
    )
    return yaml.load(stream, AttrLoader)


def mwf_gallery_build(tpl_data, yaml_data, css_data=adict({}), img_prefix=None):
    imgs = adict(yaml_load(yaml_data, yaml.SafeLoader))
    if img_prefix:
        imgs = adict(filter(lambda item: item[0].startswith(img_prefix), imgs.items()))
    mako_lookup = TemplateLookup(
        directories=[cwd],
        strict_undefined=True,
    )
    mako_tpl = Template(
        tpl_data,
        input_encoding="utf-8",
        lookup=mako_lookup,
        strict_undefined=True,
    )
    return mako_tpl.render(imgs=imgs, css=css_data)

def mwf_gallery_load(tpl_path, html_path, yaml_path, css_dict={}, img_prefix=None):
    tpl_data = Path(tpl_path).read_text(encoding="utf8")
    css_data = adict(css_dict)
    with open(yaml_path) as yaml_data:
        Path(html_path).write_text(
            mwf_gallery_build(tpl_data, yaml_data, css_data, img_prefix), encoding="utf8"
        )


def main():
    mwf_gallery_load(
        tpl_path=Path(cwd, "mwf_mako_slideshow.html"),
        html_path=Path(cwd, "mwf-slideshow-wf.html"),
        yaml_path=Path(cwd, "mwf_data.yaml"),
        css_dict='{"background_color": "#840d1a", "color": "white", "img": "filter: invert(100%)"}',
    )


def cli():
    fire.core.Display = lambda lines, out: print(*lines, file=out)
    fire.Fire(mwf_gallery_load)


if __name__ == "__main__":
    cli()
