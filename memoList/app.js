const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");

const app = express();
const router = express.Router();
const db = mongoose.connection;
const Todo = require("./models/todo");

db.on("error", console.error.bind(console, "connection error:"));

router.get("/", (req, res) => {
  res.send("Hi!");
});

//할 일 작성하기
router.post("/todos",async (req,res) =>{
  const { value } = req.body;
  const maxOrderByUserId = await Todo.findOne().sort("-order").exec();
  const order = maxOrderByUserId ? maxOrderByUserId.order + 1 : 1;
  await todo.save();
  res.send({ todo });
})

//할 일 가져오기
router.get("/todos", async(req,res)=>{
  const todos = await Todo.find().sort("-order").exec();

  res.send({ todos });
})

//할 일 순서 바꿔주기
router.patch("/todos/:todosId", async (req,res) =>{
  const { todoId } = req.params;
  const { order } = req.body;

  const currentTodo = await Todo.findById(todoId);
  if (!currentTod) {
    throw new Error("존재하지 않는 todo데이터입니다.");
  }
  if (order) {
    const targetTodo = await Todo.findOne({ order }).exec();
    if (targetTodo){
      targetTodo.order = todo.order;
      await targetTodo.save();
    }
    currentTodo.order = order;
  }

  await currentTodo.save();

  res.send({});
});

app.use("/api", bodyParser.json(), router);
app.use(express.static("./assets"));

mongoose.connect("mongodb://localhost/todo-demo", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

app.listen(8080, () => {
  console.log("서버가 켜졌어요!");
});