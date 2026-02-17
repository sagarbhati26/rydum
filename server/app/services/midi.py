import pretty_midi
import io

class MidiService:
    @staticmethod
    def to_bytes(pm: pretty_midi.PrettyMIDI) -> io.BytesIO:
        """
        Convert PrettyMIDI object to a bytes buffer.
        """
        midi_data = io.BytesIO()
        pm.write(midi_data)
        midi_data.seek(0)
        return midi_data

    @staticmethod
    def save_to_file(pm: pretty_midi.PrettyMIDI, filename: str):
        """
        Save PrettyMIDI object to a file.
        """
        pm.write(filename)
