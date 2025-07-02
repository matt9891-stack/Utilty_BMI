
// to start we will create a function that takes some inputs like weight and hight and provide some output

// we create a function to convert height from centimeters to meters because BMI formula needs meters
// const creates a variable called BMI which is calculated by dividing th weight by the power of the height in meters
function BMI_calculator(weight, height) {
  height = height / 100;
  const BMI = weight / (height ** 2);
//we have used the if statement to check whether the BMI lies in certain ranges 
//the function will return a different statement based on the BMI value
  if (BMI >= 40) {
    return 'Based on your weight and height your BMI suggests an Obesity Class 3';
  } else if (BMI >= 35) {
    return 'Based on your weight and height your BMI suggests an Obesity Class 2';
  } else if (BMI >= 30) {
    return 'Based on your weight and height your BMI suggests an Obesity Class 1';
  } else if (BMI >= 25) {
    return 'Based on your weight and height your BMI suggests an Overweight status';
  } else if (BMI >= 18.5) {
    return 'Based on your weight and height your BMI suggests a Healthy weight status';
  } else {
    return 'Based on your weight and height your BMI suggests an Underweight status';
  }
}
//readline will work as input in Node.js reading the input given by the user
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin, //these 2 lines allow the the code to take the input from the user and show it in the terminal
  output: process.stdout
});

rl.question('What is your weight in Kg? ', (weight) => { //The code allow input to input it's weight
  console.log('Your weight is', weight); //The weight given will be diplayed in the console

  rl.question('What is your height in cm? ', (height) => { //The code allow input to input it's height
    console.log('Your height is', height); //The height given will be diplayed in the console
//The code below will perform the BMI calculation using the function and display the result in the terminal 
    const result = BMI_calculator(Number(weight), Number(height));
    console.log(result);

    rl.close();
  });
});
