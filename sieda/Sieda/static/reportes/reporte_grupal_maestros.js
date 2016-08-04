
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

    $.get('/lista/grupos/').done(function (data) {
      
        osChartConfig.dataProvider = data;
        var chart = AmCharts.makeChart('chartdiv', osChartConfig);

    }).fail(function (err) {
        console.log(err)
    });

});
