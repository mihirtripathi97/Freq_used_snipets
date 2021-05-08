def angle_tweak(file,dsfile,dfrow):
    
    # Function to get azzimuthally averaged radial brightness profile of protoplenetory disk image (FITS)
    
    # file - FITS image
    # dsfile - refrence file with radial brightness profile (DSHARP) Remove after perfacting
    # dfrow - data row - containing inclination, position angle and center coordinates (RA DEC and pixel) of disk
    
    
    name = dsfile.split('.')[0] # Name of source
    
    # Get header and data from the fits file 
    hdul = fits.open(file)
    hdul.info()
    header = hdul[0].header
    
    obstm = header['DATE-OBS']
    print(obstm)
    
    # Define wcs object from fits header
    wcs = WCS(hdul[0].header, naxis=[1,2], fix = False) 
    # for FITS files of DSHARP objects --- axis 1,2 has image data 
    
    # Extract image data from fits file, assign units
    #data = u.Quantity(hdul[0].data.squeeze(), unit = hdul[0].header['BUNIT'])
    hdul.close()
     
    
    # Grab distance, inclination, PA and coordinates from data frame row
    
    dist = dfrow.loc['Distance']
    incl = dfrow.loc['Incl.']
    PA = dfrow.loc['PA']
    J2_RA = dfrow.loc['RA']       #J2000 icrs   , unit - deg
    J2_DEC = dfrow.loc['DEC']
    G_RA = dfrow.loc['GAIA RA']    # J2016 GAIA edr3, , unit - deg
    G_DEC = dfrow.loc['GAIA DEC']  ## J2016 GAIA edr3, , unit - deg
    G_RA_pm = dfrow.loc['GAIA_RA_PM']
    G_DEC_pm = dfrow.loc['GAIA_DEC_PM']

    RAp = dfrow.loc['Photo_RA_pix']          # Photopeak pixel value
    DECp = dfrow.loc['Photo_DEC_pix']
       
    
    # define position objects 
    #j2pos = SkyCoord(ra = J2_RA*u.deg, dec = J2_DEC*u.deg, frame = ICRS, equinox = 'J2016',distance = dist*u.pc)
    gaiapos = SkyCoord(ra = G_RA*u.deg, dec = G_DEC*u.deg, frame = ICRS, obstime = 'J2016',distance = 100*u.pc)  
    print('original GAIA position : ',gaiapos) 
    #from pixels of imfit peak  -- 2D gaussian fit peak    
    tdgpos = pixel_to_skycoord(round(RAp,9), round(DECp,9), wcs,  mode = 'all')
    
    gaiapos = gaiapos.transform_to(tdgpos)
    
   
          
   # print('J2000 position: ',j2pos) 
    print('GAIA position after transforming to photo frame : ',gaiapos)  
    print('photopeak position : ',tdgpos)
    

    ra_off = tdgpos.ra - gaiapos.ra
    dec_off = tdgpos.dec - gaiapos.dec
    
    sep = tdgpos.separation(gaiapos)
    print(sep)
    
    
    
    print(dist_2)
    
   
    
    
    tdgpos = tdgpos.transform_to(ICRS)
    gaiapos = gaiapos.transform_to(ICRS)
    
    sep = tdgpos.separation(gaiapos)
    print(sep)
    
    ra_off = tdgpos.ra - gaiapos.ra
    dec_off = tdgpos.dec - gaiapos.dec
    
   
    return



df = pd.read_csv('Disk_data.csv', sep= '\t', index_col = 0, header = 'infer', dialect= 'excel-tab', float_precision ='round_trip' )

#print(df)


imfile = 'HD 163296_continuum.fits'
obj_name = 'HD 163296'
dsfile = 'HD 163296.profile.txt'

angle_tweak(imfile,dsfile,df.loc[obj_name])

