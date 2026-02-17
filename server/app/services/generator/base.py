from abc import ABC, abstractmethod
import pretty_midi

class BeatGenerator(ABC):
    """
    Abstract base class for beat generators.
    This allows us to swap out the rule-based generator for an ML model later.
    """
    
    @abstractmethod
    def generate(self, bpm: int, bars: int, **kwargs) -> pretty_midi.PrettyMIDI:
        """
        Generate a beat.
        
        Args:
            bpm: Beats per minute.
            bars: Number of bars to generate.
            **kwargs: Additional parameters (e.g., style, complexity, temperature).
            
        Returns:
            A pretty_midi.PrettyMIDI object containing the generated beat.
        """
        pass
