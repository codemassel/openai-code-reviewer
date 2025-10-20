from fastapi import FastAPI
from ai_analyzer import AIAnalyzer
from code_parser import CodeParser
from report_builder import ReportBuilder
from src.routers import summarizer_router
from fastapi.middleware.cors import CORSMiddleware
import logging
import os

app = FastAPI(title="AI Code Reviewer")
app.include_router(summarizer_router.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def root():
    return {"message": "Welcome to the OpenAI Code Reviewer!"}

@app.get("/analyze")
def analyze_repo(owner: str, repo: str):
    logger.info(f"Analysiere Repository: {owner}/{repo}")

    parser = CodeParser(owner, repo)
    analyzer = AIAnalyzer()
    report_builder = ReportBuilder()

    try:
        code_files = parser.fetch_code_files()
        logger.info(f"{len(code_files)} Dateien gefunden. Analysiere...")

        analyses = []
        for file_name, content in code_files.items():
            feedback = analyzer.analyze_code(content, file_name)
            analyses.append(feedback)

        report = report_builder.build_markdown_report(owner, repo, analyses)

        report_path = os.path.join(os.getcwd(), f"{repo}_AI_Code_Report.md")
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report)

        return {"message": "Analyse abgeschlossen!", "report_file": report_path}
    except Exception as e:
        logger.error(f"Fehler bei der Analyse: {e}")
        return {"error": str(e)}
