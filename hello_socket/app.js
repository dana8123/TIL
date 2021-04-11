const express = require("express");
const Http = require("http");
const socketIo = require("socket.io");

const app = express();
const http = Http.createServer(app);
const io = socketIo(http, {
  cors: {
    origin: "*",
    methods: ["GET", "POST"]
  }
});

app.get("/test", (req,res)=>{
  res.send("익스프레스 잘 켜져있습니다.");
})

http.listen(3000, () =>{
  console.log("서버가 켜졌습니다.");
});

io.on("connection", (socket) => {
  console.log("connecting!");


  socket.send("oh!")

  socket.emit("customEventName", "새로운 이벤트인가?");
})