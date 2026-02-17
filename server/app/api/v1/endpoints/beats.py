from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse
from app.models.beat import BeatGenerationRequest
from app.services.generator.simple import SimpleBeatGenerator
from app.services.midi import MidiService
import io

router = APIRouter()

# Dependency Injection for the generator
def get_beat_generator():
    return SimpleBeatGenerator()

@router.post("/generate", response_class=StreamingResponse)
async def generate_beat(
    request: BeatGenerationRequest,
    generator: SimpleBeatGenerator = Depends(get_beat_generator)
):
    """
    Generate a drum beat in MIDI format based on BPM and bars.
    """
    try:
        # Generate the beat using the service
        # Logic is separated from API
        pm = generator.generate(request.bpm, request.bars)
        
        # Convert to bytes for download
        midi_data = MidiService.to_bytes(pm)
        
        # Create a filename
        filename = f"beat_{request.bpm}bpm_{request.bars}bars.mid"
        
        return StreamingResponse(
            midi_data, 
            media_type="audio/midi",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
