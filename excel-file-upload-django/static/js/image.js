
window.onload = function () {
    for (var i=0;i<context.length;i++){
        var chart = new CanvasJS.Chart('chartContainer1', {
            animationEnabled: true,
            title:{
	            text: context[i]['title']
            },
            axisY: {
                interval: 100
            },
            dataPointMaxWidth: 20,
            data: [{
                type: "boxAndWhisker",
                upperBoxColor: "#FFC28D",
                lowerBoxColor: "#9ECCB8",
                stemThickness:2,
                whiskerThickness:2,
                lineThickness:2,
                color: "black",
                dataPoints: [
                    { label: "Registered Nurse", y: [context[i]['Q'][0], context[i]['Q'][1], context[i]['Q'][3], context[i]['Q'][4], context[i]['Q'][2] ]}, 
                ]
            }]
        });
        chart.render();
    }
}







/*var chart = new CanvasJS.Chart(MyViewVar.var_1[0], {
animationEnabled: true,
title:{
    text: "Annual Salary Range - USA"
},
axisY: {
    title: "Annual Salary (in USD)",
    prefix: "$",
    interval: 40000
},
data: [{
    type: "boxAndWhisker",
    upperBoxColor: "#FFC28D",
    lowerBoxColor: "#9ECCB8",
    color: "black",
    yValueFormatString: "$#,##0",
    dataPoints: [
        { label: "Registered Nurse", y: [123, 55320, 82490, 101650, 71000] },
       
    ]
}]
});
chart.render();

// 123
var chart = new CanvasJS.Chart(MyViewVar.var_1[1], {
animationEnabled: true,
title:{
    text: "Annual Salary Range - USA"
},
axisY: {
    title: "Annual Salary (in USD)",
    prefix: "$",
    interval: 40000
},
data: [{
    type: "boxAndWhisker",
    upperBoxColor: "#FFC28D",
    lowerBoxColor: "#9ECCB8",
    color: "black",
    yValueFormatString: "$#,##0",
    dataPoints: [
        { label: "Registered Nurse", y: [456, 55320, 82490, 101650, 71000] },
       
    ]
}]
});
chart.render();
*/

