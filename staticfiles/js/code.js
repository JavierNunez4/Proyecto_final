function registrarseFunction(){
    todoOk = true;

    if(!validarNombreVacio()) todoOk =false;
    if(!validarApellidoVacio()) todoOk = false;
    if(!validarContraVacio()) todoOk = false;
    if(!validarContra()) todoOk = false;


    if (todoOk) {
        document.miformulario.action="";
        document.miformulario.submit();
        return true;
    }
    return false;
    
}


function cambiarColor(id, color){
    n = document.getElementById(id);
    n.classList.remove('rojo');
    n.classList.remove('verde');
    n.classList.add(color);
}

function validarNombreVacio(){
    inputNombre = document.miformulario.txt_nombre;
    if(inputNombre.value.trim().length==0){
        cambiarColor('ok01', 'rojo');
        return false;
    }
    cambiarColor('ok01', 'verde');
    return true;
    
}


function validarApellidoVacio(){
    inputApellido = document.miformulario.txt_apellido;
    if(inputApellido.value.trim().length==0){
        cambiarColor('ok02', 'rojo');
        return false;
    }
    cambiarColor('ok02', 'verde');
    return true;
    
}

function validarContraVacio(){
    inputContra = document.miformulario.txt_contra;
    if(inputContra.value.trim().length >= 8 && inputContra.value.trim().length <= 24){
        cambiarColor('ok03', 'verde');
        return true;
    }
    cambiarColor('ok03', 'rojo');
    return false;
    
}

function validarContra(){
    inputContra2 = document.miformulario.txt_contra2;
    inputContra = document.miformulario.txt_contra;
    if(inputContra.value.trim().length == 0 || inputContra2.value.trim().length ==0 ){
        cambiarColor('ok04','rojo');
        return false;
    }else{
        if(inputContra.value == inputContra2.value){
            cambiarColor('ok04', 'verde');
            return true;
        }
        cambiarColor('ok04', 'rojo');
        return false; 

    }  
    
}
