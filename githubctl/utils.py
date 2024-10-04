import csv
import sys
import json
import pydoc

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

        for col in headers:
            table.add_column(str(col))

        for d in list_of_dict:
            table.add_row(*[str(c) for c in d.values()])

        console = Console()
        # console.print(table)
        pydoc.pager(table)
