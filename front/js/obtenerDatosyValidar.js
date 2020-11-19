$(document).ready(function(){
    $('#LoginFallido').hide();
    $('#FaltanCampos').hide();

    $('#UsuarioTexto').change(function(){
        $('#LoginFallido').hide();
        $('#FaltanCampos').hide();
    });

    $('#ContraseñaTexto').change(function(){
        $('#LoginFallido').hide();
        $('#FaltanCampos').hide();
    });

    $('#Entrar').click(async function(){
        $('#LoginFallido').hide();
        $('#FaltanCampos').hide();

        usuario = $('#UsuarioTexto').val();
        contraseña = $('#ContraseñaTexto').val();

        if (!usuario || !contraseña){
            $('#FaltanCampos').show(300);
        } else {        
            resultadoValidacion = await eel.validarEntrada(usuario, contraseña)();

            if (resultadoValidacion == 1) {
                eel.abrirPaginaDatos();
            } else {
                $('#LoginFallido').show(300);
            };
        }
    });
});