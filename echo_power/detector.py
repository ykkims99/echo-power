
import tflite_runtime.interpreter as tflite
import numpy as np
import yaml

class EchoPowerDetector:
    def __init__(self, model_path, config_path):
        self.interpreter = tflite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

    def predict(self, input_tensor):
        input_details = self.interpreter.get_input_details()
        output_details = self.interpreter.get_output_details()
        self.interpreter.set_tensor(input_details[0]['index'], input_tensor)
        self.interpreter.invoke()
        output = self.interpreter.get_tensor(output_details[0]['index'])
        return output
