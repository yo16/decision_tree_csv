from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

from .test_datas import get_moons

def do_test():
    moons = get_moons()
    X = moons[0]
    Y = moons[1]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0, stratify=Y)
    
    # sklearn.tree.DecisionTreeClassifier
    # https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
    clf_model = DecisionTreeClassifier(max_depth=3)
    clf_model.fit(X_train, Y_train)
    print(clf_model.score(X_test, Y_test))




