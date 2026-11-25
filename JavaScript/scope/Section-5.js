// ## Section 5: Block Scope with Loops (5 Questions)

// ### Q21.
// Predict the complete output:

// ```js
// for (var number = 2; number <= 6; number += 2) {
//     console.log(number);
// }
// console.log("Final:", number);
// ```

// Explain why `"number"` can be accessed after the loop.

// ### Q22.
// What will be printed?

// ```js
// var count = 10;
// for (var count = 1; count <= 3; count++) {
//     console.log(count);
// }
// console.log("Count:", count);
// ```

// Explain what happens to the original value of `"count"`.

// ### Q23.
// Predict the output:

// ```js
// var i = 5;
// while (i > 2) {
//     console.log(i);
//     i--;
// }
// console.log("After loop:", i);
// ```

// Is `"i"` accessible after the loop? Why?

// ### Q24.
// Find the error, if any:

// ```js
// for (var item = 1; item <= 3; item++) {
//     console.log("Item:", item);
// }
// console.log("Last item:", item);
// ```

// Does the final statement cause an error? What value does `"item"` contain?

// ### Q25.
// Rewrite the following loop so that the loop variable is not accessible outside the loop. Use a declaration that provides block scope.

// ```js
// for (var step = 1; step <= 4; step++) {
//     console.log(step);
// }
// console.log(step);
// ```

// Explain the difference between your solution and the original code.

// ---

// ====================================================================================================================================
// Q21
// 2
// 4
// 6
// 8
// Final:8
// Because var does not have block scope. It has function scope or global scope.
//   Therefore, the variable declared inside the loop can also be accessed outside it.
// Q22
// 1
// 2
// 3
// Count: 4
// The original value 10 gets replaced by 1 when the loop starts because both declarations refer to the same variable.
// var does not create a separate variable inside the loop.
// Q23
//   5
// 4
// 3
// After loop: 2
// Yes, because i is declared using var, which does not have block scope.

// Variables declared using var inside loops can be accessed outside the loop.
// Q24
// Item: 1
// Item: 2
// Item: 3
// Last item: 4
// 1. var does not have block scope, we can access item outside the loop.
// The final statement does not cause an error because var allows access outside the loop.

// Q25
// for (let step = 1; step <= 4; step++) {
//     console.log(step);
// }

// console.log(step);
// var does not create a separate variable for each loop iteration. let creates a separate binding for each iteration, 
//   which is especially useful with callbacks.


