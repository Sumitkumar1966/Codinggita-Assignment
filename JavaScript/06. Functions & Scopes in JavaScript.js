# Assignment : Functions in JS
---
### Section 1: What Is a Function?
1. Why do we use functions instead of writing the same code again and again? Explain with one simple example.  
2. List any four advantages of functions and write one line for each advantage.  
3. Imagine you have to display a welcome message at 6 different places in your program. How will a function help you here?
4. Show the same code written twice without a function and once with a function.  
5. Give one real-life analogy that explains the idea of a function.  
6. Why do functions make debugging easier? Answer in 1–2 lines.
// ================================================================================================================================================
  // answeers:=
  1. We use functions to avoid writing the same code again and again, make code reusable, and keep it short and easy to manage.
example :
function sayhello {
  console.log("hello sumit")
}
sayhello()
sayhello()
sayhello()

2. Code Reusability: We can use the same code multiple times without rewriting it.
Less Repetition: Functions avoid writing the same code again and again.
Easy Debugging: Functions make it easier to find and fix errors.
Better Readability: Functions make code organized and easier to understand.

  3.
function welcome() {
    console.log("Welcome to CodingGita!");
}

welcome();
welcome();
welcome();
welcome();
welcome();
welcome();
4.
without a function
console.log("Hello Sumit");
console.log("Hello Sumit");
with a function
function greet() {
    console.log("Hello Sumit");
}

greet();
greet();

5.
A function is like a washing machine. We start it whenever we need to wash clothes, instead of washing everything manually from the beginning each time.

  6.
Functions keep code organized into smaller parts, making it easier to find and fix errors in a specific part of the program.
  // ================================================================================================================================================
  ### Section 2: Function Declaration
1. Create a function declaration named `displayCourse` that returns `"JavaScript Fundamentals"`. Call it and print the result.  
2. Write a function declaration getStudentStatus that returns the string "Active Learner". Store the returned value in a variable and print it.  
3. Write a function declaration and call it before its definition. What happens and why? Explain briefly.
// Answers==================================================================================================================================
  1.
function displayCourse{
  returns "javascript fundamental"
}
console.log(displayCourse())
2.
function getStudentStatus() {
    return "Active Learner";
}

let status = getStudentStatus();
console.log(status);
3.
displayMessage();

function displayMessage() {
    console.log("Hello World");
}
  // =================================================================================================================================
### Section 3: Function Expression
1. Create a function expression named `showMotto` that returns `"Code. Learn. Grow."`. Call it and print the output.  
2. Write a function expression `getSemester` that returns the number `3`. Print the value returned by the function.  
3. Create a function expression and try to call it before writing the expression. What error do you get and why?

  // Answers+=============================================================================================================
  1.
  const showMotto = function() {
    return "Code. Learn. Grow.";
};

console.log(showMotto());
2.
 const getSemester=function(){
   return 3
 };
console.log(getSemester())
3.
displayMessage();

function displayMessage() {
    console.log("Hello World");
}

it prints hello world as in javascript JavaScript supports hoisting for function declarations, which allows us to call a function before its definition.
### Section 4: Function Calling (Invocation)
1. Write a function declaration `greetStudent` that returns `"All the best for your coding journey!"`. Call this function four times.  
2. Create a function expression `todayFocus` that returns `"Focus on functions today"`. Store the result in a variable and print that variable.  
3. Write one function declaration and one function expression. Call each of them twice and print all four results

// ==========================================================================================================================

1.
function greetStudent(){
  returns "All the best for your coding journey!"
}
console.log(greetStudent()
console.log(greetStudent()
console.log(greetStudent()
console.log(greetStudent()
 2.
const todayFocus = function() {
    return "Focus on functions today";
};

let result = todayFocus();
console.log(result);

3.
function greet() {
    return "Hello Student";
}

const sayBye = function() {
    return "Goodbye Student";
};

console.log(greet());
console.log(greet());

console.log(sayBye());
console.log(sayBye());
// ========================================================================================================

### Section 5: Parameters vs Arguments

**Practical Questions**
1. Write a function declaration `subtract(a, b)` that returns the difference of two numbers. Call it with arguments `50` and `18` and print the result.  
2. Create a function expression `greetUser(name)` that returns `"Welcome, " + name + "!"`. Call it with the argument `"Aarav"`.  
3. Write a function `calculateArea(length, breadth)` that returns the area of a rectangle. Call it twice with different pairs of arguments: `(12, 5)` and `(8, 9)`.

**Theory Questions**

4. What is the difference between a parameter and an argument? Explain with a short example.  
5. Can a function have parameters but be called without arguments? What happens in that case? Explain briefly.

---
  // =================================================================================================================

  1.
  function subtract(a,b){
  returns a-b
}
console.log(subtract(50,18));
2.
const greetUser=function(name){
    return "Welcome, " + name+" !"
}
console.log(greetUser("Sumit"))
3.
function calculateArea(length,breadth){
    return length*breadth
}
console.log(calculateArea(12,5))
console.log(calculateArea(8,9))
4.
A parameter is a variable written in the function definition, whereas an argument is the actual value passed to the function when calling it.
  function greet(name) {  // name is a parameter
    console.log("Hello " + name);
}

greet("Sumit");  // "Sumit" is an argument
5.
Yes, but if no arguments are passed, the parameters get the value undefined in JavaScript (unless default values are provided).
  function greet(name) {
    console.log(name);
}

greet();
// =====================================================================================================================
### Section 6: Return Statement

**Practical Questions**
1. Write a function `squareOfNumber(n)` that returns the square of the given number. Call it with `9` and print the returned value.  
2. Create a function `isAdult(age)` that returns `true` if age is 18 or above, otherwise returns `false`. Test it with `17` and `20`.  
3. Write a function `getFullName(firstName, lastName)` that returns the full name. Call it with `"Rohit"` and `"Sharma"` and print the result.

**Theory Questions**

4. What does a function return if there is no `return` statement inside it?  
5. Why do we use the `return` statement in a function instead of just using `console.log()` inside the function? Explain in 2–3 lines.

---

  // ====================================================================================================================
  Answers:=
1.




