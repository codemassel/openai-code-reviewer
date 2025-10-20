def validate_github_input(owner, repo):
    import re
    return bool(re.match(r"^[A-Za-z0-9_.-]+$", owner)) and bool(re.match(r"^[A-Za-z0-9_.-]+$", repo))
