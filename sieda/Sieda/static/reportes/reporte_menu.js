AmCharts.makeChart("chartdiv",
	{
		"type": "serial",
		"categoryField": "category",
		"startDuration": 1,
		"theme": "light",
		"categoryAxis": {
			"gridPosition": "start",
			"title": ""
		},
		"chartCursor": {
			"enabled": false
		},
		"trendLines": [],
		"graphs": [
			{
				"fillAlphas": 1,
				"id": "AmGraph-1",
				"title": "graph 1",
				"type": "column",
				"valueField": "column-1",
				"labelText": "[[column-1]]"
			}
		],
		"guides": [],
		"valueAxes": [],
		"allLabels": [],
		"balloon": {},
		"titles": [],
		"dataProvider": [
			{
				"category": "Maestro-1",
				"column-1": "15"
			},
			{
				"category": "Maestro-2",
				"column-1": "20"
			},
			{
				"category": "Maestro-3",
				"column-1": "25"
			},
			{
				"category": "Maestro-4",
				"column-1": "30"
			}
		]
	}
);
AmCharts.makeChart("chartdiv2",
	{
		"type": "serial",
		"categoryField": "category",
		"startDuration": 1,
		"theme": "default",
		"categoryAxis": {
			"gridPosition": "start",
			"title": ""
		},
		"chartCursor": {
			"enabled": false
		},
		"trendLines": [],
		"graphs": [
			{
				"fillAlphas": 1,
				"id": "AmGraph-1",
				"title": "graph 1",
				"type": "column",
				"valueField": "column-1",
				"labelText": "[[column-1]]"
			}
		],
		"guides": [],
		"valueAxes": [],
		"allLabels": [],
		"balloon": {},
		"titles": [],
		"dataProvider": [
			{
				"category": "Tutor-1",
				"column-1": "15"
			},
			{
				"category": "Tutor-2",
				"column-1": "20"
			},
			{
				"category": "Tutor-3",
				"column-1": "25"
			},
			{
				"category": "Tutor-4",
				"column-1": "30"
			}
		]
	}
);
AmCharts.makeChart("chartdiv3",
	{
		"type": "serial",
		"categoryField": "category",
		"startDuration": 1,
		"theme": "patterns",
		"categoryAxis": {
			"gridPosition": "start",
			"title": ""
		},
		"chartCursor": {
			"enabled": false
		},
		"trendLines": [],
		"graphs": [
			{
				"fillAlphas": 1,
				"id": "AmGraph-1",
				"title": "graph 1",
				"type": "column",
				"valueField": "column-1",
				"labelText": "[[column-1]]"
			}
		],
		"guides": [],
		"valueAxes": [],
		"allLabels": [],
		"balloon": {},
		"titles": [
			{
				"id": "Title-1",
				"text": "Grupo:___"
			}
		],
		"dataProvider": [
			{
				"category": "Maestro-1",
				"column-1": "15"
			},
			{
				"category": "Maestro-3",
				"column-1": "25"
			},
			{
				"category": "Maestro-5",
				"column-1": "30"
			}
		]
	}
);