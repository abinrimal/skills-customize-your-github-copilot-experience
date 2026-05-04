import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix


def load_data(path="sample_data.csv"):
    return pd.read_csv(path)


def preprocess(df):
    # Placeholder preprocessing: drop NA rows and separate features/labels
    df = df.copy()
    df = df.dropna()
    X = df.drop(columns=["label"])
    y = df["label"]
    return X, y


def train_and_evaluate(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    probs = clf.predict_proba(X_test)[:, 1]

    print("Classification report:\n", classification_report(y_test, preds))
    print("ROC AUC:", roc_auc_score(y_test, probs))
    print("Confusion matrix:\n", confusion_matrix(y_test, preds))

    return clf


def main():
    df = load_data()
    X, y = preprocess(df)
    clf = train_and_evaluate(X, y)


if __name__ == "__main__":
    main()
