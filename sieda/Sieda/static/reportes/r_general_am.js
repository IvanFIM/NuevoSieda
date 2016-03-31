
$(document).ready(function () {


    var osChartConfig = {
    "type": "serial",
    "categoryField": "Seccion",
    "startDuration": 1,
    "theme": "light",
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
            "valueField": "Calificacion"
        }
    ],
    "guides": [],
    "valueAxes": [
        {
            "id": "ValueAxis-1",
            "title": "Axis title"
        }
    ],
    "allLabels": [],
    "balloon": {},
    "titles": [
        {
            "id": "Title-1",
            "size": 15,
            "text": "Reporte General"
        }
    ],
    "dataProvider": []
};

    $.get('/lista/jefes/').done(function (data) {
        var data2 = [];
        $.each(data,function(key, value){
            data2.push({
                Seccion: value.fields.Seccion,
                Calificacion: value.fields.Calificacion
            });
        });

        osChartConfig.dataProvider = data2;
        var chart = AmCharts.makeChart('chartdiv', osChartConfig);

    }).fail(function (err) {
        console.log(err)
    });

});
