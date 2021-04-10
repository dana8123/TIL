const name = "dana",
  age = 24,
  gender = "female";

const sayHi = (name, age, gender?) => {
  console.log(`Hello ${name}, you ar ${age}, and ${gender}`);
};

sayHi(name, age);

export {};