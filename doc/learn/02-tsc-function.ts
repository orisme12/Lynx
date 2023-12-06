function great_world(name: string) {
  return name;
}

great_world('10');

function return_func(): number {
  return 10;
}

return_func();


// Tipar objetos en funciones -- forma 1

function saludar({name , age}: {name:string , age : number}){
 console.log(`Hola ${name}, tienes ${age} años`)
}
saludar({name: 'Carlos', age:27})


//  Tipar objetos en funciones -- forma 1

function saludar2(persona:{name:string, age: number } ){
  const {name, age } = persona
  console.log(`Hola ${name}, tienes ${age} años`)
 }
 saludar2({name: 'Carlos', age:27})


// Indicarle a la función que tipo de dato será retornado

 function saludar3({name , age}: {name:string , age : number}):string{
  
  console.log(`Hola ${name}, tienes ${age} años`)
  return name  
 }
 saludar3({name:'Carlos',age : 27})


// Tipar funciones que se usan como parametros dentro de otra función

const sayHiFunction = (fn:(name : string) => void) =>{
  fn('felipe')
}

const sayHi = (name : string) =>{
  console.log(`Hola ${name}`)
}
sayHiFunction(sayHi)

// Tipar arrow functions -- Forma 1

const sumar = (a:number , b: number): number =>{
  return a + b
}
console.log(sumar(2,3))

// Tipar arrow functions -- Forma 2

const dividir: (a:number , b: number) => number = (a,b) => {
  return a / b
}
console.log(dividir(10,3))



// autocompletado

let str = '10';

str.toLowerCase();
str.split(' ');
str.slice(10)

