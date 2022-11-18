let API = "http://127.0.0.1:5000";
let boton = document.getElementById("boton_submit");
let usuario = document.getElementById("user");
let contraseña = document.getElementById("contraseña");
let mensaje = document.getElementById("mensaje");
contraseña.addEventListener("change",(e)=>{
  contra = e.target.value;
  console.log(contra)

})
usuario.addEventListener("change",(e)=>{
  nombre = e.target.value;
  console.log(usuario)
}) 
boton.addEventListener("click",async function  handle_submit(e) {
  e.preventDefault();
  const respuesta = await fetch(`${API}/crear`,{
    method:["POST"],
    headers:{"Content-Type":"application/json"
  },
  body: JSON.stringify ({
    nombre,
    contra
  })
  })
  
  const data = await respuesta.json();
  console.log(data);
  console.log(data.sesion);
  if (data.cuenta =="existente") {
    let mensaje1 = data.mensaje;
    localStorage.setItem('sesion', "false");

    console.log(mensaje1);
    mensaje.innerHTML = mensaje1

  }else{
    let mensaje1 = data.mensaje;
    let usernameToJson = JSON.stringify(data);
    console.log("mi nombre es:"+data.nombre);
    localStorage.setItem('sesion', "true");
    localStorage.setItem('nombre', data.nombre)
    mensaje.innerHTML = mensaje1
  }
})