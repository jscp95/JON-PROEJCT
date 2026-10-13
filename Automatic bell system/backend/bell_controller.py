import threading
from playsound3 import playsound

class BellController:
    def __init__(self, sound_file="assets/bell.mp3"):
        self.sound_file = sound_file
        self.current_sound = None
        self.ringing = False

    def ring_bell(self, duration=10):
        if self.ringing:
            return

        self.ringing = True
        threading.Thread(target=self._play_bell, args=(duration,), daemon=True).start()

    def _play_bell(self, duration):
        end_time = duration

        try:
            self.current_sound = playsound(
                self.sound_file,
                block=False
            )

            # For a simple version, play one bell sound.
            # If your bell.mp3 is shorter than the required duration,
            # repeat it until duration ends.
            import time
            start = time.time()

            while time.time() - start < end_time and self.ringing:
                if self.current_sound and not self.current_sound.is_alive():
                    self.current_sound = playsound(
                        self.sound_file,
                        block=False
                    )
                time.sleep(0.2)

        except Exception as e:
            print("Bell playback error:", e)

        finally:
            self.ringing = False

    def stop_bell(self):
        self.ringing = False

        if self.current_sound:
            try:
                self.current_sound.stop()
            except Exception:
                pass
