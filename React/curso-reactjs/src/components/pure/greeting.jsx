import React, { Component } from 'react';
import PropTypes from 'prop-types';



class Greeting extends Component {

    constructor(props){
        super(props)
        this.state ={
            age : 39
        }
    }

    

    render() {
        return (
            <div>
                <h1>
                    Hello {this.props.name}!
                </h1>
                <h2>You're: {this.state.age} years old.</h2>

                <div>
                    <button onClick={this.birthday}>
                        It's your birthday
                    </button>
                </div>

            </div>
        );
    }

    birthday = () =>{
        this.setState((prevStage)=>(
            {
                age: prevStage.age + 1
            }
        )
        )
    }   

}


Greeting.propTypes = {
    name: PropTypes.string,
};


export default Greeting;
