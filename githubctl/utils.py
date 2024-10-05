import csv
import sys
import json
import pydoc
import jmespath

from typing import List
from rich import print_json
from rich.console import Console
from rich.table import Table

from options import OutputOption


def print_beauty(list_of_dict: List[dict], output: OutputOption):
    if output == OutputOption.csv:
        fieldnames = list_of_dict[0].keys()
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list_of_dict)
    elif output == OutputOption.json:
        print_json(json.dumps(list_of_dict))
    elif output == OutputOption.table:
        table = Table()
        headers = list_of_dict[0].keys()
        table.add_column("")
        for col in headers:
            table.add_column(str(col))

        for repo in list_of_dict:
            table.add_row(
                *[str(list_of_dict.index(repo) + 1)] + [str(c) for c in repo.values()]
            )

        console = Console()
        console.print(table)
        # pydoc.pager(table)


def sort_by_key(list_of_dict, key_list, reverse: bool = False):
    key_list.reverse()

    expr = ""
    for key in key_list:
        if not expr:
            expr = f"sort_by(@, &{key})"
        else:
            expr = f"sort_by({expr}, &{key})"

    if reverse:
        expr = f"{expr}.reverse(@)"

    return jmespath.search(expr, list_of_dict)
