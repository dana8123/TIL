function isValidAge(person){
  if(person["age"] > 19){
    return true;
  } else{
    return false;
  }
}

const personArray = [
  {"name": "John Doe", "age": 20},
  {"name": "Jane Doe", "age": 19},
];

for(let i = 0; i < personArray.length; i++){
  if(isValidAge(personArray[i])){
    console.log("Here is your beer!",personArray[i]["name"]);
  } else{
    console.log("get OUT!", personArray[i]["name"]);
  }
}