function motionSensorSub()
{
var zeromq = require('zmq');
 
var sock = zeromq.socket('sub');
sock.connect('tcp://127.0.0.1:5556');
sock.subscribe('motion');
 
sock.on('message', function(data) {
   console.log(data.toString());
});
}