# Photo to Polaroid Format
<br />  

## Project Description
This Python script uses basic OOP and Pillow image processing to transform an ordinary image into its polaroid variant. 
<br />  

*Here is an example*
<p float="right">
  <kbd><img src="./Images/Back%20To%20Grime.jpg/" width="400" /></kbd>
  <kbd><img src="./editedImages/Back%20To%20Grime_edit.jpg" width="400" /></kbd> 
</p>
<br />  

## Basically what the script does is:

* Decides which polaroid format will be the best for the picutre taking into account the ratio of the photo
* Crops the image
* Applies filters
* Applies polaroid border
* Tries to retrive the name of the picture and the date it was taken. Writes data on image
<br />  

 All fotos are converted to either *1080 x 1290* or *1620 x 1290* .jpg
