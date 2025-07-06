class BMI_calculator: #definition of my class BMI_calculator

# A class is a blueprint for a project which in our case is to create an Utility that suggest what class of BMI we are based on weight and height given

# After defining our container (the class) we are going to define what object the container will need to work
    def __init__(self,weight,height): #we call the constructor __init__
        self.weight = weight # we define the first object as the weight in KG
        self.height = height/100 # we define the second object as the height to be input in cm

# As second step we are going to define the action that the 2 object are going to take creating a new method calculate_BMI
    def calculate_BMI(self):
        self.BMI = self.weight/self.height**2
        return self.BMI 
# The second method will assign the class of BMI based on the value of BMI
    def calculate_class(self):
        if self.BMI > 40:
            print(f'Your BMI is {self.BMI} which indicates an Obesity class III')
        elif self.BMI > 35:
            print(f'Your BMI is {self.BMI} which indicates an Obesity class II')
        elif self.BMI > 30:
            print(f'Your BMI is {self.BMI} which indicates an Obesity class I')
        elif self.BMI > 25:
            print(f'Your BMI is {self.BMI} which indicates an Overweighted status')
        elif self.BMI > 18:
            print(f'Your BMI is {self.BMI} which indicates a Normoweighted status')
        elif self.BMI < 18:
            print(f'Your BMI is {self.BMI} which indicates a Underweighted status')

try:
    height = int(input('What is your height in cm?'))
except ValueError:
    print(f'Your height must be in cm')   
try:
    weight = int(input('What is your weight in KG?'))
except ValueError:
    print(f'Your weight must be in KG')
else:
    bmi = BMI_calculator(weight,height)
    bm = bmi.calculate_BMI()
    clas=bmi.calculate_class()

    print(clas)
