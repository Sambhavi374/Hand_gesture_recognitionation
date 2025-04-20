import numpy as np
import tensorflow as tf




## Recognize the fingure positions/gestures from their history
class PointHistoryClassifier(object):
    def __init__(
        self,
        model_path='model/point_history_classifier/point_history_classifier.tflite',
        score_th=0.5, # Threshold to determine if the result is valid
        invalid_value=0, # The value to return if the result is invalid
        num_threads=1, 
    ):

        # load and prepare the model for inference(predictions)   
        self.interpreter = tf.lite.Interpreter(model_path=model_path,
                                               num_threads=num_threads) #

        self.interpreter.allocate_tensors()

        # get input and output tensors.(details like shape, dtype)
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        self.score_th = score_th
        self.invalid_value = invalid_value



    
    
    def __call__(self,point_history):

        
        input_details_tensor_index = self.input_details[0]['index']

        self.interpreter.set_tensor(
            input_details_tensor_index,
            np.array([point_history], dtype=np.float32))
        self.interpreter.invoke()

        output_details_tensor_index = self.output_details[0]['index']

        result = self.interpreter.get_tensor(output_details_tensor_index)

        result_index = np.argmax(np.squeeze(result))

        if np.squeeze(result)[result_index] < self.score_th:
            result_index = self.invalid_value

        return result_index
