from sklearn.preprocessing import LabelBinarizer


class LabelBinarizerForPipelines(LabelBinarizer):

    def fit(self, X, y=None):
        return super().fit(X)

    def transform(self, X, y=None):
        return super().transform(X)

    def fit_transform(self, X, y=None):
        return super().fit_transform(X)
