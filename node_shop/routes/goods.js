const express = require('express');
const Goods = require('../schemas/goods');

const router = express.Router();
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

router.get('/goods/:goodsId',async (req,res)=>{
  const {goodsId} = require.params;
  goods = await Goods.findOne({goodsId : goodsId});
  res.json({detail : goods}); 
  //TODO: 몽고디비 부분은 따로 알아보자.
})


module.exports = router;