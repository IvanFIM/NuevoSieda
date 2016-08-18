
$(document).ready(function () {


    var osChartConfig = {
    "type": "serial",
    "categoryField": "Maestro_id__Nombre",
    "startDuration": 1,
    "theme": "light",
    "categoryAxis": {
        "gridPosition": "start",
        "boldLabels": true,
        "labelRotation": 45
    },
    "chartScrollbar": {
        "enabled": true
    },
    "trendLines": [],
    "graphs": [
        {
            "fillAlphas": 1,
            "id": "AmGraph-1",
            "title": "graph 1",
            "type": "column",
            "balloonText": "Total evaluaciones: <b>[[num]]</b>",
            "labelText": "[[total]]",
            "valueField": "total"
        }
    ],
    "guides": [],
    "valueAxes": [
        {
            "id": "ValueAxis-1",
            "title": "Calificación total ",
        }
    ],
    "allLabels": [],
    "balloon": {
        "fixedPosition": false,
     
    },
    "titles": [
        {
            "id": "Title-1",
            "size": 15,
            "text": "Resultados de evaluación: Maestros"
        }
    ],
    "dataProvider": [],
    "export": AmCharts.exportCFG
};
   

    var g = GetURLParameter('grupo');
    var c= GetURLParameter('carrera');
    $.get('/lista/grupos/?grupo='+g+'&carrera='+c).done(function (data) {
      
        osChartConfig.dataProvider = data;
        var chart = AmCharts.makeChart('chartdiv', osChartConfig);

    }).fail(function (err) {
        console.log(err)
    });

});

 function GetURLParameter(sParam)
    {
        var sPageURL = window.location.search.substring(1);
        var sURLVariables = sPageURL.split('&');
        for (var i = 0; i < sURLVariables.length; i++)
        {
            var sParameterName = sURLVariables[i].split('=');
            if (sParameterName[0] == sParam)
            {
                return decodeURIComponent(sParameterName[1]);
            }
        }
    }