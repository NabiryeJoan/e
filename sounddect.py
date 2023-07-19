# we are trying to make a program that detects sound
# When you run this code, it will continuously listen to the microphone input and print "Sound detected!" whenever it detects a sound event that surpasses the specified threshold (THRESHOLD). 
# The threshold value can be adjusted to change the sensitivity of sound detection. Higher values make it less sensitive, while lower values make it more sensitive. Keep in mind that ambient noise 
# or microphone sensitivity may influence the results.
import pyaudio
import numpy as np

def detect_sound():
    CHUNK = 1024
    RATE = 44100
    THRESHOLD = 0.01  # Adjust this value to change the sensitivity of sound detection

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)

    try:
        print("Listening for sound...")
        while True:
            data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
            rms = np.sqrt(np.mean(np.square(data)))

            if rms > THRESHOLD:
                print("Sound detected!")
            else:
                print("Listening for sound...")

    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    detect_sound()
