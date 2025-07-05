# Utilty_BMI
In this project, we have created two small utilities that calculate the BMI (Body Mass index) and assign a class based on the value of the index.

The two utilities have been developed using two of the most common programming languages, **Python** and **JavaScript** with the final aim to compare them.

**Python** is a programming language widely known and used for its easy syntax, as it use english language developing its code, and its versatility and readability. It can support different programming styles such as procedural, object oriented and functional and, thanks to its many different free libraries it is widely used for data analysis, data science and machine learning.

**JavaScript** is a programming language used to create dynamic interface on the website. It runs directly on the browser but it can be used into any IDE such as VsCode by using Node.js which is an open sourche cross-platform


We have executed the script by using an open-source application called Node.js that allow the execution of JavaScript code outside the web browser.

The aim is to compare the 2 utilities on the following points:

**-Development models.**

**-Syntax and readability.**

**-Performance efficiency.**

**-Scalability and maintainability.**

**-Security implications.**

------------------------------------------------------------------------------------------------------
**-Development models.**

**Python Utility**

The utility was designed and implemented using the Object-Oriented Programming (OOP) paradigm. By structuring the code around a class, it establishes a clear blueprint that encapsulates related data (such as BMI values and classification thresholds) and functionality (such as calculation methods) within a single reusable component. This encapsulation promotes modularity, making it easier to manage, extend, and debug the code. Creating objects from the class allows the utility to handle multiple, independent sets of data without interference, improving flexibility. Furthermore, this approach facilitates code reuse, enabling the utility to be imported and utilized in other projects simply by instantiating new objects with different input data. Overall, adopting OOP enhances maintainability, promotes clean code organization, and supports scalability as the project grows or requirements evolve.

**HOW DOES THE UTILITY WORKS USING PYTHON**

https://github.com/user-attachments/assets/6dc94ecb-4f52-4f14-8805-93033dcd8408

**HOW THE OOP CAN FACILITATE THE SCALABILITY OF THE SAME UTILITY**

https://github.com/user-attachments/assets/172a282e-930a-44fa-8958-edd3e59d6acd

**JS Utility**

The JavaScript utility has been developed following a procedural programming approach rather than an object-oriented one. The code is structured as a series of functions and sequential instructions that execute step-by-step, with the core logic encapsulated within a standalone function (BMI_calculator). This function takes inputs, performs calculations, and returns results without relying on the creation of objects or classes.

User interaction is managed using Node.js’s readline module, which handles input and output directly in the terminal environment. This procedural design keeps the utility straightforward and easy to follow for simple scripts like this. However, because it runs in a Node.js environment, the developer must be mindful of the current working directory and runtime context to ensure the utility executes properly, especially when integrating or deploying within larger projects.

While procedural programming offers simplicity and is often well-suited for small, focused tasks, it may limit extensibility and reusability compared to an object-oriented design. Nonetheless, this approach makes the utility quick to write, test, and run in the Node.js environment.

**HOW DOES THE UTILITY WORKS IN JAVASCRIPT USING NODE.js**

https://github.com/user-attachments/assets/cb4104a4-f86a-46ca-a2e6-919b67b9b34c

