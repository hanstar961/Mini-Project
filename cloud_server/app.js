const port = 8080;
const express = require('express');
const http = require('http');

const app = express();
const server = http.createServer(app);
const io = require('socket.io')(server);

let client_dict = {};

server.listen(port);

app.get('/', function (req, res) {
    res.sendfile(__dirname + '/index.html');
});

console.log('start!');
io.on('connect', function connection(socket) {
    console.log('Someone is connected!');
    console.log('Someone ID:');
    console.log(socket.id);

    socket.on('client_type', function saveClient(clientName) {
        if (clientName === 'pi'){
            client_dict.pi = socket.id;
            console.log('This is pi ID:');
            console.log(client_dict.pi);
        }
        else if (clientName === 'chloe'){
            client_dict.chloe = socket.id;
            console.log('This is chloe ID:');
            console.log(client_dict.chloe);
        }
    });

    socket.on('piano_button', function pianoRequest(button) {
        console.log('piano message arrived with ' + button);
        if (button === 'piano'){
            io.to(client_dict.pi).emit('piano');
        }
    });

    socket.on('drum_button', function drumRequest(button) {
        console.log('drum message arrived with ' + button);
        if (button === 'drum'){
            io.to(client_dict.pi).emit('drum');
        }
    });
});
