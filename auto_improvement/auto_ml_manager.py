from keras_tuner import Hyperband

class AutoMLManager:
    def __init__(self, model_builder):
        self.model_builder = model_builder

    def optimize_model(self, x_train, y_train, x_val, y_val):
        tuner = Hyperband(
            self.model_builder,
            objective='val_accuracy',
            max_epochs=10,
            directory='auto_ml_dir',
            project_name='auto_ml_optimization'
        )
        tuner.search(x_train, y_train, epochs=5, validation_data=(x_val, y_val))
        best_model = tuner.get_best_models(num_models=1)[0]
        return best_model
