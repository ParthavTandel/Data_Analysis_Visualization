import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Analysis of course review", classes = "text-h4 text-center q-pa-md")
    p1 = jp.QDiv(a = wp, text = "These graph represent course review analysis")
    return wp

jp.justpy(app)