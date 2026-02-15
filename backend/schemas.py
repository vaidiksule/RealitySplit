from pydantic import BaseModel
from typing import List


class LensFraming(BaseModel):
    lens: str
    body_html: str
    bias_score: int
    emotional_intensity: int
    loaded_language_density: int
    urgency_level: int
    selective_omission_score: int


class HeatmapMetrics(BaseModel):
    emotional: int
    factual_balance: int
    tribal_signals: int
    urgency: int


class AnalyzeRequest(BaseModel):
    article: str


class AnalyzeResponse(BaseModel):
    original: str
    framings: List[LensFraming]
    heatmap: HeatmapMetrics
    polarization_risk: int
    most_manipulative: str
    most_neutral: str
