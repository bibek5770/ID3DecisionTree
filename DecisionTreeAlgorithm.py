from DataOperations import Data
class decisionTreeLearner(object):

    def __init__(self, current_attributesList):
        self.dataset=Data(current_attributesList)
        self.level=0
        self.treeString=[]

    def decision_learning_tree(self, remaining_predictor_set, current_attributes, default=None):
        if not remaining_predictor_set:# if example is null return default
            self.appendString("D: "+default,0)
        elif self.dataset.Is_SameClassification(remaining_predictor_set):# if all examples have the same classification return the clasification
            self.appendString("C: "+self.dataset.getSameClassification(remaining_predictor_set), 0)
        elif not current_attributes:# if attributes == null return majority
            self.appendString("M: "+self.dataset.majority(remaining_predictor_set), 0)
        else:
            bestAttribute=self.dataset.getBestAttribute(remaining_predictor_set, current_attributes)
            childrenList= list(set(self.dataset.getListOfPossibleChildrenFromAttribute(remaining_predictor_set, bestAttribute)))# get unique values from current bestAttribute
            majority = self.dataset.majority(remaining_predictor_set)
            self.appendString(bestAttribute.upper(), 2)
            for child in childrenList:# for each value in unique values
                self.appendString(child.lower(), 2)
                # recursively call itself on subset of (examples and attributes)
                self.decision_learning_tree(self.dataset.getSubset_Example_byValue(remaining_predictor_set, child, bestAttribute),
                                            self.dataset.removeAttribute(current_attributes, bestAttribute), majority)
                self.level -= 2
            self.level -= 2

    def appendString(self, value, level):
        self.treeString.append("{0}{1}".format("||\t" * self.level,value))
        self.level += level

    def start(self, examples, attributes):
        self.dataset.width = len(examples[0]) - 1
        retTree = self.decision_learning_tree(examples, attributes)
        with open("out.txt", 'w+') as f:
            print ("\nD => Default\t C=> Same Classification\t M => Majority")
            for item in self.treeString:
                print item
                f.write(item + "\n")
            print ("D => Default\t C=> Same Classification\t M => Majority")
        return retTree


