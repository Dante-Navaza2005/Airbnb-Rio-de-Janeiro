# Reducing visualized data

To facilitate rigorous comparisons and statistical analyses leveraging longitude and latitude data sourced from the dataframe, we will employ plotly.express to construct a Mapbox visualization. This visualization will accurately depict each property at its respective geographical coordinates, alongside with its corresponding price point.

However, in order to avoid crashes and slowdowns, only the first 70,000 samples will be visualized.

```python
data = main_dataframe.sample(71000)
center = {'lat':data.latitude.mean(), 'lon':data.longitude.mean()}
map_graph = px.density_mapbox(data, lat='latitude', lon='longitude',z='price', radius=2.5, center=center, zoom=10, mapbox_style='open-street-map')
```
