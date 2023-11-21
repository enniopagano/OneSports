let API = "http://192.168.44.118:3306";
let boton = document.getElementById("boton_submit");
let usuario = document.getElementById("user");
let contrasena = document.getElementById("contraseña");
let correo = document.getElementById("correo");
let mensaje = document.getElementById("mensaje");
contrasena.addEventListener("change",(e)=>{
  contra = e.target.value;
  console.log(contra)
})
usuario.addEventListener("change",(e)=>{
  nombre = e.target.value;
  console.log(usuario)
})
correo.addEventListener("change",(e)=>{
  correo = e.target.value;
  console.log(correo)
}) 
boton.addEventListener("click",async function  handle_submit(e) {
  e.preventDefault();
  const respuesta = await fetch(`${API}/crear`,{
    method:["POST"],
    headers:{"Content-Type":"application/json"
  },
  body: JSON.stringify ({
    nombre,
    contra,
    correo
  })
  })
  
  const data = await respuesta.json();
  console.log(data);
  console.log(data.sesion);
  if (data.nombre == "existe") {
    localStorage.setItem('sesion', "false");

    mensaje_existe = "Ese nombre de usuario ya existe, por favor elija otro"
    console.log(mensaje1);
    mensaje.innerHTML = mensaje_existe

  } else {
    let mensaje1 = data.mensaje;
    let usernameToJson = JSON.stringify(data);
    console.log("mi nombre es:" + data.nombre);
    localStorage.setItem('sesion', "true");
    localStorage.setItem('nombre', data.nombre)
    mensaje.innerHTML = mensaje1
  }
})