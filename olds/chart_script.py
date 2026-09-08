import plotly.graph_objects as go
import pandas as pd

# Data from the provided JSON
categorias = ["Género Vocal", "Rangos Vocales", "Estilos Vocales Rock/Metal", "Técnicas Vocales Específicas", "Efectos y Texturas Vocales", "Géneros Específicos Rock/Metal", "Etiquetas de Sección para Voces"]
cantidad_tags = [6, 7, 16, 10, 19, 17, 10]

# Abbreviate category names to fit 15 character limit
categorias_abrev = [
    "Género Vocal",
    "Rangos Vocales", 
    "Estilos R/M",
    "Técnicas Esp",
    "Efectos/Text",
    "Géneros R/M",
    "Etiq. Sección"
]

# Create horizontal bar chart
fig = go.Figure()

fig.add_trace(go.Bar(
    y=categorias_abrev,
    x=cantidad_tags,
    orientation='h',
    marker_color='#1FB8CD'
))

fig.update_layout(
    title="Vocal Tags by Category",
    xaxis_title="Tag Count",
    yaxis_title="Category"
)

fig.update_traces(cliponaxis=False)

# Save as both PNG and SVG
fig.write_image("vocal_tags_chart.png")
fig.write_image("vocal_tags_chart.svg", format="svg")

fig.show()