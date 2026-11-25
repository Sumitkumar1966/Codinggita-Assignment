// ## Section 4: No Block Scope with `"var"` (5 Questions)

// ### Q16.
// Predict the output:

// ```js
// if (10 > 5) {
//     var result = "Success";
// }
// console.log(result);
// ```

// Explain why `"result"` is accessible outside the `"if"` block.

// ### Q17.
// What will be printed?

// ```js
// var number = 1;
// if (true) {
//     var number = 2;
// }
// console.log(number);
// ```

// Why does the output differ from what you might expect if the block had its own scope?

// ### Q18.
// Predict the output:

// ```js
// var message = "Start";
// {
//     var message = "End";
// }
// console.log(message);
// ```

// Does the standalone block create a separate scope for `"var"`?

// ### Q19.
// Find the output and explain the variable's scope:

// ```js
// if (false) {
//     var result = 100;
// }
// console.log(result);
// ```

// Does the condition being `"false"` prevent the `"var"` declaration from being hoisted?

// ### Q20.
// Rewrite the following code so that the variable `"secret"` cannot be accessed outside the `"if"` block. Use a variable declaration that supports block scope.

// ```js
// if (true) {
//     var secret = "Hidden";
// }
// console.log(secret);
// ```

// Explain why your solution works.

// ---
// ======================================================================================================================
// Answers
// 16.
// Success
// Variables declared using var inside an if block can be accessed outside that block.
// 17
// 2
// The output is 2 because var does not create a separate variable inside the if block.
// 18)
// End
// No, a standalone block does not create block scope for var.
// 19)
// Undefined
// Yes, the var declaration is hoisted even when the condition is false. But the assignment does not happen.
// 20)
// if (true) {
//     let secret = "Hidden";
// }

// console.log(secret);







