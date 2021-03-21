const express = require('express')
const app = express()
const connect = require('./schemas');
const port = 3000
const goodsRouter = require('./routes/goods');
const userRouter = require('./routes/user');
app.use(express.urlencoded({ extended: false }))

connect();

app.use(express.json())


app.use(express.static('public'));

app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');



app.get('/home',(req,res)=>{
  res.render('index');
})

app.get('/detail',(req,res)=>{
  res.render('detail')
})

app.get('/cart', (req, res) => {
  res.render('cart');
})

app.get('/order', (req,res) => {
  res.render('order')
})


app.use('/user',userRouter);
app.use('/goods',goodsRouter); //이건 지워야하는건가?
app.use("/api", [goodsRouter]);




app.listen(port, () => {
  console.log(`listening at http://localhost:${port}`)
})