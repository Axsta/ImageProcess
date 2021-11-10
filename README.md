# Detection of Pothole using Image Processing Techniques

&emsp; India is one of the most populous country, roads are the main mode of transportation in this developing country. But due to the heavy use of roads, there is a high amount of wear and tear carried out. Since these roads cannot sustain itself for a long time, a timely maintenance is expected to be carried out in order to prevent the formation of potholes. The manner in which a pothole is formed depends on the type of bituminous pavement surfacing. The heavy traffic on the road is the primary reasons for the fatiguing of the road surface, resulting in the formation of the crack. These depressions collect water and allow the water to mix with the asphalt. When vehicles drive through such holes the water is expelled along with some of the asphalt, and this slowly creates a cavity underneath the crack. If a regular road maintenance is neglected, the road surface will eventually collapse into the cavity, resulting in a visibly huge pothole over the surface. In order to repair these roads in a timely manner, it is necessary that the entity knows which area is affected by the pothole or decaying road section is located and an automated process could assist with this.<br></br>

&emsp; This approach includes the use of a computer vision based system. In this system, a two-dimensional image of roads is used. The digital images are captured by the camera and are processed to capture the information related to road anomalies. In a 2D image-based approach, the system extracts the texture measure based on the histogram as the features of the image region, and the nonlinear support vector machine was built up to identify a potential region is a pothole or not. 
 <br></br>

Following is actual picture captured of a pothole :
 <br></br>
 <p align = "center">
<img src=https://github.com/Axsta/ImageProcess/blob/master/pothole.png />
 </p>
 <br></br>
 
Methodology of the model : 
* The model converts the RGB image to gray scale
* Reduce noises by using Gaussian filter
* Detect edge using the Canny Edge detection technique
* Refine edge detection using Erosion morphology

<br></br>
  <p align = "center">
<img src="https://github.com/Axsta/ImageProcess/blob/master/edge.png">
 </p>
