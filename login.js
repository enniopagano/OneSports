let API = "http://192.168.44.118:3306";
let boton = document.getElementById("boton_submit")
let usuario = document.getElementById("user")
let contraseña = document.getElementById("contraseña")
let h1_mensaje = document.getElementById("mensaje")
contraseña.addEventListener("change",(e)=>{
  contra = e.target.value
  console.log(contra)
})
usuario.addEventListener("change",(e)=>{
  nombre = e.target.value
  console.log(usuario)
}) 
boton.addEventListener("click",async function  handle_submit(e) {
  e.preventDefault()
  const respuesta = await fetch(`${API}/inicio_sesion`,{
    method:["POST"],
    headers:{"Content-Type":"application/json"
  },
  body: JSON.stringify ({
    nombre,
    contra
  })
  })
  
  const data = await respuesta.json();
  console.log(data)
  console.log(data.sesion);
  if (data.sesion =="falso") {
    mensaje = data.mensaje;
    localStorage.setItem('sesion', "false");

    console.log(mensaje);
    h1_mensaje.innerHTML = data.mensaje

  }else{
     //depurador
    let usernameToJson = JSON.stringify(data)
    console.log("mi nombre es:"+data.nombre)
    localStorage.setItem('sesion', "true");
    localStorage.setItem('nombre', data.nombre);
    h1_mensaje.innerHTML = data.nombre
  }
})
let btn_cerrar = document.getElementById("boton_cerrar")
btn_cerrar.addEventListener("click",()=>{
  localStorage.clear();
})