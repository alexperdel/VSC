import React, {useState} from 'react';
import PropTypes from 'prop-types';



const FGreeting = (props) => {

    // Breve introducción a useStage
    // const [variable, métido para iniciarlizarla] = useStage(valor inicial)
   const [age, setage] = useState(39);

   const fbirthday = () =>{
    //actualizamos Stage
    setage(age+1);
   }

    return (
        <div>
                <h1>
                    Hello {props.name} desde componente Funcional!
                </h1>
                
                <h2>You're: {age} years old.</h2>

                <div>
                    <button onClick={fbirthday}>
                        It's your birthday
                    </button>
                </div>
        </div>
    );
};


FGreeting.propTypes = {
    name:PropTypes.string,
};


export default FGreeting;


