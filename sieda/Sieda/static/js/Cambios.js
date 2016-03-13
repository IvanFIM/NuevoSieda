    $(document).on('ready',function(){
        $.ajax({
            type:"GET",
            contentType:"application/json; charsey=utf-8",
            dateType:"json",
            url:"/lista/secciones/",
            success:function(response){
                var i = (response.length-1);
                for(i;i<=(response.length-1);i++){
                    $('#Cambios').append("<li class='collection-item avatar email-unread email_last'><i class='icon_4 '>S</i><div class='avatar_left'><span class='email-title'>"+response[i].fields.Descripcion+"</span><p class='truncate grey-text ultra-small'>Sección</p></div><div class='clearfix'></div></li> <br>");
                }
            }
        });

        $.ajax({
            type:"GET",
            contentType:"application/json; charsey=utf-8",
            dateType:"json",
            url:"/lista/maestros/",
            success:function(response){
                var i = (response.length-1);
                for(i;i<=(response.length-1);i++){
                    $('#Cambios').append("<li class='collection-item avatar email-unread email_last'><i class='icon_4 icon_5'>M</i><div class='avatar_left'><span class='email-title'>"+response[i].fields.Nombre+"</span><p class='truncate grey-text ultra-small'>Maestro</p></div><div class='clearfix'></div></li> <br>");
                }
            }
        });
        $.ajax({
            type:"GET",
            contentType:"application/json; charsey=utf-8",
            dateType:"json",
            url:"/lista/jefes/",
            success:function(response){
                var i = (response.length-1);
                for(i;i<=(response.length-1);i++){
                    $('#Cambios').append("<li class='collection-item avatar email-unread email_last'><i class='icon_4 icon_6'>J</i><div class='avatar_left'><span class='email-title'>"+response[i].fields.Nombre+"</span><p class='truncate grey-text ultra-small'>Jefe de carrera</p></div><div class='clearfix'></div></li> <br>");
                }
            }
        });
        $.ajax({
            type:"GET",
            contentType:"application/json; charsey=utf-8",
            dateType:"json",
            url:"/lista/tutores/",
            success:function(response){
                var i = (response.length-1);
                for(i;i<=(response.length-1);i++){
                    $('#Cambios').append("<li class='collection-item avatar email-unread email_last'><i class='icon_4 icon_v7'>T</i><div class='avatar_left'><span class='email-title'>"+response[i].fields.Maestro+"</span><p class='truncate grey-text ultra-small'>Tutores</p></div><div class='clearfix'></div></li> <br>");
                }
            }
        });

    });