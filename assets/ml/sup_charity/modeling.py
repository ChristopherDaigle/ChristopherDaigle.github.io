__author__ = 'Chris_Daigle'
import pandas as pd
import numpy as np
from time import time
from sklearn.metrics import fbeta_score, accuracy_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


def eng_pipe(data):
    """
    Pipeline for completing all transformations
    :param data: pandas dataframe
    """
    # Separate, 2.1 in DE
    Y = data['income']
    X = data.drop('income', axis=1)

    # One-hot-encoding, 2.2 in DE
    factors = ['age', 'workclass', 'education_level', 'education_num',
               'marital_status', 'occupation', 'relationship', 'race',
               'sex', 'capital_gain', 'capital_loss', 'hours_per_week',
               'native_country']
    X = pd.get_dummies(X[factors], drop_first=True)                     # Remove the base case and make dummies
    Y = (Y == '>50K').apply(lambda x: x * 1)                            # Assign positive class

    # Logarithmic transform of skewed factors, 2.2.2 in DE
    skewed = ['capital_gain', 'capital_loss']
    X_log_transformed = pd.DataFrame(data=X).copy()
    X_log_transformed[skewed] = X[skewed].apply(lambda x: np.log(x + 1))

    # Normalization, 2.2.4 in DE
    scaler = MinMaxScaler(feature_range=(0, 1))                         # default=(0, 1)
    numerical = ['age', 'education_num', 'capital_gain', 'capital_loss', 'hours_per_week']
    X_log_minmax = pd.DataFrame(data=X_log_transformed).copy()
    X_log_minmax[numerical] = scaler.fit_transform(X_log_transformed[numerical])

    # Final data:
    X_trans = X_log_minmax

    # Split, 2.3 in DE
    X_train, X_test, y_train, y_test = train_test_split(X_trans, Y, random_state=0, test_size=0.2, stratify=Y)

    return X_trans, X_train, X_test, y_train, y_test


def full_train_predict(learner, x_train, y_train, x_test, y_test):
    """
    Pipeline to train, predict, and score algorithms

    :param learner: the learning algorithm to be trained and predicted on
    :param x_train: features training set
    :param y_train: income training set
    :param x_test: features testing set
    :param y_test: income testing set

    :return results: f-0.5 score, 0.5 chosen for high precision, avoiding false positives
    """
    results = {}

    # Fitting
    start = time()                                              # Get start time
    learner.fit(x_train, y_train)                               # Train model
    end = time()                                                # Get end time
    results['train_time'] = end - start                         # Calculate the training time

    # Predicting
    start = time()                                              # Get start time
    predictions_test = learner.predict(x_test)
    predictions_train = learner.predict(x_train)
    end = time()                                                # Get end time
    results['pred_time'] = end - start                          # Calculate the total prediction time

    # Scoring
    results['acc_train'] = accuracy_score(y_train, predictions_train)               # Training accuracy
    results['acc_test'] = accuracy_score(y_test, predictions_test)                  # Testing accuracy
    results['f_train'] = fbeta_score(y_train, predictions_train, beta=0.5)          # Training F-0.5 score
    results['f_test'] = fbeta_score(y_test, predictions_test, beta=0.5)             # Testing F-0.5 score

    # User feedback
    learner_name = learner.__class__.__name__,
    sample_size = len(x_train)
    factor_size = len(x_train.columns)
    print("{} trained on {} samples over {} factors.".format(learner_name, sample_size, factor_size))

    return results
