import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
data = pd.read_csv("reviews.csv", parse_dates = ["Timestamp"])
data["Month"] = data["Timestamp"].dt.strftime("%Y %m")
month_average_crs = data.groupby(["Month","Course Name"])["Rating"].count().unstack()

chart_def = """
 {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in May, 2020'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 70.67,
            sliced: true,
            selected: true
        }, {
            name: 'Edge',
            y: 14.77
        },  {
            name: 'Firefox',
            y: 4.86
        }, {
            name: 'Safari',
            y: 2.63
        }, {
            name: 'Internet Explorer',
            y: 1.53
        },  {
            name: 'Opera',
            y: 1.40
        }, {
            name: 'Sogou Explorer',
            y: 0.84
        }, {
            name: 'QQ',
            y: 0.51
        }, {
            name: 'Other',
            y: 2.6
        }]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Analysis of course review", classes = "text-h4 text-center q-pa-md")
    p1 = jp.QDiv(a = wp, text = "These graph represent course review analysis")
    hc = jp.HighCharts(a = wp, options = chart_def)
    hc.options.title.text = "Average rating by week"

    # hc.options.xAxis.categories = list(month_average_crs.index)

    hc_data = [{"name":v1, "y":[v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]

    hc.options.series.data = hc_data


    return wp

jp.justpy(app)