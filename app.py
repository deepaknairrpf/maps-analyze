import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

#External CSS
external_css = ["https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
                "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css", ]

for css in external_css:
    app.css.append_css({"external_url": css})

#External JavaScript
external_js = ["http://code.jquery.com/jquery-3.3.1.min.js",
               "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})

#Internal CSS
colors = {
         'background': '#0000FF',
         'color': '#FFA500'
}

#Our app's Layout
app.layout = html.Div(style=colors,children=[
    html.H1(children='Iris visualization',style={'textAlign':'center'}),
html.Div(style={'textAlign':'center'},children='''
     Built with Dash: A web application framework for Python.
    ''')
])
if __name__ == '__main__':
    app.run_server(debug=True)
