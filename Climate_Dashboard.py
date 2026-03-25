import numpy as np
import pandas as pd
import xarray as xr
import dask.array as da
import panel as pn
import hvplot
import hvplot.xarray
import geoviews as gv
import geoviews.feature as gf

ds = xr.tutorial.open_dataset('air_temperature')
ds['air'] = ds['air']-273.15

variable_Switch = pn.widgets.RadioButtonGroup(
    name='Select variable',
    options={'Air temperature':'air'},
    button_type='success'
)
times = ds.time.values
time_options = {pd.to_datetime(t).strftime('%Y-%m-%d') :t for t in times}
time_select = pn.widgets.Select(
    name='select time',
    options=time_options
)

color_map={
    'air':'coolwarm'
}

def getcmap(selection):
    return color_map.get(selection, 'viridis')

reactive_map = pn.bind(getcmap, variable_Switch)
interactive_map = ds.interactive()[variable_Switch].sel(time=time_select)
plot = interactive_map.hvplot.quadmesh(
    x='lon', y='lat', colorbar=True,
    cmap = reactive_map,
    geo=True,
    coastline=True,
    features=['borders'],
    title='Real world atmospheric data'
)
pn.serve(plot)
