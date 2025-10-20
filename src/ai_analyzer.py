from openai import OpenAI
import os
import logging

logger = logging.getLogger(__name__)

class AIAnalyzer:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def analyze_code(self, code: str, file_name: str):
        logger.info(f"Analysiere Datei mit AI: {file_name}")

        prompt = f"""
        Analysiere den folgenden Python-Code auf Probleme, schlechte Praktiken und mögliche Verbesserungen.
        Gib klare, prägnante Vorschläge in Markdown aus.

        Datei: {file_name}
        Code:
        ```python
        {code}
        ```
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",  # kann später auf GPT-5 oder GPT-4o geändert werden
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
            )
            return f"### {file_name}\n{response.choices[0].message.content}\n"
        except Exception as e:
            logger.error(f"Fehler bei AI-Analyse: {e}")
            return f"### {file_name}\nFehler bei der Analyse: {e}\n"
