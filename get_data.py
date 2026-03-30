import xarray as xr

ds = xr.tutorial.open_dataset("air_temperature")
ds.to_netcdf("air_temperature.nc")

print("Success! 'air_temperature.nc' is now in your folder.")