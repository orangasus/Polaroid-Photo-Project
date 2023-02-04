# Photo to Polaroid Format

**Disclaimer: This is a study project. I built it in order to learn Python and get familiar with [Pillow Library](https://pillow.readthedocs.io/en/stable/ "Pillow library")**
<br />  
<br />
## Project Description
This Python script uses basic OOP and Pillow image processing to transform an ordinary image into its polaroid variant. 
<br />  
*Here is an example*
<p float="right">
  <img src="./Images/Back%20To%20Grime.jpg/" width="450" />
  <img src="./editedImages/Back%20To%20Grime_edit.jpg" width="450" /> 
</p>
<br />  

## Basically what the script does is:

* Decides which polaroid format will be the best for the picutre taking into account the ratio of the photo
* Crops the image
* Applies filters
* Applies polaroid border
* Tries to retrive the name of the picture and the date it was taken. Writes data on image
<br />  
<br />  

All fotos are converted to either *1080 x 1290* or *1620 x 1290* .jpg
