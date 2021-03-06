from image import ImageWithWCS
import image_collection as tff
import numpy as np
from os import path

def shift_images(files, source_dir, output_file='_shifted'):
    """Align images based on astrometry."""

    ref = files[0] # TODO: make reference image an input
    ref_im = ImageWithWCS(path.join(source_dir,ref))
    ref_pix = np.int32(np.array(ref_im.data.shape)/2)
    ref_ra_dec = ref_im.wcs_pix2sky(ref_pix)
    for fil in files[1:]:
        img = ImageWithWCS(path.join(source_dir,fil))
        ra_dec_pix = img.wcs_sky2pix(ref_ra_dec)
        shift = ref_pix - np.int32(ra_dec_pix)
        print shift
        img.shift(shift, in_place=True)
        base, ext = path.splitext(fil)
        img.save(path.join(source_dir,base+output_file+ext))
        
        

    



