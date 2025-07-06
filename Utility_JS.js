
function BMI_calculator(weight, height) {
  height = height / 100;
  const BMI = weight / (height ** 2);
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

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin, 
  output: process.stdout
});

rl.question('What is your weight in Kg? ', (weight) => { 
  console.log('Your weight is', weight); 

  rl.question('What is your height in cm? ', (height) => { 
    console.log('Your height is', height);  
    const result = BMI_calculator(Number(weight), Number(height));
    console.log(result);

    rl.close();
  });
});
