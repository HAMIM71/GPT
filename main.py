from github import Github
import os
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
g = Github(ACCESS_TOKEN)
query = "language: python"
result = g.search_repositories(query)
print(g.get_user())
print(result.totalCount)
