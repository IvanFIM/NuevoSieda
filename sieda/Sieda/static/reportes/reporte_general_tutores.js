
$(document).ready(function () {


    var osChartConfig = {
    "type": "serial",
    "categoryField": "Tutor_id__Maestro__Nombre",
    "startDuration": 1,
    "theme": "default",
    "categoryAxis": {
        "gridPosition": "start",
        "boldLabels": true
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
            "text": "Resultados de evaluación: Tutores"
        }
    ],
    "dataProvider": [],
    "export": AmCharts.exportCFG
};

    $.get('/lista/g_tutores/').done(function (data) {
      
        osChartConfig.dataProvider = data;
        var chart = AmCharts.makeChart('chartdiv', osChartConfig);

    }).fail(function (err) {
        console.log(err)
    });

});
