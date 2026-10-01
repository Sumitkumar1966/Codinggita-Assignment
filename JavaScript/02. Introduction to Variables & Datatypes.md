# Assignment : Introduction to Variables and Datatypes
---
## Part I : Variables (let, var, const)

### Part a — 4 Questions

**1. Personal Information**<br>
Declare variables for `name`, `age`, and `city` using appropriate variable keywords. Assign values and print all three variables.
<br>
Ans==>>>
let name = Sumit;
let age = 18;
let city = "Ahmedabad";

console.log(name);
console.log(age);
console.log(city);
**2. Change the Score**
Create a variable `score` with the value `50`. Change its value to `80` and print the final value. Use the appropriate keyword for a value that can change.
<br> 
Ans==>>
let score = 50;

score = 80;

console.log(score);

**3. Constant Value**
Create a constant variable `PI` with the value `3.14`. Print its value. Do not try to change the value.<br>
Ans==>>
let PI=3.14;
console.log(PI);
**4. Uninitialized Variables**
Declare one variable having name `num1` using `var` and one having name `num2` using `let` without assigning values. Print both variables. Then assign values to them and print the values again.<br>
Ans===>>>
var num1;
let num2;

console.log(num1);
console.log(num2);

num1 = 10;
num2 = 20;

console.log(num1);
console.log(num2);

### Part b — 4 Questions

**5. Choose the Correct Keyword**
Create the following variables using the most appropriate keyword:

* `studentName` — the value will not change
* `marks` — the value may change
* `schoolName` — the value will not change

Assign values to all three variables. Change `marks` and print all variables.
<br>
Ans===>>>>
let studentName= "Sumit";
var marks= 40;
const schoolName="codinggita";
console.log(studentName);
console.log(marks);
console.log(schoolName);

**6. Understand Scope**
Write a program where `var`, `let`, and `const` variables are declared inside an `if` block. Try to access all three variables outside the block. Observe and identify which variables can be accessed.<br>
Ans==>>>
if (true) {
    var a = 10;
    let b = 20;
    const c = 30;
}

console.log(a); // 10
console.log(b); 
console.log(c); 

**7. Test Re-declaration**
Declare a variable named `user` using `var` and declare it again with a different value. Then perform the same experiment using `let`. Observe what happens and identify which declaration allows re-declaration.<br>
Ans==>>
var user="Sumit";
var user="Sanu";
console.log(user);
let user="Sumit";
let user="Sanu";
console.log(user);

**8. Test Re-assignment**
Create three variables using `var`, `let`, and `const`. Assign an initial value to each. Try to change the value of all three variables. Observe which variables allow re-assignment and which one produces an error.<br>
Ans==>>>
var a = 10;
let b = 20;
const c = 30;
console.log(a);
console.log(b);
console.log(c);
### Part c — 2 Questions

**9. Predict and Explain**
Without running the code, predict the output of each `console.log()` and identify which lines cause errors. Explain your answer using the rules of scope, re-assignment, and variable declaration.

```javascript
var x = 10;

if (true) {
    var x = 20;
    let y = 30;
    const z = 40;
}

console.log(x);
console.log(y);
console.log(z);
```
<br>
### Answer:=
The var is a functional scope but let and const are block scope thst's why only x will print and let and const will give error

**10. Fix the Program**
The following program contains multiple errors. Fix the code so that it runs correctly. Make sure your solution follows the rules for **initialization, re-declaration, re-assignment, and scope**.

```javascript
const name;

let age = 20;
let age = 25;

if (true) {
    var city = "Delhi";
    let country = "India";
}

console.log(country);

const score = 50;
score = 80;
```
<br>
Ans:-
const name = "Sumit";

let age = 20;
age = 25;

if (true) {
    var city = "Delhi";
    let country = "India";
    console.log(country);
}

console.log(city);

let score = 50;
score = 80;

console.log(name);
console.log(age);
console.log(city);
console.log(score);










// // Part e — Basic Identification (4 Questions)


// // 1. Classify the Types

// let wholeNumber = 25;
// let decimalNumber = 12.5;
// let text = "Hello World";
// let isStudent = true;

// console.log(wholeNumber, typeof wholeNumber);
// console.log(decimalNumber, typeof decimalNumber);
// console.log(text, typeof text);
// console.log(isStudent, typeof isStudent);

// // Output:
// // 25 number
// // 12.5 number
// // Hello World string
// // true boolean


// // 2. Undefined vs Null


// let a;
// let b = null;

// console.log(a, typeof a);
// console.log(b, typeof b);

// // Output:
// // undefined undefined
// // null object

// // Explanation:
// // undefined means a variable has been declared but has not been assigned a value.
// // null means an empty or intentionally missing value has been assigned.
// // typeof null returns "object" because of a historical JavaScript behavior.


