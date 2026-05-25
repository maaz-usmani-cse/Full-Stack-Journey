
// import DevAbout from './daily_backup/Day_01_Basics/About';          
// import { Frontend, Backend } from './daily_backup/Day_01_Basics/Skills'; 
// import myimage from './assets/tumhari.webp'
// function App() {
//   let mycss={
//     backgroundColor:"red",
//     color:'white'
//   }
//   return (
//     <div style={{ padding: '30px', fontFamily: 'sans-serif' }}>
//       <h1>My First React Project 🚀</h1>
      
      
//       <DevAbout />

//       <hr />
//       <h3 style={mycss}>Technical Expertise:</h3>
//       <ul><object data="" type=""></object>
       
//         <Frontend />
//         <Backend />
//         {/* <Image/> */}
//          <img src={myimage} />
//       </ul>
      
//     </div>
    
//   );
// }
// export default App;


// 📂 File: src/App.jsx

import Navbar from './components/Navbar';
import Footer from './components/Footer';

function App() {
  return (
    <div style={styles.mainLayout}>
      {/* 1. Sabse upar Navbar call kiya */}
      <Navbar />

      {/* 2. Bich ka main area content ke liye */}
      <main style={styles.contentArea}>
        <h2>Welcome to my Class Task 🎯</h2>
        <p>
          Sir, maine Navbar aur Footer ko alag-alag reusable components mein 
          baant kar, CSS apply karke ek dum industry standard par banaya hai.
        </p>
      </main>

      {/* 3. Sabse neeche Footer call kiya */}
      <Footer />
    </div>
  );
}

const styles = {
  mainLayout: {
    display: 'flex',
    flexDirection: 'column',
    minHeight: '100vh',
    background: '#121212', // Premium Dark Theme
    color: '#f0f0f0',
    margin: '-8px', // Browser ke default margin ko saaf karne ke liye
  },
  contentArea: {
    padding: '40px',
    textAlign: 'center',
    flex: 1,
  }
};

export default App;