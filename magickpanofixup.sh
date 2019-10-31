# Script to resample and append ACRC tower camera images (post camera upgrade); by Telayna, October 2019

convert /products/htdocs/media/cam/acrc_pano/misc/ACRC_Pano_1.jpg -sample 2560x1890 /products/htdocs/media/cam/acrc_pano/misc/pic1.jpg
convert /products/htdocs/media/cam/acrc_pano/misc/ACRC_Pano_2.jpg -sample 2480x1880 /products/htdocs/media/cam/acrc_pano/misc/pic2.jpg
convert /products/htdocs/media/cam/acrc_pano/misc/ACRC_Pano_3.jpg -sample 2490x1920 /products/htdocs/media/cam/acrc_pano/misc/pic3.jpg
convert /products/htdocs/media/cam/acrc_pano/misc/pic1.jpg /products/htdocs/media/cam/acrc_pano/misc/pic2.jpg /products/htdocs/media/cam/acrc_pano/misc/pic3.jpg +smush -8 /products/htdocs/media/cam/acrc_pano/misc/pano.jpg
convert /products/htdocs/media/cam/acrc_pano/misc/pano.jpg -crop 7600x1790 /products/htdocs/media/cam/acrc_pano/misc/cropped.jpg
mv /products/htdocs/media/cam/acrc_pano/misc/cropped-0.jpg /products/htdocs/media/cam/acrc_pano/ACRC_Pano_$(TZ=US/Alaska date +%Y%m%d-%H%M).jpg

