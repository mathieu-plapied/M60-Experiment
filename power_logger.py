import threading
import time
from pynvml import (
    nvmlInit,
    nvmlShutdown,
    nvmlDeviceGetHandleByIndex,
    nvmlDeviceGetPowerUsage,
    NVMLError
)

class PowerLogger:
    def __init__(self, interval=0.2, gpu_index=0):
        self.interval = interval
        self.gpu_index = gpu_index
        self.energy_joules = 0.0
        self._lock = threading.Lock()
        self._stop_event = threading.Event()
        self.thread = None
        self._last_time = None

        nvmlInit()
        self.handle = nvmlDeviceGetHandleByIndex(self.gpu_index)

    def _log_power(self):
        self._last_time = time.monotonic()
        next_sample = self._last_time + self.interval
        while not self._stop_event.is_set():
            try:
                now = time.monotonic()
                delta = now - self._last_time
                self._last_time = now

                power_mw = nvmlDeviceGetPowerUsage(self.handle)
                power_w = power_mw / 1000.0

                with self._lock:
                    self.energy_joules += power_w * delta
            except NVMLError:
                pass

            sleep_time = next_sample - time.monotonic()
            if sleep_time > 0:
                time.sleep(sleep_time)
            next_sample += self.interval

    def start(self):
        if self.thread and self.thread.is_alive():
            return  
        self.reset()
        self._stop_event.clear()
        self.thread = threading.Thread(target=self._log_power, daemon=True)
        self.thread.start()

    def stop(self):
        self._stop_event.set()
        if self.thread:
            self.thread.join()

    def get_energy_joules(self):
        with self._lock:
            return self.energy_joules

    def instant_power_w(self):
        try:
            power_mw = nvmlDeviceGetPowerUsage(self.handle)
            return power_mw / 1000.0
        except NVMLError:
            return None

    def reset(self):
        with self._lock:
            self.energy_joules = 0.0

    def shutdown(self):
        try:
            nvmlShutdown()
        except NVMLError:
            pass

"""
Pour tester
def main():
    nvmlInit()
    ngpu = nvmlDeviceGetCount()
    print(f"[INFO] GPUs détectés : {ngpu}")
    logger = PowerLogger(interval=0.2, gpu_index=0)
    logger.start()
    print("[INFO] Échantillonnage en cours pendant 5 secondes...")

    for i in range(5):
        time.sleep(1)
        inst = logger.instant_power_w()
        energy = logger.get_energy_joules()
        print(f"  t={i+1}s : puissance instantanée = {inst:.1f} W, énergie cumulée = {energy:.2f} J")

    logger.stop()
    print(f"[RESULTAT] Énergie totale mesurée : {logger.get_energy_joules():.2f} J")
    logger.shutdown()

if __name__ == "__main__":
    import threading
    from pynvml import nvmlInit, nvmlDeviceGetCount, nvmlShutdown, nvmlDeviceGetHandleByIndex, nvmlDeviceGetPowerUsage
    main()
"""