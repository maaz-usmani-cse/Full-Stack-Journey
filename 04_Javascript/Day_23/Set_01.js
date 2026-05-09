/*

API-->> application programing interface
asynchronous and synchro

*/




async function access(){
    let data=await fetch('https://jsonplaceholder.typicode.com/posts')
    let res=await data.json()
    let show_res=res.map((x)=>
        <tr>
    

        </tr>




)
}
    

access()






