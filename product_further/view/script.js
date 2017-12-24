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

//按产品分类
var dict = new Array();
for (var index in dataSet) {
    var item = dataSet[index];
    if (dict[item.product] == null) {
        dict[item.product] = [];
    }
    dict[item.product].push([new Date(item.complete_time), item.further_wight, item.further_name, item.further_type, item.description]);
}
console.log(dict);

//整合后的数据带入了图形中

var chart_legned = [];
var chart_data = [];
var symbols = ['circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'];
for (var key in dict) {
    var series_item = {
        name: '产品名',
        type: 'scatter',
        tooltip: {
            trigger: 'item',
            formatter: function (params) {
                //[2.further_name, 3.further_type, 1.further_wight, 4.description, 0.complete_time]
                return '[' + params.seriesName + ']'
                    + '[' + params.value[2] + ']'
                    + '[' + params.value[3] + ']'
                    + '<br/>'
                    + params.value[4];
            },
            axisPointer: {
                type: 'cross',
                lineStyle: {
                    type: 'dashed',
                    width: 1
                }
            }
        },
        //标识形状 ，产品
        symbol: 'circle',
        //标识尺寸，权重
        symbolSize: function (value) {
            return Math.round(parseInt(value[1]));
        },
        data: []
    };
    //setting
    chart_legned.push(key);
    series_item.name = key;
    series_item.symbol = 'circle';
    series_item.data = dict[key];
    chart_data.push(series_item);
}
console.log(chart_data);

var myChart = echarts.init(document.getElementById('chart_1'));
var option = {
    title: {
        text: '任务散点图',
        subtext: '2018年'
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
    // dataZoom: {
    //     show: true,
    //     start: 20,
    //     end: 80
    // },
    legend: {
        data: chart_legned//['e-server']
    },
    grid: {
        y2: 80
    },
    xAxis: [
        {
            type: 'time',
            min: new Date(2018, 0),
            max: new Date(2018, 12),
            splitNumber: 6,
        }
    ],
    yAxis: [
        {
            type: 'value'
        }
    ],
    animation: false,
    series: chart_data
};

myChart.setOption(option);