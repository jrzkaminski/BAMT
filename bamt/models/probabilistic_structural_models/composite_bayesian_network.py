from .bayesian_network import BayesianNetwork


class CompositeBayesianNetwork(BayesianNetwork):
    def __init__(self):
        super().__init__()

    def fit(self):
        pass

    def predict(self):
        pass

    def sample(self):
        pass

    def __str__(self):
        return "Composite Bayesian Network"