// ## Section 2: Global Scope (5 Questions)

// ### Q6.
// Predict the output:

// ```js
// var game = "Cricket";
// function play() {
//     console.log("I like " + game);
// }
// play();
// console.log(game);
// ```

// ### Q7.
// What will be the output?

// ```js
// var language = "English";
// function showLanguage() {
//     console.log(language);
// }
// function changeLanguage() {
//     language = "Gujarati";
// }
// showLanguage();
// changeLanguage();
// showLanguage();
// console.log(language);
// ```

// Explain why the output changes.

// ### Q8.
// Find the error, if any:

// ```js
// function displayMarks() {
//     console.log(marks);
// }
// var marks = 75;
// displayMarks();
// ```

// Will this code produce an error? Explain your answer.

// ### Q9.
// Predict the output:

// ```js
// var color = "Red";
// function showColor() {
//     var message = "Favorite color: ";
//     console.log(message + color);
// }
// showColor();
// console.log(color);
// console.log(message);
// ```

// Which statement causes an error, and why?

// ================================================================================================================
// Answrs:
// 6.
// I like Cricket
// Cricket
// 7.\
// English
// gujarati
// gujarati
// 8.
// no noerrror will produce as var marks is a global function and can be accessed everywhere
// 9
// Favorite color: Red
// Red
// ReferenceError: message is not defined
// it causes error as message is not a global scope but a functional scope
// 10
var school="Sunrise School";
function showschool(){
    console.log(school);
}
function updateSchool(){
    school="Green valley school"
}
showschool();
updateSchool();
console.log(school)



