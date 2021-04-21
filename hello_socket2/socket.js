const WebSocket = require("ws");

module.exports = (server) => {
	const wss = new WebSocket.Server({ server });

	wss.on("connection", (ws, req) => {
		//클라이언트의 ip를 알아내는 코드
		//proxy addr패키지를 사용해도 좋다고 함
		const ip = req.headers["x-forwarded-for"] || req.connection.remoteAddress;

		console.log("새로운 클라이언트 접속", ip);
		//클라이언트로부터 메세지를 받았을 때 발생
		ws.on("message", (message) => {
			console.log(message);
		});
		//웹소켓 연결 중 문제 발생 시 발생
		ws.on("error", (error) => {
			console.log(error);
		});
		//클라이언트와 연결이 끊겼을 때 발생
		ws.on("close", () => {
			console.log("클라이언트 접속 해제", ip);
			//setInterval로 계속해서 서버에 메세지를 보내는 행위를 멈춤
			//메모리 누수 방지
			clearInterval(ws.interval);
		});
		//3초마다 연결 된 모든 클라이언에게 메세지를 보냄
		const interval = setInterval(() => {
			//readyState가 open인지 확인 후 (CONNECTING, OPEN, CLOSING, CLOSED 중 1개의 상태 )
			if (ws.readyState === ws.OPEN) {
				ws.send("서버에 클라이언트로 메세지를 보냅니다.");
			}
		}, 3000);
		ws.interval = interval;
	});
};
