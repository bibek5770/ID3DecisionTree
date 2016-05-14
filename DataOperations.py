import math
import operator
class Data(object):

    attributeAndIndex=dict()
    width=0

    def __init__(self,attributess):
        for attribute in attributess:
            index = attributess.index(attribute)
            self.attributeAndIndex[attribute] = index

    def getSubset_Example_byValue(self,passed_example, value, attribute):
        index=self.getIndexOf(attribute)
        retval=[]
        for lines in passed_example:
            if(lines[index]==value):
                retval.append(lines)
        return retval

    def getSameClassification(self, examples):
        return examples[0][len(examples[0])-1]

    def getIndexOf(self, find_attribute):
        return self.attributeAndIndex.get(find_attribute)

    def getListOfPossibleChildrenFromAttribute(self,passed_example,passed_attribute):
        x = self.getIndexOf(passed_attribute)
        retVal=[]
        for lines in passed_example:
            retVal.append(lines[int(x)])
        return retVal[:]

    def removeAttribute(self,attributes, remove_attribute):
        if remove_attribute in attributes:
            attributes.remove(remove_attribute)
        return attributes[:]

    def Is_SameClassification(self, parsed_list):
        width = len(parsed_list[0]) - 1
        same = parsed_list[0][width]
        for line in parsed_list:
            if (line[width] != same):
                return False
        return True
    # returns most occuring classification label in example list
    def majority(self, current_examplesList):
        length = len(current_examplesList[0]) - 1
        allAnswer = []
        for current_examplesListe in current_examplesList:
            allAnswer.append(current_examplesListe[length])
        return max(set(allAnswer), key=allAnswer.count)

    #concept from
    ##http: // www.saedsayad.com / decision_tree.htm
    def getBestAttribute(self, predictors, current_attributesList):
        listofTarget=self.getListOfPossibleChildrenFromAttribute(predictors,"Target")# gets list of all target
        indiviudal_target_count = dict.fromkeys(listofTarget, 0.0)
        gain_from_individual_attribute = dict.fromkeys(current_attributesList[:-1],float(0.0))# initialize dict of gain for Attribute
        for attribute in current_attributesList[:-1]:# target not included
            filteredExamplesByAttribute=self.getListOfPossibleChildrenFromAttribute(predictors,attribute)# gets list of all values by attribute
            currentAttributeEntropy=0
            for value in list(set(filteredExamplesByAttribute)):# foreach unique value in the list of values
                subsetByvalueInAttribute=self.getSubset_Example_byValue(predictors,value,attribute)#gets example rows corresponding to the value
                indiviudal_target_count = dict.fromkeys(indiviudal_target_count.iterkeys(), 0)
                for examples in subsetByvalueInAttribute:
                    x=examples[self.width]
                    indiviudal_target_count[x]= indiviudal_target_count.get(x,0) +1
                # gets entropy for current value of attribute and adds it to entropy of other value to get total entopy of attribute
                currentAttributeEntropy+= self.getEntropy(indiviudal_target_count.values()) * \
                                          (float(sum(indiviudal_target_count.values()))/
                                         len(filteredExamplesByAttribute))
            gain_from_individual_attribute[attribute]=self.getEntropy((dict((x,listofTarget.count(x)) for x in set(listofTarget)).values())) - currentAttributeEntropy
        #http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        return max(gain_from_individual_attribute.iteritems(), key=operator.itemgetter(1))[0]

    def getEntropy(self, target_values_with_count=[]):
        total = float(sum(target_values_with_count))
        x=0.0
        for i in target_values_with_count:
            probability_Of_Answer = float(i / total)
            try:
                entropy = math.log(probability_Of_Answer, 2.0)
            except:
                entropy = 0
            x -= float(probability_Of_Answer * entropy)
        return x

