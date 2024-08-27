const array1 = [1,2,3,4,5]
const array2 = [6,7,8,9,10]

const array3 = array1.concat(array2); // Concatenación de listas
console.log(array3) // [1,2,3,4,5,6,7,8,9,10]

const array4 = [...array1,...array2];// Factor de propagación
console.log (array4); // [1,2,3,4,5,6,7,8,9,10]

//ERRORES

const array5 = [array1 + array2];
console.log (array5) // ['1,2,3,4,56,7,8,9,10'] Es un String

const array6 = [array1, array2];
console.log (array6) // [ [1,2,3,4,5] [6,7,8,9,10] ] Es una lista con dos listas dentro

