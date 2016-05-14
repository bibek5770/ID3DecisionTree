#############################
# Bibek Gautam              #
# Decision Tree ID3 learner #
# CMPS:470                  #
############################
from DecisionTreeAlgorithm import decisionTreeLearner

trainingExample=[]
inputfile = raw_input("Enter the fileName to learn from:\n1. iris.in\n2.PreprocessedIris.txt\n3.PlayGolf.txt\n4.PlayGolfTest.txt"
                      "\n\tOr Enter Full Path of the file\n=>")
with open(inputfile) as f:
    num_examples = int(f.readline().rstrip())
    num_attributes = int(f.readline().rstrip())
    attributes = (f.readline().rstrip().split(','))
    attributes.append("Target")
    for line in f:
         trainingExample.append(line.lower().rstrip().replace(" ","").split(','))
    print "Learning from: " + inputfile +"\n"
    decisionTreeLearner(attributes).start(trainingExample,attributes)

print "\nThe result is in file out.txt"








