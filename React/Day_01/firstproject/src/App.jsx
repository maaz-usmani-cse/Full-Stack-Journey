
import DevAbout from './daily_backup/Day_01_Basics/About';          
import { Frontend, Backend } from './daily_backup/Day_01_Basics/Skills'; 
import myimage from './assets/tumhari.webp'
function App() {
  let mycss={
    backgroundColor:"red",
    color:'white'
  }
  return (
    <div style={{ padding: '30px', fontFamily: 'sans-serif' }}>
      <h1>My First React Project 🚀</h1>
      
      
      <DevAbout />

      <hr />
      <h3 style={mycss}>Technical Expertise:</h3>
      <ul><object data="" type=""></object>
       
        <Frontend />
        <Backend />
        {/* <Image/> */}
         <img src={myimage} />
      </ul>
      
    </div>
    
  );
}
export default App;