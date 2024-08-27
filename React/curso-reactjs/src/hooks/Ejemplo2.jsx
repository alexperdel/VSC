/**
 * Ejemplo de uso de:
 * - useState() 
 * - useRef() para referenciar elementos dentro del HTML
 * - useEffect() para controlar los cambios en el HTML
 */

import React, {useState, useRef, useEffect} from 'react';

const Ejemplo2 = () => {


// Vamos a crear dos contadores distintos, cada uno en un estado.

const [contador1, setContador1] = useState(0);
const [contador2, setContador2] = useState(0);

// Crear un REFERENCIA con useRef para asociar una var con un elemento del HTML

const miRef = useRef();

function incrementar1() {
    setContador1(contador1+1)
}

function incrementar2() {
    setContador2(contador2+10)
}

// Trabajando con useEffect
// Caso 1: Ejecutar SIEMPRE un snippet de código, cuando se hace un cambio en el componente

    // useEffect(() => {o
    //     cnsole.log('Cambio en el estado del componente, se referencia en');
    //     console.log(miRef);

    //     })


// Caso 2: Ejecutar SOLO cuando cambie el contador1
        
    // useEffect(() => {
    //     console.log('Cambio en el estado del componente, se referencia en')
    //     console.log(miRef)
        
    // }, [contador1]);


// Caso 3: Ejecutar SOLO cuando si hay cambio en contador1 o contador2. 

    useEffect(() => {
        console.log('Cambio en el estado del componente, se referencia en')
        console.log(miRef)
       
    }, [contador1,contador2]);


    return (
        <div>
          <h3>Ejemplo de useStage, useRef, useEffect</h3>        
            <h4>Contador1: {contador1}</h4>
            <h4>Contador2: {contador2}</h4>
            {/*Elemento referenciado */}
            <h5 ref={miRef}>Ejemplo de elemento referenciado</h5>
            <div>
                <button onClick={incrementar1}>Aumetar +1</button>
                <button onClick={incrementar2}>Aumentar +10</button>
            </div>
        </div>

    );
}

export default Ejemplo2;
