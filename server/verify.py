import requests
import os
import time
import subprocess
import sys

def verify_api():
    print("Starting verification...")
    
    # Ensure server is running (we will run it separately)
    url = "http://127.0.0.1:8000/api/v1/beats/generate"
    payload = {
        "bpm": 120,
        "bars": 4
    }
    
    try:
        print(f"Sending request to {url}...")
        response = requests.post(url, json=payload, stream=True)
        
        if response.status_code == 200:
            print("Success! Request returned 200 OK.")
            
            # Save the file
            filename = "test_beat.mid"
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"File saved to {filename}")
            
            # Check if file is valid MIDI (simple check)
            file_size = os.path.getsize(filename)
            print(f"File size: {file_size} bytes")
            
            if file_size > 0:
                print("Verification passed! MIDI file generated.")
                # Optional: use pretty_midi to load it back and check
                import pretty_midi
                try:
                    pm = pretty_midi.PrettyMIDI(filename)
                    print(f"Loaded MIDI file. Instruments: {len(pm.instruments)}")
                    print(f"First instrument: {pm.instruments[0].name}")
                    print(f"Total notes: {len(pm.instruments[0].notes)}")
                except Exception as e:
                    print(f"Failed to parse generated MIDI: {e}")
            else:
                print("Verification failed: File is empty.")
                
        else:
            print(f"Request failed with status: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("Could not connect to server. Make sure it is running.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    verify_api()
