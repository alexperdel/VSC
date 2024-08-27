// Funcion Generadora

function* generaId (){
    let id = 0;
    while (true){
        id++
        if (id===0){
            return id
        } 
        yield id
    }
}

const genId = generaId();

console.log(genId.next())