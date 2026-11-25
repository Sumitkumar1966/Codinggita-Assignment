// ## Section 3: Function Scope (5 Questions)

// ### Q11.
// Predict the output:

// ```js
// function calculateTotal() {
//     var first = 100;
//     var second = 200;
//     console.log(first + second);
// }
// calculateTotal();
// console.log(first);
// ```

// Explain the behavior of the last statement.

// ### Q12.
// Find and explain the error:

// ```js
// function employee() {
//     var salary = 30000;
// }
// employee();
// console.log(salary);
// ```

// ### Q13.
// What will be the output?

// ```js
// var number = 15;
// function test() {
//     var number = 25;
//     console.log(number);
// }
// test();
// console.log(number);
// ```

// Why doesn't the value printed inside the function change the global variable?

// ### Q14.
// Consider this code:

// ```js
// function calculate() {
//     var result = 40;
//     result = result + 10;
//     console.log(result);
// }
// calculate();
// calculate();
// ```

// Answer the following:
// - What is the output?
// - Is a new local variable created each time the function is called?
// - Does the local variable remain accessible after the function finishes executing?

// ### Q15.
// Write a function named `"calculateArea()"` that:
// - Declares a local variable `"length"` with the value `8`.
// - Declares a local variable `"width"` with the value `4`.
// - Calculates and prints the area of a rectangle.
// - Does not make either variable accessible outside the function.

// ---
// ==================================================================================================================
// Answers:
11.
it shows ReferenceError: first is not defined
12.
ReferenceError: salary is not defined
becaure salary is written inside the employee() function.
13.
25
15
Because local number does not change the global number
14.
(i)50
50
(ii).Yes, a new local variable is created each time the function is called.
  (iii).No, the local variable cannot be accessed after the function finishes executing.
  15.
function calculateArea() {
    var length = 8;
    var width = 4;

    var area = length * width;

    console.log(area);
}

calculateArea();
  
