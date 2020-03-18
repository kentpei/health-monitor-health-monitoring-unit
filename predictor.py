import pandas as pd

# collecting data from the csv file from the database
def Predictor(file):
    try:
        df = pd.read_csv(file+'.csv')
        Pulse = df.iloc[:,0].values
        BloodPressure = df.iloc[:,1].values
        OxygenLevel = df.iloc[:,2].values
        healthPredict(Pulse,BloodPressure,OxygenLevel)   #call the AI function to predict health
    except:
        print("an error occurs")

# making prediction based on the data collect from the Predictor
def healthPredict(Pulse,BloodPressure,OxygenLevel):
    pass   #AI function using pass instead 


## test Predictor("Dataset1")