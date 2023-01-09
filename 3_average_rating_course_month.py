import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
data = pd.read_csv("reviews.csv", parse_dates = ["Timestamp"])
data["Month"] = data["Timestamp"].dt.strftime("%Y %m")
month_average_crs = data.groupby(["Month","Course Name"]).mean().unstack()

chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Moose and deer hunting in Norway, 2000 - 2021'
    },
    subtitle: {
        align: 'center',
        text: 'Source: <a href="https://www.ssb.no/jord-skog-jakt-og-fiskeri/jakt" target="_blank">SSB</a>'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 120,
        y: 70,
        floating: true,
        borderWidth: 1,
        backgroundColor:
             '#FFFFFF'
    },
    xAxis: {
        plotBands: [{ // Highlight the two last years
            from: 2019,
            to: 2020,
            color: 'rgba(68, 170, 213, .2)'
        }]
        categories: []
    },
    yAxis: {
        title: {
            text: 'Quantity'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Hunting season starting autumn {point.x}</b><br>'
    },
    credits: {
        enabled: false
    },
    series: [{
        name: 'Moose',
        data:
            [
                38000,
                37300,
                37892,
                38564,
                36770,
                36026,
                34978,
                35657,
                35620,
                35971,
                36409,
                36435,
                34643,
                34956,
                33199,
                31136,
                30835,
                31611,
                30666,
                30319,
                31766
            ]
    }, {
        name: 'Deer',
        data:
            [
                22534,
                23599,
                24533,
                25195,
                25896,
                27635,
                29173,
                32646,
                35686,
                37709,
                39143,
                36829,
                35031,
                36202,
                35140,
                33718,
                37773,
                42556,
                43820,
                46445,
                50048
            ]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Analysis of course review", classes = "text-h4 text-center q-pa-md")
    p1 = jp.QDiv(a = wp, text = "These graph represent course review analysis")
    hc = jp.HighCharts(a = wp, options = chart_def)
    hc.options.title.text = "Average rating by week"

    hc.options.xAxis.categories = list(month_average_crs.index)

    hc_data = [{"name":v1, "data":[v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]

    hc.options.series = hc_data


    return wp

jp.justpy(app)