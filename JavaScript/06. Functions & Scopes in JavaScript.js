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
function squareOfNumber(n) {
    return n * n;
}

console.log(squareOfNumber(9));
2.
function isAdult(age){
    if (age>=18){
        return true
    }else{
        return false
    }
}
console.log(isAdult(17));
3.
function getFullName(firstName, lastName) {
    return firstName + " " + lastName;
}

console.log(getFullName("Rohit", "Sharma"));
4.
If there is no return statement inside a function, it returns undefined by default.
  5.
return sends the result back from the function so we can store it in a variable or use it in calculations.



console.log() only displays the result on the screen; it does not return the value

### Section 7: Why Use Functions? (Real-world Example)

**Practical Questions**
1. You need to calculate the total marks of three subjects for 4 different students. Write a function `getTotal(m1, m2, m3)` and call it four times with different marks instead of repeating the addition code.  
2. Create a function `calculateSimpleInterest(principal, rate, time)` that returns the simple interest. Use the function to find interest for two different sets of values.  
3. Without using a function, write code to find the average of three numbers twice (for two students). Then rewrite the same logic using a single function `findAverage(a, b, c)` and call it twice.

**Theory Questions**

4. How do functions help in reducing code repetition? Explain with one real-world example.  
5. Mention any three advantages of using functions in a program.


---
  // ==================================================================================================================================================================================================================
  // ANSWERS:
  1.
function getTotal(m1, m2, m3) {
    return m1 + m2 + m3;
}

console.log(getTotal(80, 75, 90));
console.log(getTotal(70, 85, 80));
console.log(getTotal(60, 65, 70));
console.log(getTotal(90, 95, 85));
2.
function calculateSimpleInterest(principal, rate, time){
    return (principal*rate*time)/100
}
console.log(calculateSimpleInterest(200,5,1))
3.
// Student 1
let a = 10;
let b = 20;
let c = 30;

let avg1 = (a + b + c) / 3;
console.log(avg1);

// Student 2
let x = 40;
let y = 50;
let z = 60;

let avg2 = (x + y + z) / 3;
console.log(avg2);
4.
Functions help us avoid writing the same code again and again.

We write the code once inside a function and call that function whenever we need it.
  Suppose a teacher wants to calculate the total marks of 50 students.

Without a function, the teacher has to write the addition code 50 times.

With a function, the teacher writes the addition logic only once and calls it for all 50 students.

This saves time and makes the code shorter.
  5.
1. Code Reusability: We can use the same function multiple times without writing the same code again.

2. Code Readability: Functions make code easier to read and understand.

3. Easy Maintenance: If we want to change something, we only need to update the function instead of changing the same code at multiple places.

### Section 8: Function Scope

**Practical Questions**
1. Create a function `showCity` that declares a local variable `city = "Ahmedabad"` and prints it. After calling the function, try to print `city` outside and note what happens.  
2. Declare a global variable `trainer = "CodingGita Mentor"`. Write a function `displayTrainer` that prints this global variable. Call the function and also print the variable outside the function.  
3. Write a function `demoScope` that contains a local variable `value = 50`. Print the variable inside the function. Then try accessing the same variable outside and explain the output/error.

**Theory Questions**
4. A variable declared inside a function cannot be used outside. Why does JavaScript follow this rule? How does it help in writing better programs?  
5. What will happen if a global variable and a local variable have the same name? Which one will the function use? Explain briefly.

---
  // ======================================================================================================
  Answers:
1.
function showCity() {
    let city = "Ahmedabad";
    console.log(city);
}

showCity();

console.log(city);
2.
let trainer = "CodingGita Mentor";

function displayTrainer() {
    console.log(trainer);
}

displayTrainer();

console.log(trainer);
3.
function demoScope() {
    let value = 50;
    console.log(value);
}

demoScope();

console.log(value);

4.
JavaScript follows this rule because of local scope. It protects variables from being accessed or changed outside the function.

It helps in:
(i) Avoiding unwanted changes to variables.
(ii) Preventing naming conflicts.
(iii)Keeping code clean and organized.
  5
If a global variable and a local variable have the same name, the function will use the local variable because it gets priority inside the function.

### Section 9: Combining Function Concepts

