$(document).ready(function () {
    $('#data_table').DataTable({
        data: dataSet,
        columns: [
            {data: "product"},
            {data: "further_name"},
            {data: "further_type"},
            {data: "further_wight"},
            {data: "description"},
            {data: "complete_time"}
        ]
    });
});


var myChart = echarts.init(document.getElementById('chart_1'));
var option = {
    title: {
        text: '时间坐标散点图',
        subtext: 'dataZoom支持'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            show: true,
            type: 'cross',
            lineStyle: {
                type: 'dashed',
                width: 1
            }
        }
    },
    toolbox: {
        show: true,
        feature: {
            mark: {show: true},
            dataView: {show: true, readOnly: false},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    dataZoom: {
        show: true,
        start: 30,
        end: 70
    },
    legend: {
        data: ['e-server', 'e-studio']
    },
    dataRange: {
        min: 0,
        max: 100,
        orient: 'horizontal',
        y: 30,
        x: 'center',
        color: ['orange', 'lightgreen'],
        splitNumber: 5
    },
    grid: {
        y2: 80
    },
    xAxis: [
        {
            type: 'time',
            min: new Date(2018, 0),
            max: new Date(2018, 12),
            splitNumber: 12,
        }
    ],
    yAxis: [
        {
            type: 'value'
        }
    ],
    animation: false,
    series: [
        {
            name: 'e-server',
            type: 'scatter',
            tooltip: {
                trigger: 'axis',
                formatter: function (params) {
                    var date = new Date(params.value[0]);
                    return params.seriesName
                        + ' （'
                        + date.getFullYear() + '-'
                        + (date.getMonth() + 1) + '-'
                        + date.getDate() + ' '
                        + date.getHours() + ':'
                        + date.getMinutes()
                        + '）<br/>'
                        + params.value[1] + ', '
                        + params.value[2];
                },
                axisPointer: {
                    type: 'cross',
                    lineStyle: {
                        type: 'dashed',
                        width: 1
                    }
                }
            },
            //标识尺寸
            symbolSize: function (value) {
                return Math.round(value[2] / 2);
            },
            // itemStyle: {
            //     normal: {
            //         color: function (param) {
            //             return json[0].marker.color[param.dataIndex];
            //         }
            //     }
            // },
            data: (function () {
                var d = [];
                var len = 0;
                var now = new Date();
                var value;
                while (len++ < 100) {
                    d.push([
                        new Date(2018, Math.floor(Math.random() * (12 - 1)) + 1, Math.floor(Math.random() * (28 - 1)) + 1),//完成时间
                        (Math.random() * 1000).toFixed(2) - 0,//权重
                        (Math.random() * 100).toFixed(2) - 0//任务总数？

                    ]);
                }
                console.log(d);
                return d;
            })()
        },
        {
            name: 'e-studio',
            type: 'scatter',
            tooltip: {
                trigger: 'axis',
                formatter: function (params) {
                    var date = new Date(params.value[0]);
                    return params.seriesName
                        + ' （'
                        + date.getFullYear() + '-'
                        + (date.getMonth() + 1) + '-'
                        + date.getDate() + ' '
                        + date.getHours() + ':'
                        + date.getMinutes()
                        + '）<br/>'
                        + params.value[1] + ', '
                        + params.value[2];
                },
                axisPointer: {
                    type: 'cross',
                    lineStyle: {
                        type: 'dashed',
                        width: 1
                    }
                }
            },
            //标识尺寸，权重
            symbolSize: function (value) {
                return Math.round(value[2] / 10);
            },
            data: (function () {
                var d = [];
                var len = 0;
                var now = new Date();
                var value;
                while (len++ < 100) {
                    d.push([
                        new Date(2018, Math.floor(Math.random() * (12 - 1)) + 1, Math.floor(Math.random() * (28 - 1)) + 1),
                        (Math.random() * 30).toFixed(2) - 0,
                        (Math.random() * 100).toFixed(2) - 0
                    ]);
                }
                console.log(d);
                return d;
            })()
        }
    ]
};

myChart.setOption(option);