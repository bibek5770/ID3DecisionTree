from __future__ import print_function

class Preprocessing(object):

    def __init__(self,fileName):
        self.fileName = fileName

    def Preprocessed(self):
        with open(self.fileName, "r") as file_To_Preproces:
            Num_Examples= int(file_To_Preproces.readline().rstrip())
            Num_Attributes= int(file_To_Preproces.readline())
            attributes= file_To_Preproces.readline()
            q = file_To_Preproces.readlines()
            #q = file_To_Preproces.readlines()[3:]
        preprocessed_data=self.preprocess(q)
        with open("PreprocessedIris.txt",'a') as data_file:
            #data_file.write(attributes)
            data_file.write("{0}{1}".format(attributes,preprocessed_data))

    def preprocess( self, lines):
        retVal=""
        ###########################################
        ''' 10= setosa, 11=Versicolor, 12= Virginica'''
        ###########################################
        setosa , Versicolor, Virginica= 10,11,12

        for line in lines:
            line = line.rstrip()
            preprocess_SepalLength, preprocess_SepalWidth, preprocess_PetalLength, preprocess_PetalWidth = 0,0,0,0
            currentline=line.strip().split(",")
            currentLine_sepalLength,currentLine_sepalWidth, currentLine_petalLength, currentLine_petalWidth=float(currentline[0]),float(currentline[1]),float(currentline[2]),float(currentline[3])

            if(currentLine_sepalLength<4.9):
                preprocess_SepalLength = setosa
            elif(currentLine_sepalLength > 7):
                preprocess_SepalLength = Virginica
            elif(currentLine_sepalLength >= 4.9):
                preprocess_SepalLength=currentline[0]

            if(currentLine_sepalWidth > 3.8):
                preprocess_SepalWidth = setosa
            elif(currentLine_sepalWidth < 2.2):
                preprocess_SepalWidth = Versicolor
            elif(currentLine_sepalWidth>= 2.2 and currentLine_sepalWidth<=3.8):
                preprocess_SepalWidth=currentline[1]
                #do nothing if(currentline[0] <4.9):

            if(currentLine_petalLength < 3):
                preprocess_PetalLength = setosa
            elif(currentLine_petalLength>5.1):
                preprocess_PetalLength = Virginica
            elif(currentLine_petalLength>=3 and currentLine_petalLength<4.5):
                preprocess_PetalLength=Versicolor
            elif(currentLine_petalLength >=4.5 and currentLine_petalLength<=5.1):
                preprocess_PetalLength=currentline[2]

            if(currentLine_petalWidth < 1):
                preprocess_PetalWidth = setosa
            elif(currentLine_petalWidth> 1.8):
                preprocess_PetalWidth = Virginica
            elif( currentLine_petalWidth >=1.0 and currentLine_petalWidth <1.4):
                preprocess_PetalWidth=Versicolor
            elif(currentLine_petalWidth>=1.4  and currentLine_petalWidth <=1.8 ):
                preprocess_PetalWidth=currentline[3]

            retVal+="{0}, {1}, {2}, {3}, {4}\n".format(preprocess_SepalLength, preprocess_SepalWidth, preprocess_PetalLength, preprocess_PetalWidth, currentline[4])
        return retVal