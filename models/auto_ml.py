from keras_tuner import Hyperband

def build_auto_ml_model(hp):
    model = tf.keras.Sequential()
    model.add(layers.Dense(units=hp.Int('units', min_value=32, max_value=512, step=32), activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def auto_ml_tuning(x_train, y_train, x_val, y_val):
    tuner = Hyperband(
        build_auto_ml_model,
        objective='val_accuracy',
        max_epochs=10,
        directory='auto_ml_dir',
        project_name='auto_ml_optimization'
    )
    tuner.search(x_train, y_train, epochs=5, validation_data=(x_val, y_val))
    return tuner.get_best_models(num_models=1)[0]
