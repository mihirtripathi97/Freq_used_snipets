#Python

import os
from astropy.io import fits
from astropy.wcs import WCS
import astropy.units as u
import matplotlib.pyplot as plt

file = 'AS 205_continuum.fits'
name = file.split('_')[0] # Name of source
file_path = os.path.join(name )
        
# Get header and data from the fits file 
hdul = fits.open(file)
hdul.info()
header = hdul[0].header
     
# Define wcs object from fits header
wcs = WCS(hdul[0].header, naxis=[1,2], fix = False) 
# For FITS files of DSHARP objects --- axis 1,2 has image data  
# Extract image data from fits file,  and assign units
data = u.Quantity(hdul[0].data.squeeze(), unit = hdul[0].header['BUNIT'])
hdul.close()


plt.subplot(projection = wcs)
plt.imshow(data, origin = 'lower', cmap = 'hot')   
plt.xlim(700,2700)
plt.ylim(700,2700)
plt.colorbar()
plt.grid()
plt.savefig(file_path + '.png', dpi = 600)
plt.show()
plt.close()
