import logo from './logo.svg';
import './App.css';
import Ejemplo4 from './hooks/Ejemplo4';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        
        {/* Componente propio Greeting.jsx */}
        {/* <Greeting name="Alex"></Greeting> */}
        {/* <FGreeting name="Wedge"></FGreeting> */}
        {/* <TaskListComponent></TaskListComponent>  */}
        <Ejemplo4 nombre="Alex">
        {/*Todo lo que hay aquí  es tratado como props.children*/}
          <h5>
            Contenido del props.children
          </h5>
        </Ejemplo4>

        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
