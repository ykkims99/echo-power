
import numpy as np
from echo_power.detector import EchoPowerDetector
from echo_power.preprocessor import normalize_signal
from echo_power.relay_control import setup, trigger_relay

# Fake input signal for test
v = np.random.normal(220, 5, 1000)
i = np.random.normal(0.5, 0.1, 1000)
x = normalize_signal(v, i)

setup()
model = EchoPowerDetector("model/echo_power.tflite", "echo_power/config.yaml")
y = model.predict(x)

if y[0][1] > 0.85:  # assuming class 1 is 'abnormal'
    trigger_relay(True)
