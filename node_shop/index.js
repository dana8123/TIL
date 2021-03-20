const express = require('express')
const app = express()
const connect = require('./schemas');
const port = 3000
const goodsRouter = require('./routes/goods');
const userRouter = require('./routes/user');

connect();

app.use(express.json())


app.use(express.static('public'));


app.get('/', (req, res) => {
  res.send('hello')
})

app.get('/home', (req, res) => {
  res.render('index');
})

app.get('/detail',(req,res)=>{
  res.render('detail')
})
app.use('/user',userRouter);
app.use('/goods',goodsRouter); //이건 지워야하는건가?
app.use("/api", [goodsRouter]);


app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');


app.listen(port, () => {
  console.log(`listening at http://localhost:${port}`)
})