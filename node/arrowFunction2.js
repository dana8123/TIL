function hello(message) {
	console.log(message);
}

// 첫번째 arrow function
const arrowFunction = (message) => {
	console.log(message);
}

// 두번째 arrow function
const arrowFunctionWithoutReturn = (message) => console.log(message);

hello("Hello function"); // Hello function
arrowFunction("Hello arrow function"); // Hello arrow function
arrowFunctionWithoutReturn("Hello arrow function without return"); // Hello arrow function without return