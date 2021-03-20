const isReady = true;
// 1. Producer
const promise = new Promise((resolve, reject) => {
  console.log("Promise is created!");
  if (isReady) {
    resolve("It's ready");
  } else {
    reject("Not ready");
  }
});
// promist에서 resolve되거나 reject된 이후의 후처리를 담당하는 부분
// 2. Consumer
promise
// resolve 될 경우
  .then(messsage => {
    console.log(messsage);
  })
  // reject될 경우
  .catch(error => {
    console.error(error);
  })
  .finally(() => {
    console.log("Done");
  });