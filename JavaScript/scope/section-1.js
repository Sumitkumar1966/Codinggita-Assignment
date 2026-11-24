// # JavaScript Assignment: Scope and Hoisting

// ---

// ## Section 1: What Is Scope? (5 Questions)

// ### Q1.
// Consider the following code:

// ```js
// var city = "Surat";
// function display() {
//     var country = "India";
//     console.log(city);
//     console.log(country);
// }
// display();
// ```

// Answer the following:
// - Which variable is declared in the global scope?
// - Which variable is declared inside the function?
// - Can both variables be accessed inside `"display()"`?

// ### Q2.
// Predict the output:

// ```js
// var price = 500;
// function calculate() {
//     var tax = 50;
//     console.log(price + tax);
// }
// calculate();
// console.log(price);
// ```

// ### Q3.
// Identify the scope of each variable:

// ```js
// var college = "ABC College";
// function student() {
//     var name = "Rahul";
//     var age = 20;
// }
// function teacher() {
//     var subject = "JavaScript";
// }
// ```

// Classify `"college"`, `"name"`, `"age"`, and `"subject"` as global or function-scoped variables.

// ### Q4.
// What will happen when you execute this code? Explain why.

// ```js
// function first() {
//     var number = 100;
// }
// function second() {
//     console.log(number);
// }
// first();
// second();
// ```

// ### Q5.
// Write a JavaScript program that:
// - Declares one variable in the global scope.
// - Declares another variable inside a function.
// - Prints both variables inside the function.
// - Prints the global variable outside the function.

// ---

// ==================================================================================================================
// Answers
// 1
// City
// Country
// Yes, both variables are accessible inside display()
// 2.
// 550
// 500
// 3.
// "college"==> Global,
// "name"==> function, 
// "age"==> function, and "subject"==> function
//   4.
// it will give reference error as
// One function cannot directly access another function's local variables
//   5.
var name="Sumit";
function display(){
  var marks=35;
  console.log(marks);
  console.log(name);
}
display();
console.log(name)

