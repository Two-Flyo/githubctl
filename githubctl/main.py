import os
import typer
import pydoc

from dotenv import load_dotenv
from rich import print

from github import get_all_user_repositories
from utils import print_beauty
from options import OutputOption

if os.path.isfile(".env"):
    load_dotenv()

# # test
# print(f"github token = {os.environ.get("GITHUB_TOKEN")}")

app = typer.Typer()

repo_app = typer.Typer()

app.add_typer(repo_app, name="repo")


@repo_app.command(name="list", help="list user repository")
def list_repos(
    user: str = typer.Option(..., "--user", "-u", help="github user name"),
    output: OutputOption = typer.Option(
        OutputOption.json, "--output", "-o", help="format output"
    ),
):
    repo = get_all_user_repositories(username=user)
    print_beauty(list_of_dict=repo, output=output)


if __name__ == "__main__":
    app()
