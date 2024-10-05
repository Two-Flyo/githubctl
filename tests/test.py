import sys
import io
import os
import mdv
import pydoc

# 强制 Python 的 stdout 使用 UTF-8 编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def render_markdown_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            markdown_content = file.read()

        rendered = mdv.main(markdown_content)
        os.environ["LESS"] = "-R"
        pydoc.pager(rendered)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    filename = "input.md"
    render_markdown_file(filename)


# import subprocess
# import mdv


# def render_markdown_file(filename):
#     try:
#         # 打开并读取 Markdown 文件
#         with open(filename, "r", encoding="utf-8") as file:
#             markdown_content = file.read()

#         # 使用 mdv 渲染 Markdown
#         rendered = mdv.main(markdown_content)

#         # 使用 subprocess 调用 less 来分页显示渲染结果
#         proc = subprocess.Popen(["less", "-R"], stdin=subprocess.PIPE, encoding="utf-8")
#         proc.communicate(input=rendered)

#     except Exception as e:
#         print(f"Error: {e}")


# if __name__ == "__main__":
#     filename = "input.md"
#     render_markdown_file(filename)


# from rich.console import Console
# from rich.markdown import Markdown

# console = Console()

# with open("input.md", "r") as md_file:
#     markdown = Markdown(md_file.read())
# console.print(markdown)

# import jmespath
# import json

# from rich import print

# with open("people.json") as f:
#     people = json.load(f)
#     # print(people)

# search = "people[?(age==`28`)]"

# print(jmespath.search(search, people))
