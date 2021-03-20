const mongoose = require('mongoose');

const { Schema } = mongoose;
const cartSchema = new Schema({
  goodsId: {
    type: Number,
    require: true,
    unique: true
  },
  quantity: {
    type: Number,
    require: true
  }
});

module.export = mongoose.model("Cart",cartSchema);