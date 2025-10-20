import datetime

class ReportBuilder:
    def build_markdown_report(self, owner, repo, analyses):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"# 🧠 AI Code Review Report for {owner}/{repo}\n\n_Generated on {date}_\n\n"
        body = "\n---\n".join(analyses)
        return header + body
