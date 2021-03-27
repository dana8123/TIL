const express = require("express");
const connect  = require("./models/index");
const jwt = require("jsonwebtoken");
const User = require('./models/user');
const Cart = require('./models/cart');
const Goods = require('./models/goods');
const authMiddleware = require('./middlewares/auth-middleware');
const joi = require("joi");
const app = express();
const router = express.Router();

connect();

//joi validation
const userSchema = joi.object({
  email : joi.required()
            .email({ minDomainSegments: 2, tlds: { allow: ['com', 'net'] } }),
  password : joi.required()
            .pattern(new RegExp('^[a-z0-9]{3,30}$')),
  confirmPassword: joi.string()
            .required(),
  nickname : joi.string()
            .min(2)
            .max(10)
            .required(),
});

const authSchema = joi.object({
  email : joi.required(),
password : joi.required()
})

router.post("/users", async(req,res)=>{
  try{
    const{
      nickname,
      email,
      password,
      confirmPassword
    } = await userSchema.validateAsync(req.body);

  if(password != confirmPassword){
    res.stastus(400).send({
      errorMessage: '패스워드가 동일하지않습니다.'
    });
    return; //아래의 코드를 실행할 필요가 없다
  }


  const existUser = await User.find({
    $or: [{ email }, { nickname }],
  });
  if (existUser.length){
    res.status(400).send({
      errorMessage: '이미 가입된 이메일 또는 닉네임이 있습니다.'
    });
    return;
  }

  const user = new User({ email, nickname, password});
  await user.save();
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
    const { email, password  } = await authSchema.validateAsync(req.body);
  
  const user = await User.findOne({ email, password }).exec();
  
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


app.listen(8080, () => {
  console.log("서버가 요청을 받을 준비가 됐어요");
});