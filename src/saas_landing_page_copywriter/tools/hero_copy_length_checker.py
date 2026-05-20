from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class HeroCopyInput(BaseModel):
    headline: str = Field(..., description="Hero headline")
    subheadline: str = Field(..., description="Hero subheadline")


class HeroCopyLengthChecker(BaseTool):
    name: str = "Hero Copy Length Checker"
    description: str = (
        "Checks if headline is under 10 words "
        "and subheadline is under 20 words."
    )

    def _run(self, headline: str, subheadline: str) -> str:
        headline_words = len(headline.split())
        subheadline_words = len(subheadline.split())

        headline_valid = headline_words <= 10
        subheadline_valid = subheadline_words <= 20

        return (
            f"Headline words: {headline_words} "
            f"(Valid: {headline_valid})\n"
            f"Subheadline words: {subheadline_words} "
            f"(Valid: {subheadline_valid})"
        )