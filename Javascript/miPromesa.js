const miPromesa = new Promise((ok,error) => {
    const i = Math.floor(Math.random()*2)
    if (i !== 0){
        ok()
    }else{
        error()
    }
})

miPromesa
    .then(()=> console.log("Es Ok"))
    .catch(()=>console.log("Es error"))







    