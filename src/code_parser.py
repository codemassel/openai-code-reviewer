from github import Github
import os
import logging

logger = logging.getLogger(__name__)

class CodeParser:
    def __init__(self, owner, repo_name):
        self.owner = owner
        self.repo_name = repo_name
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.client = Github(self.github_token)

    def fetch_code_files(self):
        repo = self.client.get_repo(f"{self.owner}/{self.repo_name}")
        contents = repo.get_contents("")
        code_files = {}

        def process_dir(items):
            for item in items:
                if item.type == "dir":
                    process_dir(repo.get_contents(item.path))
                elif item.name.endswith(".py"):
                    logger.info(f"Code-Datei gefunden: {item.path}")
                    code_files[item.path] = item.decoded_content.decode("utf-8")

        process_dir(contents)
        return code_files
