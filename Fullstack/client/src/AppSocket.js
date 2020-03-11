import React,{useEffect,useState} from 'react';
import socketIOClient from "socket.io-client";


function App() {
  const [counter,setCounter] = useState(0)
  const [socket,setSocket] = useState(null)


  const handleChange = () => {
    setCounter(counter + 1)
    socket.emit('counter', counter + 1)
  }

  useEffect(()=>{
    const socket = socketIOClient('http://localhost:5000');
    setSocket(socket)
  },[])

  useEffect(() => {
    if(socket){
      socket.on('counter',data => {
        setCounter(data)
      })
    }
  },[counter])

  return (
    <div className="App">
     <div>Hello World</div>
     <h2>{counter}</h2>
     <button onClick={handleChange} >Increase</button>
    </div>
  );
}

export default App;
