from sklearn import tree

models = {
    'DTGC': tree.DecisionTreeClassifier(criterion='gini'),
    'DTEC': tree.DecisionTreeClassifier(criterion='entropy'),

}