import Child from "./Child"
import Child_2 from "./child2"
import Child_3 from "./Child3"
import Child_4  from "./Child4"
import Child_5 from "./Child5"

function App(){
  let info={
        name:'sultan mirza',
        city:'saudi',
        work:'engineer'
    }
  return (
    <>
    <Child name='usmani ye props hold kr rha hai'  age={20} collage='RITS'/>
    <Child_2 name='Amjad' age={25}/>
    <Child_3 name='fahad Usmani' city='mumbai' />
    <Child_4 city='dubai' contact={342654887}/>
    <Child_5 data={info}/>

    </>
  )
}

export default App

