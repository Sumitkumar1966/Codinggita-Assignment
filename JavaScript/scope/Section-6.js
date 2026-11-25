// ## Section 6: Function Scope Inside Loops (5 Questions)

// ### Q26.
// Predict the output:

// ```js
// function calculate() {
//     for (var number = 1; number <= 3; number++) {
//         console.log(number * 10);
//     }
//     console.log("Final:", number);
// }
// calculate();
// ```

// Explain why `"number"` is accessible after the loop but not outside the function.

// ### Q27.
// Identify which statements cause errors:

// ```js
// function student() {
//     for (var marks = 60; marks <= 80; marks += 10) {
//         console.log(marks);
//     }
//     console.log(marks);
// }
// student();
// console.log(marks);
// ```

// Explain your answer for each occurrence of `"marks"`.

// ### Q28.
// Predict the output:

// ```js
// function test() {
//     var value = 5;
//     while (value < 8) {
//         console.log(value);
//         value++;
//     }
//     console.log("Final value:", value);
// }
// test();
// ```

// How many times does the loop execute?

// ### Q29.
// Find and explain the error:

// ```js
// function calculate() {
//     for (var i = 1; i <= 2; i++) {
//         console.log(i);
//     }
// }
// console.log(i);
// calculate();
// ```

// Why does the order of these statements matter?

// ### Q30.
// Write a function named `"printNumbers()"` that:
// - Uses a `"for"` loop to print numbers from 1 to 5.
// - Declares the loop variable using `"var"`.
// - Prints the loop variable again after the loop, inside the function.
// - Demonstrates that the loop variable cannot be accessed outside the function.

// Write the function call and the statement that attempts to access the variable outside the function. Explain the expected error.

// ---

// =============================================================================================
// Q26
10
20
30
Final: 4
var is accessible outside the loop but not outside its function.
  // Q27
  60
70
80
90
ReferenceError: marks is not defined
var allows access throughout the function, but not outside the function.
  // Q28
  5
6
7
Final value: 8
The loop executes 3 times because it prints 5, 6, and 7.
// Q29
