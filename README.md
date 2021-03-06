# LongName
This module can be used to convert codes to long names from the HMIS dataset

### What is HMIS?
HMIS (Homeless Management Information System) is software application that records all housing services provided to individuals and families seeking federally funded homelessness assistance. HMIS stores client-level data and data on the provision of housing and services to homeless individuals and families and persons at risk of homelessness and must comply with the U.S. Department of Housing and Urban Development (HUD) data collection, management, and reporting standards.

### What does this module do?
HMIS Datasets often contain a lot of column that are encoded using identifiers. To understand the meaning of a particular value, one has to look it up in the HMIS data dictionary.
For example, Enrollment.csv contains a column called 'Length of Stay' which takes nine possible values as follows:

<img src="IMG1.png" width="50%" />



### addLongName function
With multiple columns being encoded with some of them taking 35+ possible values, it is difficult to remember what each value represents.`addLongName` function will insert a column looking up its value from the data dictionary and insert it next to the column you passed.
Returns a DataFrame with additional LongName column

#### Parameters:
<li> df : DataFrame of interest</li> 

<li> col: columnn whose long name is to be appended to the DataFrame</li> 

#### Returns:
<li> df : DataFrame with new column inserted at (location of) column + 1 index</li> 
  

### How to invoke the function?

You can invoke the function by importing the file and calling the function as showing in the image below

<img src="IMG3.png" width="50%" />


### Currently the module supports following columns - 
<li>LivingSituation</li>
<li>Destination</li>
<li>DisabilityType</li>
<li>ProjectType</li>
<li>HousingType</li>
<li>HouseholdType</li>
<li>GeographyType</li>
<li>Ethnicity</li>
<li>Gender</li>
<li>LengthOfStay</li>
<li>TimesHomelessPastThreeYears</li>
<li>MonthsHomelessPastThreeYears</li>
