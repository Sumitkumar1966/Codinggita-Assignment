// # 1. What Is an Array?
// Question:1 What is the definition of an array in JavaScript?
Answer:1 
// An array is an ordered collection of values.
// Each value has a unique index (position).
// Index always starts at 0.


// Question:2 What is the technical term for the position of a value inside an array?
Answer:2
// index

Question:3 
// At which number does the index of an array always start?
Answer:3 
// 0 

Question:4 
// Given the array var numbers = [10, 20, 30, 40];, what value is stored at index 2?
ANswer:4 
// 30

Question:5 
// For the same array var numbers = [10, 20, 30, 40];, what is the index of the number 40?
Answer:5
// 30
// =======================================================================================================
// #2 Creating Arrays
// 1.
ANswer:1 
// first method==>
    // var arr = [1,2,3,4,5]
// second method==>
// var arr = new Array(1,2,3,4,5)
2.
Answer:2 
// var arr = [1,2,3,4,5]
3.
Answer:3 
// var students= ["Jenil","Mahir","Priyesha","Yashvi"]
4.
var marks=new Array(85,90,78);
5.
New
// =============================================================================================================
## # 3. Accessing Values in an Array
1. What do you use to access a specific value stored in an array?
2. Given `var students = ["Jenil", "Mahir", "Priyesha"];`, what does `console.log(students[0]);` output?
3. For the same array, what does `console.log(students[2]);` output?
4. What value does JavaScript return if you attempt to access an index that does not exist (such as `students[10]`)?
5. Write a line of code to log the first element of an array named `colors`.

---
// ==========================================================================================================
// 1.
// // indexing
// 2.
// Jenil
// 3.
// priyesha
// 4.
// undefined
// 5.
// var color=["red","white","green","orange"]

// ==================================================================================================================

## # 4. Updating Values
1. How do you update a specific value inside an existing JavaScript array?
2. Given `var marks = [80, 75, 90];`, what code would you write to change the second element (`75`) to `95`?
3. After executing the update from the previous question, what will `console.log(marks);` output?
4. True or False: You need to use a special built-in method like `update()` to change an array element's value.
5. Can you update a value at an index that is currently outside the bounds of the array? What happens if you assign a value to a much higher index?

---
// ==================================================================================================
  1.
  // var arr = [12,25,36,98]
// arr[2] = 55
// console.log(arr)
  2.
  // var marks = [80, 75, 90];
// marks[1]= 95;
// console.log(marks)
  3.
// [80,95,90]
4.
// false
5.
Yes, in JavaScript, you can assign a value to an index that is outside the current array bounds.
  but the length of array increses and added an empty element at the emoty palces.
  // =============================================================================================
  
// ## # 5. Array Length
// 1. What is the name of the built-in property available on every JavaScript array that tells you how many items it contains?
// 2. Given `var arr = [1, 2, 3, 4];`, what does `console.log(arr.length);` output?
// 3. If an array is empty (contains no elements), what is its `length` property equal to?
// 4. Why is the `length` property particularly useful when working with arrays?
// 5. Is `length` a function call (requiring parentheses `()`) or a property?

// ---
// 1.
//   length
// 2.
// ===>>4
// 3.
// ====>0
// 4.
// The length property is useful because it tells us the total number of elements in an array.
//   5.
// length is a property, not a function.

  // ================================================================================================
//   ## # 6. Looping Through Arrays
// 1. What are the two types of loops demonstrated in the notes for iterating through an array?
// 2. In a standard `for` loop, what condition is typically used to ensure the loop stops before going out of bounds? (`i < ...`)
// 3. In the `while` loop example, where is the increment step (`i++`) placed relative to the array access statement?
// 4. Write a `for` loop structure that prints every element of an array named `students`.
// 5. What happens if your loop condition incorrectly uses `<=` instead of `<` alongside `students.length` when accessing elements?
// 6. Write a `for...of` loop that prints every element of an array named `subject`.
// 7. What is the main advantage of using a `for...of` loop over a traditional `for` loop when you only need the values (and not the indices)?
// 8. Given `const colors = ["Red", "Blue", "Green"];`, what will the following code output?
//    ```javascript
//    for (const color of colors) {
//        console.log(color, indexOf(color);
//    }

---
// =========================================================================================================
1.
 // for loop , while loop, for...of loop
 2.
 // arr.length
 3.
 at the end after the console part
 4.
 const students = ["Jenil", "Mahir", "Krishna", "Yashvi"];
for (let i = 0; i < students.length; i++) {
    console.log(students[i]);
}
5.
it will give an error as the index of element is more than the arr element
6.
let subject = ["Maths", "Science", "English", "Computer"];

for (let sub of subject) {
    console.log(sub);
}
7.
A traditional for loop requires an index variable i.
We need to use arr[i] to access each element.
A for...of loop directly gives us the values.
8.
gives an error because indexOf() is not written correctly. It should be called using the array name, like colors.indexOf(color).
const colors = ["Red", "Blue", "Green"];

for (const color of colors) {
    console.log(color, colors.indexOf(color));
}
// =============================================================================================
## # 7. Adding Elements to Arrays
1. Which method is used to add an element at the **end** of an array?
2. Which method is used to add an element at the **beginning** of an array?
3. Given `let nums = [1, 2, 3];`, write the code to add `4` at the end using the appropriate method. What will `console.log(nums);` show after that?
4. Continuing from the previous question, write the code to add `0` at the beginning. What will the final array look like?
5. True or False: `push()` and `unshift()` both modify the original array (they are mutating methods).
---
// ===================================================================================
1.

 











