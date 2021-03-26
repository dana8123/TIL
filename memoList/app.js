const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");

const app = express();
const router = express.Router();
const db = mongoose.connection;
const Todo = require("./models/todo");

db.on("error", console.error.bind(console, "connection error:"));

mongoose.connect("mongodb://localhost/todo-demo", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

router.get("/", (req, res) => {
  res.send("Hi!");
});

//할 일 작성하기
router.post("/todos",async (req,res) =>{
  const { value } = req.body;
  const maxOrderByUserId = await Todo.findOne().sort("-order").exec();
  let order = 1;

  if (maxOrderByUserId) {
    order = maxOrderByUserId.order + 1;
  }

  const todo = new Todo({ value, order });
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
  const { order, value, done } = req.body;

  const todo = await Todo.findOne(todoId).exec();
  if (order) {
    const targetTodo = await Todo.findOne({ order }).exec();
    if (targetTodo) {
      targetTodo.order = todo.order;
      await targetTodo.save();
    }
    todo.order = order;
  } else if (value){
    todo.value = value;
  } else if(done !== undefined){
    todo.doneAt = done ? new Date() : null;
  }

    await todo.save();      

  res.send({});
});


//할 일 삭제하기
router.delete("/todos/:todoId", async (req,res)=>{
  const { todoId } = req.params;
  await Todo.findOneAndDelete(todoId);
  res.send({});
})

app.use("/api", bodyParser.json(), router);
app.use(express.static("./assets"));


app.listen(8080, () => {
  console.log("서버가 켜졌어요!");
});