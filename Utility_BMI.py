class BMI_calculator:
    def __init__(self,weight,height): 
        self.weight = weight 
        self.height = height/100 

    def calculate_BMI(self):
        self.BMI = self.weight/self.height**2
        return self.BMI 

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
