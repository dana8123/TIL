function hello() {
	console.log("Hello function");
}

// 첫번째 arrow function
const arrowFunction = () => {
	console.log("Hello arrow function");
}

// 두번째 arrow function
const arrowFunctionWithoutReturn = () => console.log("Hello arrow function without return");

hello(); // Hello function
arrowFunction(); // Hello arrow function
arrowFunctionWithoutReturn(); // Hello arrow function without return