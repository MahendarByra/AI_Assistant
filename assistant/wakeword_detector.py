import pvporcupine
import pyaudio
import struct
from assistant.voice_engine import speak_direct


def listen_for_wakeword():
    # Initialize Porcupine with built-in keyword 'jarvis'
    porcupine = pvporcupine.create(
        access_key="HV5xZRKBYsMg3bNTHFOSDfHqidbHluk8kLAplAKKykJNkQCScpgfLA==",
        keywords=["jarvis"]
    )
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("Listening for wake word 'Jarvis'...")

    try:
        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm_unpacked = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm_unpacked)

            if keyword_index >= 0:
                print("Jarvis : Voice Detection Successful!")
                speak_direct("Voice Detection Successful!")
                break

    finally:
        audio_stream.stop_stream()
        audio_stream.close()
        pa.terminate()
        porcupine.delete()
