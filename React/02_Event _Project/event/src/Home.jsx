function Home(){
    function fun(name){
        alert(name)
        
    }
    return( 
    <>
    <button onClick={()=>fun('I love you')}>click </button>
    <button>click baby</button>
    </>)
  
}


export default Home