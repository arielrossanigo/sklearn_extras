from sklearn.base import BaseEstimator, TransformerMixin


class DataFrameColumnExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        if type(columns) is str:
            columns = [columns]
        self.columns = columns

    def fit(self, x, y=None):
        return self

    def transform(self, dataframe):
        return dataframe[self.columns]
