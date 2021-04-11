class Human {
  public name: string;
  public age: number;
  public gender: string;
  //method 클래스가 시작할 때 마다 호출됨, 클래스로부터 객체를 만들 때 마다.
  constructor(name: string, age: number, gender: string){
    this.name = name;
    this.age = age;
    this.gender = gender;
  }
}
//react, js등에서 클래스를 사용할 수 있음
//ts에서는 그냥 interface쓰는게 낫다?

const lynn = new Human("Lynn", 18, "female");
const sayHi = (person: Human) => {
  return `Hello ${person.name}, you ar ${person.age}, and ${person.gender}`;
};

console.log(sayHi(person));

export {};