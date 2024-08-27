let nombre = "Alex";
let apellido = "Perdel";
let estudiante = `${nombre} ${apellido}`;
let estudianteMayus = estudiante.toUpperCase();
let estudianteMinus = estudiante.toLowerCase();

let estudianteLength = estudiante.length;
let nombreStart = nombre.substring(0,1);
let apellidoEnd = apellido.substring(5);

let espacioEstudiante = estudiante.trim();
let quitarEspaciosEstudiante = espacioEstudiante.replace (/ /g, "");
let nombreEstudiante = estudiante.includes(nombre)

console.log(nombreEstudiante)