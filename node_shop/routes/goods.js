const express = require('express');
const Goods = require('../schemas/goods');
const Cart = require('../schemas/cart')

const router = express.Router();

//body 넘겨주기
router.post('/goods',async(req,res)=>{
  const{ goodsId, name, thumbnailUrl, category, price } = req.body;

  isExist = await Goods.find({ goodsId });
  if ( isExist == 0 ){
    await Goods.create({ goodsId, name, thumbnailUrl, category, price });
  }
  res.send({ result: "success" });
});


//익명 쇼핑몰 - RESTful(REST하게) API 만들기(2)
router.get('/goods',async(req,res,next)=>{
  try{
    const {category} = req.query;
    const goods = await Goods.find({category}).sort("-goodsId");
    res.json({goods : goods})  //goods라는 컬럼?에서 내용물을 전부 가져와라 이런뜻인가
  } catch(err){
    console.error(err);
    next(err);
  }
  //TODO: req,res,next와 req,res 의 차이점. 몽고디비 표기법 
})

//상세페이지 
router.get('/goods/:goodsId',async (req,res)=>{
  const { goodsId } = req.params;
  goods = await Goods.findOne({goodsId : goodsId});
  res.json({detail : goods}); 
  //TODO: 몽고디비 부분은 따로 알아보자.
})

//cart schema 추가하였으니 api 추가하기

router.post("/goods/:goodsId/cart", async (req, res) => {
  const { goodsId } = req.params;
  const { quantity } = req.body;

  isCart = await Cart.find({ goodsId });
  console.log(isCart, quantity);
  if (isCart.length) {
    await Cart.updateOne({ goodsId }, { $set: { quantity } });
  } else {
    await Cart.create({ goodsId: goodsId, quantity: quantity });
  }
  res.send({ result: "success" });
});

module.exports = router;