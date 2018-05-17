# Measuring the Gender Pay Gap with Blinder-Oaxaca Decompositions
###### (And comparing to existing measures)
---------

SUMMARY: A gender pay gap exists when one gender, either male or female, earn higher wages. A gender pay gap can then be measured in two ways -- either adjusted or unadjusted. The unadjusted gap is just the difference in average earned wages. The adjusted gap is the pay gap that remains when other factors, such as hours worked and roles taken on are accounted for. The adjusted gap attempts to measure if males and females get the same wage for the same work.

We attempt to take a look at the components of the gender pay gap for multiple countries, implementing a commonly used method for the problem, Blinder-Oaxaca Decompositions. There exist Stata and R packages for Oaxaca type decompositions, but no Python packages. This project coincides with our development of a Python package to recreate those projects.

--------------

Project Outline:

1. We walk through the calculation of our decompositions.
2. Talk about some of our data collection, standardization, and summary statistics.
3. We run the decompositions and compare the values between countries.
4. We plot a current measure of inequality against the unexplained proportion from our decomposition.

--------------

**Note: There is a lot more that can be done with the decompositions, and we do not go fully in-depth in our analysis of our results. For now, this is just an example implementation. More work can be done exploring the individual contributions from different variables, etc.**