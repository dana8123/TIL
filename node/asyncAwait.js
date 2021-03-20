async function f() {

  let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve("완료!"), 1000)
  });

  let result = await promise; // 프라미스가 이행될 때까지 기다림 (*)

  console.log(result); // "완료!"
}

f();

//자바스크립트는 await 키워드를 만나면 
//프라미스가 처리(settled)될 때까지 기다립니다. 
//결과는 그 이후 반환됩니다. 