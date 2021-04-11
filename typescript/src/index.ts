interface Human {
  name: String,
  age: number,
  gender: String
}

const person = {
  name: "dana",
  age: 22,
  gender: "female"
}

const sayHi = (person: Human) => {
  return `Hello ${person.name}, you ar ${person.age}, and ${person.gender}`;
};

console.log(sayHi(person));

export {};