const express = require("express");
const { Op } = require("sequelize");
const { User, Goods } = require('./models');
const jwt = require("jsonwebtoken");
const authMiddleware = require('./middlewares/auth-middleware');
const app = express();
const router = express.Router();

router.post("/users", async(req,res)=>{
  try{
    const{
      nickname,
      email,
      password,
      confirmPassword
    } = req.body;

  if(password != confirmPassword){
    res.stastus(400).send({
      errorMessage: '패스워드가 동일하지않습니다.'
    });
    return; //아래의 코드를 실행할 필요가 없다
  }


  const existUser = await User.findAll({
    where: {
      [Op.or]: [{ nickname }, { email }]
    },
  });

  if (existUser.length){
    res.status(400).send({
      errorMessage: '이미 가입된 이메일 또는 닉네임이 있습니다.'
    });
    return;
  }

  const user = await User.create({ email, nickname, password});

  res.status(201).send({});
} catch(err) {
  console.log(err);
  res.status(400).send({
    errorMessage :'데이터 형식이 올바르지않습니다.'
  });
};
});

//로그인
router.post("/auth", async(req,res)=>{
  try{
    const { email, password  } = req.body;
  
  const user = await User.findOne({ where: {email, password} });
  
  if( !user ){
    res.status(400).send({
      errorMessage: '이메일 또는 패스워드가 잘못됐습니다.',
  });
  return;
}
  const token = jwt.sign({ userId : user.userId}, "yj-secret-key");
  res.send({
    token,
  });
} catch(err){
  res.status(400).send({
    errorMessage: '데이터형식이 올바르지 않습니다.'
  });
};
});


//내 정보 확인 
router.get("/users/me", authMiddleware, async(req,res)=>{
  const { user } = res.locals;
  res.send({
    user: {
      email: user.email,
      nickname: user.nickname
    }
  });
});

app.use("/api", express.urlencoded({ extended: false }), router);
app.use(express.static("assets"));
/////////////////////////////
//상품페이지 시작(하..라우터를..분리하자..분리하는게 좋을것같다...)
////////////////////////////
//상품 다 불러오기
router.get("/goods", authMiddleware, async(req,res)=>{
  try{
    const { category } = req.query;
    const goods = await Goods.findAll({
      order : [["goodsId", "DESC"]],
      where: category ? { category } : undefined,
    });
    res.send({ goods });
  }catch(err){
    console.log(err);
  }
});

//상세페이지 가져오기
router.get("/goods/:goodsId", authMiddleware, async(req,res)=>{
  const { goodsId } = req.params;
  goods = await Goods.findByPk({ goodsId });

  if(!goods){
    res.status(404).send({});
  } else{
    res.send({goods});
  }
});

//상품 생성하기
router.post("/goods", async(req,res)=>{
  const {goodsId, name, thumbnailUrl, category, price} = req.body;
  isExist = await Goods.findAll({ goodsId });
  if( isExist.length === 0 ){
    await Goods.create({ name, thumbnailUrl, category, price});
  }
  res.send({ result: "success"})
});

//상품 카트에 넣기
router.post("/goods/:goodsId/cart", authMiddleware, async(req,res) => {
  const { goodsId } = req.params;
  const { quantity } = req.body;
  isCart = await Cart.findAll({ goodsId });
  console.log(isCart, quantity);
  if (isCart.length) {
    await Cart.updateOne({ goodsId }, { $set: { quantity } });
  } else {
    await Cart.create({ goodsId: goodsId, quantity: quantity });
  }
  res.send({ result: "success" });
});

router.get("/cart", authMiddleware, async(req,res)=>{
  const cart = await Cart.find({});
  const goodsId = cart.map(cart => cart.goodsId);

  goodsInCart = await Goods.find()
    .where("goodsId")
    .in(goodsId);

  concatCart = cart.map(c => {
    for (let i = 0; i < goodsInCart.length; i++) {
      if (goodsInCart[i].goodsId == c.goodsId) {
        return { quantity: c.quantity, goods: goodsInCart[i] };
      }
    }
  });

  res.json({
    cart: concatCart
  });
});

//cart에서 삭제하기
router.delete("/goods/:goodsId/cart", authMiddleware, async(req,res)=>{
  const { goodsId } = req.params;
  
  const isGoodsInCart = await Cart.find({ goodsId});
  if  (isGoodsInCart.length > 0) {
    await Cart.deleteOne({ goodsId });
  }

  res.send({ result: "success" })
});

//cart update하기
router.patch("/goods/:goodsId/cart", authMiddleware, async(req,res) => {
  const { goodsId } = req.params;
  const { quantity } = req.body;

  isCart = await Cart.find({ goodsId });
  console.log(isCart, quantity);
  if (isCart.length) {
    await Cart.updateOne({ goodsId }, { $set: { quantity }});
  }

  res.send({ result: "success"})
});


app.listen(8080, () => {
  console.log("서버가 요청을 받을 준비가 됐어요");
});

