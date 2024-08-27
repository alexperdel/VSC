let lista = ["leche", "pan", "cerveza", "pasta", "fruta"]

lista.push ("aceite de girasol");
lista.pop();
console.log(lista);

let peliculas = [
    {nombre: "Rogue One", director : "Gareth Edwards", año: 2016},
    {nombre: "Kill Bill", director : "Tarantino", año: 2003},
    {nombre: "Harry Potter", director : "Chris Columbus", año: 2001}, 
    ]

const pelis_2010 = peliculas.filter(obj => obj.año >= 2010);
console.log(pelis_2010);

const pelis_director = peliculas.map(peliculas=>{
    return peliculas.director;
})
console.log(pelis_director)

const pelis_nombre = peliculas.map(peliculas=>{
    return peliculas.nombre;
})
console.log(pelis_nombre)

const peliDirectorTitulo = pelis_director.concat(pelis_nombre);
console.log(peliDirectorTitulo)

const peliTituloDirector = [...pelis_nombre,...pelis_director]
console.log(peliTituloDirector)


