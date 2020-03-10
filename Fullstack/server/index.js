const express = require('express');
const app = express()
const http = require('http').createServer(app);
const io = require('socket.io')(http)
const cors = require('cors')
const helmet = require('helmet')

app.use(express.json())
app.use(cors())
app.use(helmet())

app.get('/', (req, res) => {
    res.status(200).json({ message: "We are live" })
})

io.on('connection', function (socket) {
    console.log("We are here",socket.id)

    socket.on('counter', data => {
        io.sockets.emit('counter', data)
    })
});

http.listen(5000, function () {
    console.log('listening on *:5000');
});  