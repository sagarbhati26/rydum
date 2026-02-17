import pretty_midi
from typing import Dict, List
from app.services.generator.base import BeatGenerator

class DrumPattern:
    """
    Represents a rhythmic pattern for a drum kit.
    Hits are defined as 16th note steps (0-15 per bar).
    """
    def __init__(self, name: str, kick: List[int], snare: List[int], hihat: List[int]):
        self.name = name
        self.kick = kick
        self.snare = snare
        self.hihat = hihat

    @staticmethod
    def basic_rock() -> 'DrumPattern':
        """
        Standard Rock Beat:
        Kick: 1, 3 (steps 0, 8)
        Snare: 2, 4 (steps 4, 12)
        Hi-hat: 8th notes (0, 2, 4, ... 14)
        """
        return DrumPattern(
            name="Basic Rock",
            kick=[0, 8],
            snare=[4, 12],
            hihat=[0, 2, 4, 6, 8, 10, 12, 14]
        )

    @staticmethod
    def house() -> 'DrumPattern':
        """
        House Beat (4-on-the-floor):
        Kick: 1, 2, 3, 4 (steps 0, 4, 8, 12)
        Snare/Clap: 2, 4 (steps 4, 12)
        Hi-hat: Off-beats (steps 2, 6, 10, 14)
        """
        return DrumPattern(
            name="House",
            kick=[0, 4, 8, 12],
            snare=[4, 12],
            hihat=[2, 6, 10, 14]
        )

    @staticmethod
    def hiphop() -> 'DrumPattern':
        """
        Basic Hip Hop / Boom Bap:
        Kick: Syncopated (0, 7, 10)
        Snare: 2, 4 (4, 12)
        Hi-hat: 8th notes
        """
        return DrumPattern(
            name="Hip Hop",
            kick=[0, 7, 10], 
            snare=[4, 12],
            hihat=[0, 2, 4, 6, 8, 10, 12, 14]
        )

class SimpleBeatGenerator(BeatGenerator):
    """
    A rule-based beat generator using data-driven patterns.
    This separates the 'composition' (Pattern) from the 'rendering' (MIDI generation).
    """
    
    def generate(self, bpm: int, bars: int, **kwargs) -> pretty_midi.PrettyMIDI:
        # Get pattern from kwargs or default to basic rock
        pattern_name = kwargs.get('style', 'basic_rock')
        
        if pattern_name == 'house':
            pattern = DrumPattern.house()
        elif pattern_name == 'hiphop':
            pattern = DrumPattern.hiphop()
        else:
            pattern = DrumPattern.basic_rock()
        
        # Create MIDI object
        pm = pretty_midi.PrettyMIDI(initial_tempo=bpm)
        inst = pretty_midi.Instrument(program=0, is_drum=True, name="Drum Kit")
        
        # Constants
        SECONDS_PER_BEAT = 60.0 / bpm
        SECONDS_PER_16TH = SECONDS_PER_BEAT / 4
        
        STEPS_PER_BAR = 16
        
        # Velocity mappings (could be randomized later for 'humanization')
        VELOCITY_KICK = 100
        VELOCITY_SNARE = 100
        VELOCITY_HIHAT = 80
        
        # MIDI Note mappings (General MIDI)
        NOTE_KICK = 36
        NOTE_SNARE = 38
        NOTE_HIHAT = 42
        
        current_time = 0.0
        
        for bar in range(bars):
            bar_start_time = bar * STEPS_PER_BAR * SECONDS_PER_16TH
            
            # Helper to add notes
            def add_notes(steps: List[int], note_number: int, velocity: int):
                for step in steps:
                    start = bar_start_time + (step * SECONDS_PER_16TH)
                    end = start + 0.1 # Short duration for drums
                    note = pretty_midi.Note(
                        velocity=velocity, 
                        pitch=note_number, 
                        start=start, 
                        end=end
                    )
                    inst.notes.append(note)

            # Apply pattern
            add_notes(pattern.kick, NOTE_KICK, VELOCITY_KICK)
            add_notes(pattern.snare, NOTE_SNARE, VELOCITY_SNARE)
            add_notes(pattern.hihat, NOTE_HIHAT, VELOCITY_HIHAT)
            
        pm.instruments.append(inst)
        return pm
