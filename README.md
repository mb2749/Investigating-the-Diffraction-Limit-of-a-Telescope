# Investigating-the-Diffraction-Limit-of-a-Telescope
Here I will be using Python to numerically calculate the Bessel functions $J_m(x)$ using the equation

$$J_m(x) = \frac{1}{\pi} \int_0^{\pi} \cos(m\theta - x\sin\theta) \ d\theta.$$

I will use the trapezium rule to approximate it. After importing the numpy and matplotlib library, I added the Bessel function. I chose N as 10000 in order to reduce numerical error, give a good approximation to the integral and give smoother curves.
Next, I implemented the trapezium rule for the integral. I halved the first and last terms, and summed the rest of the terms in a loop. 
I then multiplied the results by the step size h and divided by $pi$ to complete it.
I then evaluated and plotted the functions $J_0(x)$, $J_1(x)$ and $J_2(x)$, using a range of x values to evaluate the functions over. I used lists to store the values for each Bessel function.
I then plotted the three functions on the same graph to make them easier to compare (can be seen in oscillations.png).
The plot shows the oscillations with decreasing amplitudes, which is consistent with the expected behaviour of Bessel functions. To check that the numerical integration was working correctly, I compared some known values, for example $J_0(0) = 1$, which was reproduced by the code.
The general shape of the graphs (oscillations with decreasing amplitude) also matches the expected behaviour of Bessel functions.

I calculated the diffraction pattern using the intensity function

$$I(r) = \left( \frac{2J_1(x)}{x} \right)^2, \qquad x = \frac{2\pi}{\lambda} \, a \, \frac{r}{R}.$$

After importing the lumpy and matplotlib libraries, I chose a suitable wavelength to define as lambda. I decided on 5.5 x 10^-7 m (550nm) as this is almost central on the visible light spectrum and is the wavelength of green light, however any wavelength in the visible range could have been used, but it would affect the size of the diffraction pattern, which is inversely proportional to $lambda$. The focal ratio was given as

$$\frac{R}{2a} = 10,$$

which I used to define R. I chose a value of 1 x 10^-3 for the aperture radius as this is a typical small aperture size, which I then used to calculate the value for R. I defined the range of r values, making sure it covered the range of ±25$\mu m$. 
I then calculated the intensity using a loop, so that for each value of r, the corresponding value of x was found. Next, I evaluated the intensity expression, using a conditional statement to deal with what would happen if x = 0, which would mean that the expression would be undefined due to division by zero. I used the limiting value I(0) for this.
Finally, I plotted the diffraction pattern, converting the radial distance into micrometres. This can be seen in Bessel_function.png.
This plot shows the central maximum, where the intensity is highest, to be at r=0. This is followed by a series of smaller peaks corresponding to diffraction rings. 
The first minimum in the diffraction pattern is related to the Airy disk radius, which sets the resolution limit of the system. This shows that the ability of the telescope to resolve detail is fundamentally limited by diffraction.
The intensity decreases as the distance from the centre increases, showing that most of the light is concentrated in the central region. This behaviour is consistent with the diffraction pattern produced by a circular aperture.
