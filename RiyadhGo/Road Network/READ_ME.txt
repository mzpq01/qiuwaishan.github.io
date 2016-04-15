The road network of Riyadh is modeled using a set of nodes (representing intersections) and a set of links (representing roads)

The shape files are using WGS84 coordinate system (EPSG:4326) and are properly aligned with the coordinates of the cell towers.

The original road network shape files were used with EMME modeling software so they contained some imaginary nodes and links that were needed for the model to work. 
We removed all of those nodes and links as well as the future links and nodes (which represent planned roads that have not been built yet) so the road network in this folder should reflect the actual layout of Riyadh.

The spreadsheet contains a description of the different road types along with their typical speed (in km/h) and capacity (in vehicles/h)