**Practical Questions**
1. Write a function `generateMessage(name, score)` that calculates whether the student has passed (score ≥ 40) and returns a complete sentence like: `"Aarav has scored 65 and the result is Pass"`.  
2. Create a function `billCalculator(item1, item2, item3)` that returns the total amount and also mentions if the customer gets a discount (total ≥ 1000 → "Discount Applied", otherwise "No Discount").  
3. Write a function `performanceReport(student, m1, m2, m3)` that calculates total and average, then returns a formatted string containing name, total, average and a remark ("Excellent" if average ≥ 80, otherwise "Keep Improving").

**Theory Questions**

4. Why is it better to perform multiple related tasks (calculation + decision + message) inside one function instead of writing separate pieces of code?  
5. How does combining concepts like parameters, return and conditions inside a single function improve code quality?

---
  1.
  function generateMessage(name, score) {
    if (score >= 40) {
        return name + " has scored " + score + " and the result is Pass";
    } else {
        return name + " has scored " + score + " and the result is Fail";
    }
}

console.log(generateMessage("Aarav", 65));
console.log(generateMessage("Rohan", 30));
2.
function billCalculator(item1, item2, item3) {
    let total = item1 + item2 + item3;

    if (total >= 1000) {
        return "Total: " + total + " - Discount Applied";
    } else {
        return "Total: " + total + " - No Discount";
    }
}

console.log(billCalculator(400, 300, 500));
console.log(billCalculator(200, 300, 100));
3.
function performanceReport(student, m1, m2, m3) {
    let total = m1 + m2 + m3;
    let average = total / 3;

    if (average >= 80) {
        return "Name: " + student + ", Total: " + total + ", Average: " + average + ", Remark: Excellent";
    } else {
        return "Name: " + student + ", Total: " + total + ", Average: " + average + ", Remark: Keep Improving";
    }
}

console.log(performanceReport("Aarav", 90, 85, 95));
console.log(performanceReport("Rohan", 50, 60, 70));
4.
It is better because one function can perform all related tasks together.
==> It avoids repeating code.
==> It makes the program easier to understand.
==> It makes code reusable and organized.
5.
Parameters: Allow us to give different inputs to the same function.
 Conditions: Help the function make decisions.
 Return: Sends the final result back.
Combining these concepts makes code reusable, simple, organized and easy to maintain.
### Section 10: Nested Functions

**Practical Questions**
1. Write a function `mainTask` that contains an inner function `helperTask`. The inner function should return `"Task completed successfully"`. Call the inner function from `mainTask` and return its result.  
2. Create a function `calculateFinal(m1, m2)` that has an inner function `getTotal` to add the marks. Use the inner function and return a message: `"Final marks = "` followed by the total.  
3. Write a function `studentStatus(name, marks)` containing an inner function `getGrade`. The inner function returns `"A"` if marks ≥ 80, `"B"` if marks ≥ 60, otherwise `"C"`. Return a final sentence using the name and grade.

**Theory Questions**

4. What is the main advantage of writing a function inside another function? When should we use nested functions?  
5. Can an inner function access variables of the outer function? What about the reverse (outer accessing inner variables)? Explain.

  // ==================================================================================================================================================
  1.
function mainTask() {
    function helperTask() {
        return "Task completed successfully";
    }

    return helperTask();
}

console.log(mainTask());\

2.
function calculateFinal(m1, m2) {
    function getTotal() {
        return m1 + m2;
    }

    return "Final marks = " + getTotal();
}

console.log(calculateFinal(40, 50));
console.log(calculateFinal(30, 60));
3.
function studentStatus(name, marks) {
    function getGrade() {
        if (marks >= 80) {
            return "A";
        } else if (marks >= 60) {
            return "B";
        } else {
            return "C";
        }
    }

    return name + " has grade " + getGrade();
}

console.log(studentStatus("Aarav", 90));
console.log(studentStatus("Rohan", 65));
console.log(studentStatus("Rahul", 40));
4.
The main advantage of nested functions is that they help organize code and keep helper functions private inside the outer function.

We should use nested functions when a small function is needed only inside another function.

Example: getGrade() is needed only inside studentStatus().
  5.
Inner function accessing outer variables: Yes, an inner function can access variables of its outer function.



Outer function accessing inner variables: No, the outer function cannot directly access variables declared inside the inner function.



  


  










