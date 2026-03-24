import xarray as xr
import numpy as np
import pandas as pd
import dask.array as da
import hvplot.xarray
import hvplot 
import panel as pn
import geoviews as gv
import geoviews.feature as gf

times = pd.date_range("2026-03-01", periods=30)
lats = np.linspace(-90, 90, 50)
lons = np.linspace(-180, 180, 50)

temp_data = da.random.random((30, 50, 50), chunks=(5, 50, 50))*40
prec_data = da.random.random((30, 50, 50), chunks=(5, 50, 50))*5

ds = xr.Dataset(
    {"temperature": (("time", "lat", "lon"), temp_data),
     'precipitation':(('time', 'lat', 'lon'), prec_data)},
    coords={"time": times, "lat": lats, "lon": lons}
)

time_options = {t.strftime('%Y-%m-%d'): t for t in times}
time_select = pn.widgets.Select(
    name='Select times', 
    options=time_options
)

variable_switch = pn.widgets.RadioButtonGroup(
    name='Select variable',
    options=['temperature', 'precipitation'],
    button_type='success'
)

color_map = {
    'temperature':'hot',
    'precipitation':'Blues'
}

def getmap(selection):
    return color_map.get(selection, 'viridis')

reactive_map = pn.bind(getmap, variable_switch)

interactive_map = ds.interactive()[variable_switch].sel(time = time_select)
plot = interactive_map.hvplot.quadmesh(
    x='lon', y='lat', colorbar=True,
    cmap = reactive_map,
    geo=True,
    alpha=0.5,
    coastline=True,
    features=['borders']
)

pn.serve(plot)