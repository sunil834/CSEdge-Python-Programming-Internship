#Voice Recorder with PyAudio
# Required Modules
import pyaudio
import wave
import soundfile as sf
from pydub import AudioSegment

# Basic Params
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

# Record audio
def record_audio(filename=WAVE_OUTPUT_FILENAME, record_seconds=RECORD_SECONDS):
    audio = pyaudio.PyAudio()
    
    # Start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Recording...")
    
    frames = []
    
    try:
        for _ in range(0, int(RATE / CHUNK * record_seconds)):
            data = stream.read(CHUNK)
            frames.append(data)
    except Exception as e:
        print(f"An error occurred while recording: {e}")
    finally:
        print("Finished recording.")
    
        # Stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()
    
        # Save the recording
        wf = wave.open(filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

# Audio Playback
def playback_audio(filename=WAVE_OUTPUT_FILENAME):
    wf = wave.open(filename, 'rb')
    
    audio = pyaudio.PyAudio()
    
    # Open stream
    stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
    
    # Read data in chunks
    data = wf.readframes(CHUNK)
    
    print("Playing back...")
    try:
        while data:
            stream.write(data)
            data = wf.readframes(CHUNK)
    except Exception as e:
        print(f"An error occurred during playback: {e}")
    finally:
        # Stop stream
        stream.stop_stream()
        stream.close()
        audio.terminate()
        print("Playback finished.")

# Save audio in different formats
def save_audio_in_format(input_filename=WAVE_OUTPUT_FILENAME, output_filename="output.flac", output_format="FLAC"):
    try:
        if output_format.lower() == 'mp3':
            audio = AudioSegment.from_wav(input_filename)
            audio.export(output_filename, format="mp3")
        else:
            data, samplerate = sf.read(input_filename)
            sf.write(output_filename, data, samplerate, format=output_format)
        print(f"Audio saved in {output_format} format as {output_filename}")
    except Exception as e:
        print(f"An error occurred while saving the audio: {e}")

# Main function
def main():
    while True:
        print("\nVoice Recording Application")
        print("1. Record Audio")
        print("2. Playback Audio")
        print("3. Save Audio in Different Format")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                duration = int(input("Enter duration in seconds: "))
                record_audio(record_seconds=duration)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '2':
            playback_audio()
        elif choice == '3':
            format_choice = input("Enter the format to save (e.g., FLAC, MP3): ").upper()
            output_filename = input("Enter the output filename (including extension): ")
            save_audio_in_format(output_filename=output_filename, output_format=format_choice)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Start
if __name__ == "__main__":
    main()