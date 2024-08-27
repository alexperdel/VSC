/**
 * Ejemplo Hooks de:
 * - useState()
 * - useContext() para trabajar con datos, utilizar el contexto 
 * y pasarselo a componentes superiores
 */

import React, {useState, useContext} from 'react';

const miContexto = React.createContext(null)


//Componente1 tiene un contexto que tiene un valor que recibe desde el padre

const Componente1 = () => {

    const state = useContext(miContexto)

    return (
        <div>
            <h1>
                EL Token es: {state.token}
            </h1>
            <Componente2></Componente2>
        </div>
    );
}


const Componente2 = () => {

    const state = useContext(miContexto);
    
    return (
        <div>
            <h2>
                La sesión es: {state.sesion}
            </h2>
        </div>
    );
}

const MiComponenteConContexto = () => {

    const estadoInicial = {
        token: '1138',
        sesion: 1
    }


    //Creamos el estado del componente

    const [sesionData, setsesionData] = useState(estadoInicial);

    function actualizarSesion() {
        setsesionData({
            token: 'THX302218',
            sesion: sesionData.sesion+1
        }
        )
        
    }

    return (
        <miContexto.Provider value = {sesionData}>
        {/*Todo lo que está aquí dentro, puede leer lo datos de sesionData */}
        {/*Si se actualiza, los componentes de aquí, también son actualizados */}
        <Componente1></Componente1>
        <button onClick={actualizarSesion}>Actualizar Sesión</button>
        </miContexto.Provider>
    );
}

export default MiComponenteConContexto;


