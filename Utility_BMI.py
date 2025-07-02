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


