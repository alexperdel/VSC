/** Ejemplo de uso del Hook useState 
 * Crear un componente de tipo Función, para acceder a su estado privado
 * a través de un Hook. Y además, poder modificarlo.
 * 
*/

import React, {useState} from 'react';

const Ejemplo1 = () => {


// Valor inicial para el contador
const valorInicial = 0;

// Valor inicial para una persona
const personaInicial = {
    nombre: 'Alex',
    email: 'aperdel@gmail.com'
}

/** Queremos que el VALOR INICIAL y que PERSONA INICIAL
 * sean parte del estado del componente, para así poder 
 * gestionar su cambio, y que este se vea reflejado, en el HTML
 * 
 * const [nombreVariable, funcionParaCambiar] = useStage(valorInicial)
 * 
 */

    const [contador, setContador] = useState(valorInicial);
    const [persona, setPersona] = useState(personaInicial);


/**
 *  Función para actualizar el estado privado de contador
 */
    function incrementarContador() {
        setContador(contador + 1)
    }

/**
 * Función para actualizar el estado de persona en el HTML
 */
    function actualizarPersona() {
        setPersona(
            {
                nombre:'Wedge',
                email: 'wedge@rebellion.com'
            }
        )
        
    }







    return (
        <div>
            <h4>Ejemplo de useStage()</h4>
            <h5>Contador: {contador}</h5>
            <h5>Persona:</h5>
            <p>Nombre: {persona.nombre}</p>
            <p>Email: {persona.email}</p>
     
        <div>
        {/*Bloque de botones para actualizar los estados*/}            
        </div>
        <button onClick={incrementarContador}>Actulizar Contador</button>
        <button onClick={actualizarPersona}>Actualizar Persona</button>
        </div>
    );
}

export default Ejemplo1;


