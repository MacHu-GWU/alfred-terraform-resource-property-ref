# -*- coding: utf-8 -*-

import json
import markdown
from pathlib_mate import PathCls as Path

providers = [
    {
        "repo_name": "terraform-provider-aws",
        "provider_name": "aws",
        "dataset_name": "tf-aws",
    },
    {
        "repo_name": "terraform-provider-azurerm",
        "provider_name": "azurerm",
        "dataset_name": "tf-azure",
    },
    {
        "repo_name": "terraform-provider-google",
        "provider_name": "google",
        "dataset_name": "tf-gcp",
    },
]

item_types = [
    {
        "item_type": "Res",  # Resource
        "folder_name": "r",
        "url_key": "resources",
    },
    {
        "item_type": "DS",  # Data Source
        "folder_name": "d",
        "url_key": "data-sources",
    },
]

HERE = Path(__file__).parent
HOME = Path.home()

md = markdown.Markdown(extensions=["full_yaml_metadata"])

for dct in providers:
    repo_name = dct["repo_name"]
    provider_name = dct["provider_name"]
    dataset_name = dct["dataset_name"]

    p_data_source = Path(HERE, repo_name, "website", "docs", "d")

    alfred_data = list()
    alfred_settings_data = {
        "columns": [
            {
                "name": "title",
                "ngram_maxsize": 10,
                "ngram_minsize": 2,
                "type_is_ngram": True
            },
            {
                "name": "subtitle",
                "type_is_store": True
            },
            {
                "name": "arg",
                "type_is_store": True
            },
            {
                "name": "autocomplete",
                "type_is_store": True
            }
        ],
        "title_field": "{title}",
        "subtitle_field": "{subtitle}",
        "arg_field": "{arg}",
        "autocomplete_field": "{autocomplete}",
    }

    for item_type_dct in item_types:
        item_type = item_type_dct["item_type"]
        folder_name = item_type_dct["folder_name"]
        url_key = item_type_dct["url_key"]

        markdown_dir = Path(HERE, repo_name, "website", "docs", folder_name)

        for p in markdown_dir.select_by_ext(".markdown"):
            item_name = p.basename.split(".")[0]

            content = p.read_text()
            md.convert(content)
            subcategory = md.Meta["subcategory"]
            description = md.Meta["description"]

            title = f"{item_type}: {subcategory} | {item_name}"
            subtitle = description
            arg = f"https://registry.terraform.io/providers/hashicorp/{provider_name}/latest/docs/{url_key}/{item_name}"
            autocomplete = f"{item_type} {subcategory} {item_name}"
            dct = dict(title=title, subtitle=subtitle, arg=arg, autocomplete=autocomplete)
            alfred_data.append(dct)

    p_alfred_data = Path(HOME, ".alfred-fts", f"{dataset_name}.json")
    p_alfred_setting_data = Path(HOME, ".alfred-fts", f"{dataset_name}-setting.json")

    p_alfred_data.write_text(json.dumps(alfred_data, indent=4))
    p_alfred_setting_data.write_text(json.dumps(alfred_settings_data, indent=4))
