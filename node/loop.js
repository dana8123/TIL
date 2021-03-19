const personArray = [
  {
  "name" : "john_doe",
  "age" : 17
},
{
  "name" : "jane_doe",
  "age" : 25
}
]

for(let i = 0; i < personArray.length; i++){
  if (personArray[i]["age"] > 19){
      console.log("Here is your beer!", personArray[i]["name"]);
  } else{
    console.log("get OUT!", personArray[i]["name"]);
  }
}
