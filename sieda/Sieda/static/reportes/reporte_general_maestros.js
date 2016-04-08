
$(document).ready(function () {


    var osChartConfig = {
    "type": "serial",
    "categoryField": "Maestro_id__Nombre",
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
            "labelText": "[[Total]]",
            "valueField": "Total"
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
        "enabled":false
    },
    "titles": [
        {
            "id": "Title-1",
            "size": 15,
            "text": "Acumulado de Resultados: Maestros"
        }
    ],
    "dataProvider": [],
    "export": AmCharts.exportCFG
};

    $.get('/lista/g_maestros/').done(function (data) {
      
        osChartConfig.dataProvider = data;
        var chart = AmCharts.makeChart('chartdiv', osChartConfig);

    }).fail(function (err) {
        console.log(err)
    });

});
/*   $.get('/lista/g_maestros/').done(function (data) {
        var data2 = [];
        $.each(data,function(key, value){
            data2.push({
                Maestro_id: value.fields.Maestro_id,
                Total: value.fields.Total
            });
        });

        osChartConfig.dataProvider = data;
        var chart = AmCharts.makeChart('chartdiv', osChartConfig);

    }).fail(function (err) {
        console.log(err)
    });*/