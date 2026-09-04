# Investigating-the-Diffraction-Limit-of-a-Telescope
Here I will be using Python to numerically calculate the Bessel functions $J_m(x)$ using the equation

$$J_m(x) = \frac{1}{\pi} \int_0^{\pi} \cos(m\theta - x\sin\theta) \, d\theta$$

I will use the trapezium rule to approximate it. After importing the numpy and matplotlib library, I added the Bessel function. I chose N as 10000 in order to reduce numerical error, give a good approximation to the integral and give smoother curves.
Next, I implemented the trapezium rule for the integral. I halved the first and last terms, and summed the rest of the terms in a loop. 
I then multiplied the results by the step size h and divided by $pi$ to complete it.
I then evaluated and plotted the functions $J_0(x)$, $J_1(x)$ and $J_2(x)$, using a range of x values to evaluate the functions over. I used lists to store the values for each Bessel function.