// // 3. Number Special Values


// let positiveInfinity = Infinity;
// let negativeInfinity = -Infinity;
// let notANumber = NaN;
// let scientificNumber = 2.5e3;
// let largeNumber = 1_000_000;

// console.log(positiveInfinity, typeof positiveInfinity);
// console.log(negativeInfinity, typeof negativeInfinity);
// console.log(notANumber, typeof notANumber);
// console.log(scientificNumber, typeof scientificNumber);
// console.log(largeNumber, typeof largeNumber);

// // Output:
// // Infinity number
// // -Infinity number
// // NaN number
// // 2500 number
// // 1000000 number



// // 4. String Styles


// let name = "Ayush";

// let singleQuote = 'Hello World';
// let doubleQuote = "Hello JavaScript";
// let templateString = `Hello ${name}`;

// console.log(singleQuote);
// console.log(doubleQuote);
// console.log(templateString);

// // Output:
// // Hello World
// // Hello JavaScript
// // Hello Ayush





// // Part f — Advanced Primitive Types (3 Questions)

// // 5. Symbol Uniqueness


// let symbol1 = Symbol("id");
// let symbol2 = Symbol("id");

// console.log(symbol1 === symbol2);

// let user = {};

// user[symbol1] = "First Value";
// user[symbol2] = "Second Value";

// console.log(user[symbol1]);
// console.log(user[symbol2]);

// // Output:
// // false
// // First Value
// // Second Value

// // Explanation:
// // Every Symbol creates a unique value.
// // Even if two Symbols have the same description,
// // they are not equal to each other.


// // 6. BigInt Precision


// let normalNumber = 9007199254740991;

// console.log(normalNumber + 1);
// console.log(normalNumber + 2);
// console.log(normalNumber + 3);

// let bigNumber = 9007199254740991n;

// console.log(bigNumber + 1n);
// console.log(bigNumber + 2n);
// console.log(bigNumber + 3n);

// // Output:
// // 9007199254740992
// // 9007199254740992
// // 9007199254740994
// // 9007199254740992n
// // 9007199254740993n
// // 9007199254740994n

// // Explanation:
// // Number can safely represent integers only up to 9007199254740991.
// // Beyond this limit, Number may lose integer precision.
// // BigInt can represent very large integers with exact precision.



// // 7. Choose the Correct Type




// let uniqueId = Symbol("id");

// let largeInteger = 9007199254740991n;

// let uninitialized;

// let emptyValue = null;

// // Output:
// // uniqueId -> Symbol
// // largeInteger -> BigInt
// // uninitialized -> undefined
// // emptyValue -> null




// // Part g — Prediction & Fixing (3 Questions)

// // 8. Predict the Output


// let a;
// let b = null;
// let c = 42;
// let d = "Hello";
// let e = true;
// let f = Symbol("key");
// let g = 123n;

// console.log(typeof a, a);
// console.log(typeof b, b);
// console.log(typeof c, c);
// console.log(typeof d, d);
// console.log(typeof e, e);
// console.log(typeof f, f);
// console.log(typeof g, g);

// // Output:
// // undefined undefined
// // object null
// // number 42
// // string Hello
// // boolean true
// // symbol Symbol(key)
// // bigint 123n

// // Explanation:
// // a is undefined because it has no assigned value.
// // b is null, but typeof null returns "object".
// // c is a number.
// // d is a string.
// // e is a boolean.
// // f is a Symbol.
// // g is a BigInt.


// // 9. Fix the Code


// let num = 10;
// let text = "Hello";
// let flag = true;
// let empty;
// let nothing = null;
// let unique = Symbol("id");
// let big = 9007199254740991n;

// console.log(num);
// console.log(text);
// console.log(flag);
// console.log(empty);
// console.log(nothing);
// console.log(unique);
// console.log(big);

// // Output:
// // 10
// // Hello
// // true
// // undefined
// // null
// // Symbol(id)
// // 9007199254740991n


// // 10. Primitive vs Non-Primitive


// // a) 
// // Primitive data types store a single simple value.
// // Non-Primitive data types can store collections of values
// // or more complex structures.

// // Example of Primitive:
// let age = 18;

// // Example of Non-Primitive:
// let student = {
//     name: "Ayush",
//     age: 18
// };


// // b)
// // They are called primitive because they represent basic,
// // single values and are not objects themselves.

// // Examples:
// let number = 10;
// let word = "Hello";
// let status = true;
// let value;
// let nothingValue = null;
// let id = Symbol("id");
// let bigValue = 100n;


// // c)
// // An Object is a non-primitive data type.
// // It can contain multiple values as properties.

// // Example:
// let person = {
//     name: "Ayush",
//     age: 18,
//     city: "Ranchi"
// };

// // Output:
// // person is an Object.
// // It can store multiple related values together.
