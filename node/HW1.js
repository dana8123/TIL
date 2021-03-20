const personArray = [
  {"name": "John Doe", "age": 20},
  {"name": "Jane Doe", "age": 19},
];
// for문


//for in 문
for (const index in personArray){
  console.log("His/Her name is", personArray[index]["name"],". He/She is" ,personArray[index]["age"],"old."
  )
}
//for each문

personArray.forEach(v =>{
  console.log("His/Her name is",v["name"],". He/She is",v["age"],"old.")
})

//for of 문
for(const person of personArray){
  console.log("His/Her name is",person["name"],"He/She is",person["age"],"old.")
}
// 위에서 배운 4가지 for문을 이용해서 아래 문장을 출력해봅시다 (console.log)

// His/her name is John Doe. He/She is 20 years old.
// His/her name is Jane Doe. He/She is 19 years old.