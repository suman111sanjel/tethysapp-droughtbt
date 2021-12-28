import netCDF4
import numpy
import datetime
# from multiprocessing import Pool
start=datetime.datetime.now()
ncFullPath = '/home/suman/192.168.11.242 user Suman/Qout_era5_t640_24hr_19790101to20191231.nc'
nc_fid = netCDF4.Dataset(ncFullPath, 'r')
lis_var = nc_fid.variables
Comid=5084007
rividAll = nc_fid.variables['rivid'][:]
time = nc_fid.variables['time'][:]
field=nc_fid.variables['Qout'][:]
end=datetime.datetime.now()
print(end-start)
getDifference = numpy.abs(rividAll - Comid)
absRiverId = numpy.abs(getDifference - Comid)
comid_idx = (absRiverId.argmin())
listNew=[]
timeNew=numpy.array_split(time,40)
for timestep, v in enumerate(time):
    nc_arr = field[timestep,comid_idx]
    listNew.append(nc_arr)
# print(listNew)
nc_fid.close()
