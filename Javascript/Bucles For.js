// Bucles For

//For
for (let i=0; i<10; i++){
    console.log(i)
}
// For con array
let lista = [1,3,5,7,9]
for (let i = 0; i<lista.length;i++){
    console.log(lista[i])
}

//For Of
for (let valor of lista) {
    console.log(valor)
    
}

//For Each
lista.forEach(valor => {
   console.log(valor) 
});




//For IN
let persona = {
    nombre: "Alex",
    apellido: "Perdel",
    edad: 38,
    isDeveloper: false,
}

for (let propiedad in persona){
    console.log(persona[propiedad]);
}