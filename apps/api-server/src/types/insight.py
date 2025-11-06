from pydantic import BaseModel, UUID4, Field, HttpUrl
from typing import Literal

class InsightRequest(BaseModel):
    insight_type: Literal['summary', 'all']
    doc_location: HttpUrl
    user_id: UUID4