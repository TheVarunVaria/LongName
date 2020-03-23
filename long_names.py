def addLongNames(df,col):

    """Returns a DataFrame with additional LongName column

    Parameters:
        df : DataFrame of interest
        col: columnn whose long name is to be appended to the DataFrame

    Returns:
        df : DataFrame with new column inserted at (location of) column + 1 index
    """
    #Disability Type
    if(col == 'DisabilityType'):
        # Create the dictionary
        event_dictionary = {
            5 : 'Physical disability',
            6 : 'Developmental disability',
            7 : 'Chronic health condition'
        }

    #Project Type
    elif (col == 'ProjectType'):
        # Create the dictionary
        event_dictionary = {
            1  : 'Emergency Shelter',
            2  : 'Transitional Housing',
            3  : 'PH - Permanent Supportive Housing ',
            4  : 'Street Outreach',
            6  : 'Services Only',
            7  : 'Other',
            8  : 'Safe Haven',
            9  : 'PH – Housing Only',
            10 : 'PH – Housing with Services (no disability required for entry)',
            11 : 'Day Shelter',
            12 : 'Homelessness Prevention',
            13 : 'PH - Rapid Re-Housing',
            14 : 'Coordinated Entry'
        }

    #HousingType
    elif (col == 'HousingType'):
        # Create the dictionary
        event_dictionary = {
            1 : 'Site-based – single site',
            2 : 'Site-based – clustered / multiple sites' ,
            3 : 'Tenant-based - scattered site'
        }

    #HouseholdType
    elif (col == 'HouseholdType'):
        # Create the dictionary
        event_dictionary = {
            1 : 'Households without children',
            3 : 'Households with at least one adult and one child',
            4 : 'Households with only children'
        }

    #GeographyType
    elif (col == 'GeographyType'):
        # Create the dictionary
        event_dictionary = {
            1  : 'Urban',
            2  : 'Suburban',
            3  : 'Rural',
            99 : 'Unknown / data not collected'
        }

    #Ethnicity
    elif (col == 'Ethnicity'):
        # Create the dictionary
        event_dictionary = {
            0  : 'Non-Hispanic/Non-Latino',
            1  : 'Hispanic/Latino',
            8  : 'Client doesn’t know',
            9  : 'Client refused',
            99 : 'Data not collected'
        }

    #LengthOfStay
    elif (col == 'LengthOfStay'):
        # Create the dictionary
        event_dictionary = {
            2  : 'One week or more, but less than one month',
            3  : 'One month or more, but less than 90 days',
            4  : '90 days or more but less than one year',
            5  : 'One year or longer',
            8  : 'Client doesn’t know',
            9  : 'Client refused',
            10 : 'One night or less ',
            11 : 'Two to six nights',
            99 : 'Data not collected'
        }

    #MonthsHomelessPastThreeYears
    elif (col == 'MonthsHomelessPastThreeYears'):
        # Create the dictionary
        event_dictionary = {
            8   : 'Client doesn’t know',
            9   : 'Client refused',
            99  : 'Data not collected',
            101 : 1,
            102 : 2,
            103 : 3,
            104 : 4,
            105 : 5,
            106 : 6,
            107 : 7,
            108 : 8,
            109 : 9,
            110 : 10,
            111 : 11,
            112 : 12,
            113 : 'More than 12 months'
        }

    #Gender
    elif (col == 'Gender'):
        # Create the dictionary
        event_dictionary = {
            0  : 'Female',
            1  : 'Male',
            2  : 'Trans Female (MTF or Male to Female)',
            3  : 'Trans Male (FTM or Female to Male)',
            4  : 'Gender non-conforming (i.e. not exclusively male or female)',
            8  : 'Client doesn’t know',
            9  : 'Client refused',
            99 : 'Data not collected'
        }

    #TimesHomelessPastThreeYears
    elif (col == 'TimesHomelessPastThreeYears'):
        # Create the dictionary
        event_dictionary = {
            1  : 'One time',
            2  : 'Two times',
            3  : 'Three times',
            4  : 'Four or more times',
            8  : 'Client doesn’t know',
            9  : 'Client refused',
            99 : 'Data not collected'
        }

    #LivingSituation
    elif (col == 'LivingSituation' || col == 'Destination'):
        # Create the dictionary
        event_dictionary = {
            16 : 'Place not meant for habitation',
            1  : 'Emergency shelter',
            18 : 'Safe Haven',
            15 : 'Foster care home or foster care group home',
            6  : 'Hospital or other residential non-psychiatric medical facility',
            7  : 'Jail, prison or juvenile detention facility',
            25 : 'Long-term care facility or nursing home',
            4  : 'Psychiatric hospital or other psychiatric facility',
            5  : 'Substance abuse treatment facility or detox center',
            29 : 'Residential project or halfway house with no homeless criteria',
            14 : 'Hotel or motel paid for without emergency shelter voucher',
            2  : 'Transitional housing for homeless persons ',
            32 : 'Host Home (non-crisis)',
            13 : 'Staying or living with friends, temporary tenure',
            36 : 'Staying or living in a friend’s room, apartment or house',
            12 : 'Staying or living with family, temporary tenure',
            22 : 'Staying or living with family, permanent tenure',
            35 : 'Staying or living in a family member’s room, apartment or house',
            23 : 'Staying or living with friends, permanent tenure',
            26 : 'Moved from one HOPWA funded project to HOPWA PH',
            27 : 'Moved from one HOPWA funded project to HOPWA TH',
            28 : 'Rental by client, with GPD TIP housing subsidy',
            19 : 'Rental by client, with VASH housing subsidy',
            3  : 'Permanent housing (other than RRH) for formerly homeless persons',
            31 : 'Rental by client, with RRH or equivalent subsidy',
            33 : 'Rental by client, with HCV voucher (tenant or project based)',
            34 : 'Rental by client in a public housing unit',
            10 : 'Rental by client, no ongoing housing subsidy',
            20 : 'Rental by client, with other ongoing housing subsidy',
            21 : 'Owned by client, with ongoing housing subsidy',
            11 : 'Owned by client, no ongoing housing subsidy',
            30 : 'No exit interview completed',
            17 : 'Other',
            24 : 'Deceased',
            37 : 'Worker unable to determine',
            8  : 'Client doesn’t know',
            9  : 'Client refused',
            99 : 'Data not collected'
        }

    #If the column name is not present in the DataFrame, return the DataFrame
    else:
        return df

    #Get the index of the column
    idx = df.columns.get_loc(col)

    #Map the values for the new column
    newCol = df[col].map(event_dictionary)

    #Insert at the column + 1 place
    df.insert(loc=idx + 1, column=col+'Text', value=newCol)

    return df
