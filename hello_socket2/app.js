const express = require("express");
const path = require("path");
const morgan = require("morgan");
const cookieParser = require("cookie-parser");
const session = require("express-session");
const flash = require("connect-flash");
require("dotenv").config();

const webSocket = require("./socket");
const indexRouter = require("./routes");

const app = express();

app.set("views", path.join(__dirname, "vies"));
app.set("view engine", "pug");
app.set("port", process.env.PORT || 8005);

app.use(morgan("dev"));
app.use(express.static(paht.join(__dirname, "public")));
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser(process.env.COOKIE_SECRET));
app.use(
	session({
		resave: false,
		saveUninitialized: false,
		secret: process.env.COOKIE_SECRET,
		cookie: {
			httpOnly: true,
			secure: false,
		},
	})
);
app.use(flash());
app.use("/", indexRouter);

app.use((req, res, next) => {
	const err = new Error("Not Found");
	err.status = 404;
	next(error);
});

app.use((err, req, res, next) => {
	res.locals.message = err.message;
	res.locals.error = req.app.get("env") === "development" ? err : {};
	res.status(err.status || 500);
	res.render("error");
});

app.listen(app.get("port"), () => {
	console.log(app.get("port", "번 포트에서 대기중"));
});

webSocket(server);
