import xarray as xr
import hvplot.xarray
import panel as pn

# 1. Load Data
ds = xr.open_dataset('./air_temperature.nc')

plot = ds.air.hvplot.quadmesh(
    x='lon', y='lat', 
    title="NASA Climate Intelligence Dashboard Prototype",
    width=800, height=500,
    cmap='viridis',
    geo=True, coastline=True
)

app = pn.Column(
    "# NASA GSoC Project: Climate Intelligence",
    "### Interative visualization of NetCDF datasets using HoloViz",
    plot
)

app.servable()