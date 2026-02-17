from pydantic import BaseModel, Field

class BeatGenerationRequest(BaseModel):
    bpm: int = Field(..., ge=40, le=200, description="Beats per minute (40-200)")
    bars: int = Field(..., ge=1, le=16, description="Number of bars to generate (1-16)")
    style: str = Field("basic_rock", description="Style of the beat (basic_rock, house, hiphop)")

class BeatGenerationResponse(BaseModel):
    message: str
    download_url: str
