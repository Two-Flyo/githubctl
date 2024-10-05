import typer
import jmespath

from githubctl.options import OutputOption
from githubctl.github import GithubAPI
from githubctl.utils import sort_by_key, print_beauty


repo_app = typer.Typer()


@repo_app.command(name="list")
def list_repos(
    user: str = typer.Option(..., "--user", "-u", help="github user name"),
    output: OutputOption = typer.Option(
        OutputOption.table, "--output", "-o", help="format output"
    ),
    query: str = typer.Option(None, "--query", "-q", help="query with jmespath"),
    sort_by: str = typer.Option(None, "--sort-by", "-s", help="sort by keys"),
):
    """
    list all repositories for a user

    githubctl repo list -u [username] --output=[table/json/csv] --sort-by=[stars/...]
    """
    github_api = GithubAPI()
    repo = github_api.get_all_user_repositories(username=user)
    if query:
        repo = jmespath.search(query, repo)
    if sort_by:
        if sort_by.startswith("~"):
            reverse = True
            sort_by = sort_by[1:].split(",")
        else:
            reverse = False
        repo = sort_by_key(list_of_dict=repo, key_list=sort_by, reverse=reverse)
    print_beauty(list_of_dict=repo, output=output)


@repo_app.command(name="delete", help="delete repository")
def delete_repo(
    user: str = typer.Option(..., "--user", "-u", help="github user name"),
    repo: str = typer.Option(..., "--repo", "-r", help="repository name"),
):
    github_api = GithubAPI()
    if github_api.delete_repository_for_user(username=user, repo_name=repo):
        print(f"repository {repo} was deleted!")
    else:
        print(f"repository {repo} not found!")
