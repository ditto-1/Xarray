# Climate Data Analysis Dashboard
A reactive geospatial tool for visualizing datasets using the HoloViz stack.

## Tech Stack
* **Data Processing:** `xarray`, `Dask`, `NumPy`, `Pandas`
* **Visualization:** `hvPlot`, `GeoViews`, `HoloViews`
* **App Framework:** `Panel`
* **Data Engines** `Pooch`, `NetCDF4`

## Phase 1: The Functional Prototype (Practice)
* **Objective:** Established a reactive link between **Panel widgets** (used to select variables such as temperature and precipitation) and `xarray` data structures.
* **Key Logic:** Used a synthetic dataset via `da.random` with specific scaling factors (**\*40** for temperature and **\*5** for precipitation) to simulate realistic physical ranges (e.g., $0$ to $40°C$) and ensure colormap alignment with data values.
* **Dynamic Aesthetics:** Assigned distinct colormaps to each variable. A `getmap` function detects the user's variable selection and injects the appropriate aesthetic (**'hot'** for temperature and **'Blues'** for precipitation).
* **Interactive Slicing:** When a specific time is selected, `ds.interactive` is used to update the map instantly according to the selected **time slice**.
* **Chunking:** Implemented **Dask chunking** in the form `chunks=(5, 50, 50)`. This divides the data into multiple slices, each containing 5 time values, allowing the dashboard to scale to **terabyte-sized** datasets by only loading required "slices" into memory.

## Phase 2: The Production-Ready Dashboard
This phase utilizes a built-in NASA dataset: `xr.tutorial.open_dataset('air_temperature')`, which focuses specifically on North America.

* **Automated Retrieval:** Used the `Pooch` library to handle the fetching and caching of the NASA data.
* **Performance Optimization:** As previously mentioned, **Dask chunking** is applied here to maintain high performance with real-world data.
* **Unit Conversion:** Temperature is originally stored in **Kelvin**, which is converted to **Celsius** to make the output more user-friendly.
* **Scientific Visualization:** A **'coolwarm'** colormap is used for air temperature. This provides a neutral center (grey/white), where below-average temperatures appear blue and above-average temperatures appear red.
* **Boundary Enforcement (The Layer Stack):** Used an overlay strategy (`Data * Coastline * Borders`) to ensure geographic boundaries remain visible. This allows the user to easily identify temperatures across different countries or states.
* **Lazy Loading:** Optimized for memory efficiency by only loading the required temporal slices into the browser via **Dask**.

## Demo Screenshots 
1. Practice1 (Temperature)
   <p align="center">
  <img src="https://github.com/user-attachments/assets/55ce0f91-9f48-48c3-b004-fdf7377303f5" width="500">
   </p>
3. Practice1 (Precipitation)
   <p align="left">
  <img src="https://github.com/user-attachments/assets/ef941b33-8b12-476e-bb07-487ce7718a57" width="500">
   </p>

4. Climate Dashboard On NASA Dataset
   <p align="center">
  <img src="https://github.com/user-attachments/assets/14354c01-a139-43cf-aa8e-acbe03c20c12" width="500">
   </p>

## How to Run
1. **Install Dependencies:**
   Ensure you have required libraries installed:
   ```bash
   pip install xarray panel hvplot geoviews pooch netcdf4 dask
2. **Run the dashboard**
   Navigate to the project folder and launch the app:
   ```bash
   python -m panel serve Climate_Dashboard.py --show
