class AdaptiveLearning:
    def __init__(self, model):
        self.model = model

    def continuous_learning(self, data, labels):
        print("Continuous learning process initiated.")
        self.model.fit(data, labels, epochs=5)
        print("Model has adapted with new data.")
