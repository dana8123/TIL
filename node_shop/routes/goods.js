const express = require('express');
const router = express.Router();

router.get('/list', function(req,res,next){
  res.send('Router 상품목록 페이지')
});


module.exports = router;