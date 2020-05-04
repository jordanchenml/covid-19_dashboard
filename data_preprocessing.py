import pandas as pd
import numpy as np


def rename_coutries(df):
    # Rename countries with duplicate naming conventions
    df['Country/Region'].replace('Mainland China', 'China', inplace=True)
    df['Country/Region'].replace('Hong Kong SAR', 'Hong Kong', inplace=True)
    df['Country/Region'].replace(' Azerbaijan', 'Azerbaijan', inplace=True)
    df['Country/Region'].replace('Holy See', 'Vatican City', inplace=True)
    df['Country/Region'].replace('Iran (Islamic Republic of)',
                                 'Iran', inplace=True)
    df['Country/Region'].replace('Taiwan*', 'Taiwan', inplace=True)
    df['Country/Region'].replace('Korea, South', 'South Korea', inplace=True)
    df['Country/Region'].replace('Viet Nam', 'Vietnam', inplace=True)
    df['Country/Region'].replace('Macao SAR', 'Macau', inplace=True)
    df['Country/Region'].replace('Russian Federation', 'Russia', inplace=True)
    df['Country/Region'].replace('Republic of Moldova',
                                 'Moldova', inplace=True)
    df['Country/Region'].replace('Czechia', 'Czech Republic', inplace=True)
    # df['Country/Region'].replace('Congo (Kinshasa)', 'Congo', inplace=True)
    df['Country/Region'].replace('Northern Ireland',
                                 'United Kingdom', inplace=True)
    df['Country/Region'].replace('Republic of Korea',
                                 'South Korea', inplace=True)
    # df['Country/Region'].replace('Congo (Brazzaville)', 'Congo', inplace=True)
    df['Country/Region'].replace('Taipei and environs', 'Taiwan', inplace=True)
    df['Country/Region'].replace('Others', 'Cruise Ship', inplace=True)
    df['Province/State'].replace('Cruise Ship',
                                 'Diamond Princess cruise ship', inplace=True)
    df['Province/State'].replace('From Diamond Princess',
                                 'Diamond Princess cruise ship', inplace=True)

    # Replace old reporting standards
    df['Province/State'].replace('Chicago', 'Illinois', inplace=True)
    df['Province/State'].replace('Chicago, IL', 'Illinois', inplace=True)
    df['Province/State'].replace('Cook County, IL', 'Illinois', inplace=True)
    df['Province/State'].replace('Boston, MA', 'Massachusetts', inplace=True)
    df['Province/State'].replace(' Norfolk County, MA',
                                 'Massachusetts', inplace=True)
    df['Province/State'].replace('Suffolk County, MA',
                                 'Massachusetts', inplace=True)
    df['Province/State'].replace('Middlesex County, MA',
                                 'Massachusetts', inplace=True)
    df['Province/State'].replace('Norwell County, MA',
                                 'Massachusetts', inplace=True)
    df['Province/State'].replace('Plymouth County, MA',
                                 'Massachusetts', inplace=True)
    df['Province/State'].replace('Norfolk County, MA',
                                 'Massachusetts', inplace=True)
    df['Province/State'].replace('Berkshire County, MA',
                                 'Massachusetts', inplace=True)
    df['Province/State'].replace('Unknown Location, MA',
                                 'Massachusetts', inplace=True)
    df['Province/State'].replace('Los Angeles, CA', 'California', inplace=True)
    df['Province/State'].replace('Orange, CA', 'California', inplace=True)
    df['Province/State'].replace('Santa Clara, CA', 'California', inplace=True)
    df['Province/State'].replace('San Benito, CA', 'California', inplace=True)
    df['Province/State'].replace('Humboldt County, CA',
                                 'California', inplace=True)
    df['Province/State'].replace('Sacramento County, CA',
                                 'California', inplace=True)
    df['Province/State'].replace('Travis, CA (From Diamond Princess)',
                                 'California', inplace=True)
    df['Province/State'].replace('Placer County, CA',
                                 'California', inplace=True)
    df['Province/State'].replace('San Mateo, CA', 'California', inplace=True)
    df['Province/State'].replace('Sonoma County, CA',
                                 'California', inplace=True)
    df['Province/State'].replace('Berkeley, CA', 'California', inplace=True)
    df['Province/State'].replace('Orange County, CA',
                                 'California', inplace=True)
    df['Province/State'].replace('Contra Costa County, CA',
                                 'California', inplace=True)
    df['Province/State'].replace('San Francisco County, CA',
                                 'California', inplace=True)
    df['Province/State'].replace('Yolo County, CA', 'California', inplace=True)
    df['Province/State'].replace('Santa Clara County, CA',
                                 'California', inplace=True)
    df['Province/State'].replace('San Diego County, CA',
                                 'California', inplace=True)
    df['Province/State'].replace('Travis, CA', 'California', inplace=True)
    df['Province/State'].replace('Alameda County, CA',
                                 'California', inplace=True)
    df['Province/State'].replace('Madera County, CA',
                                 'California', inplace=True)
    df['Province/State'].replace('Santa Cruz County, CA',
                                 'California', inplace=True)
    df['Province/State'].replace('Fresno County, CA',
                                 'California', inplace=True)
    df['Province/State'].replace('Riverside County, CA',
                                 'California', inplace=True)
    df['Province/State'].replace('Shasta County, CA',
                                 'California', inplace=True)
    df['Province/State'].replace('Seattle, WA', 'Washington', inplace=True)
    df['Province/State'].replace('Snohomish County, WA',
                                 'Washington', inplace=True)
    df['Province/State'].replace('King County, WA', 'Washington', inplace=True)
    df['Province/State'].replace('Unassigned Location, WA',
                                 'Washington', inplace=True)
    df['Province/State'].replace('Clark County, WA',
                                 'Washington', inplace=True)
    df['Province/State'].replace('Jefferson County, WA',
                                 'Washington', inplace=True)
    df['Province/State'].replace('Pierce County, WA',
                                 'Washington', inplace=True)
    df['Province/State'].replace('Kittitas County, WA',
                                 'Washington', inplace=True)
    df['Province/State'].replace('Grant County, WA',
                                 'Washington', inplace=True)
    df['Province/State'].replace('Spokane County, WA',
                                 'Washington', inplace=True)
    df['Province/State'].replace('Tempe, AZ', 'Arizona', inplace=True)
    df['Province/State'].replace('Maricopa County, AZ',
                                 'Arizona', inplace=True)
    df['Province/State'].replace('Pinal County, AZ', 'Arizona', inplace=True)
    df['Province/State'].replace('Madison, WI', 'Wisconsin', inplace=True)
    df['Province/State'].replace('San Antonio, TX', 'Texas', inplace=True)
    df['Province/State'].replace('Lackland, TX', 'Texas', inplace=True)
    df['Province/State'].replace('Lackland, TX (From Diamond Princess)',
                                 'Texas', inplace=True)
    df['Province/State'].replace('Harris County, TX', 'Texas', inplace=True)
    df['Province/State'].replace('Fort Bend County, TX', 'Texas', inplace=True)
    df['Province/State'].replace('Montgomery County, TX',
                                 'Texas', inplace=True)
    df['Province/State'].replace('Collin County, TX', 'Texas', inplace=True)
    df['Province/State'].replace('Ashland, NE', 'Nebraska', inplace=True)
    df['Province/State'].replace('Omaha, NE (From Diamond Princess)',
                                 'Nebraska', inplace=True)
    df['Province/State'].replace('Douglas County, NE',
                                 'Nebraska', inplace=True)
    df['Province/State'].replace('Portland, OR', 'Oregon', inplace=True)
    df['Province/State'].replace('Umatilla, OR', 'Oregon', inplace=True)
    df['Province/State'].replace('Klamath County, OR', 'Oregon', inplace=True)
    df['Province/State'].replace('Douglas County, OR', 'Oregon', inplace=True)
    df['Province/State'].replace('Marion County, OR', 'Oregon', inplace=True)
    df['Province/State'].replace('Jackson County, OR ', 'Oregon', inplace=True)
    df['Province/State'].replace('Washington County, OR',
                                 'Oregon', inplace=True)
    df['Province/State'].replace('Providence, RI',
                                 'Rhode Island', inplace=True)
    df['Province/State'].replace('Providence County, RI',
                                 'Rhode Island', inplace=True)
    df['Province/State'].replace('Grafton County, NH',
                                 'New Hampshire', inplace=True)
    df['Province/State'].replace('Rockingham County, NH',
                                 'New Hampshire', inplace=True)
    df['Province/State'].replace('Hillsborough, FL', 'Florida', inplace=True)
    df['Province/State'].replace('Sarasota, FL', 'Florida', inplace=True)
    df['Province/State'].replace('Santa Rosa County, FL',
                                 'Florida', inplace=True)
    df['Province/State'].replace('Broward County, FL', 'Florida', inplace=True)
    df['Province/State'].replace('Lee County, FL', 'Florida', inplace=True)
    df['Province/State'].replace('Volusia County, FL', 'Florida', inplace=True)
    df['Province/State'].replace('Manatee County, FL', 'Florida', inplace=True)
    df['Province/State'].replace('Okaloosa County, FL',
                                 'Florida', inplace=True)
    df['Province/State'].replace('Charlotte County, FL',
                                 'Florida', inplace=True)
    df['Province/State'].replace('New York City, NY', 'New York', inplace=True)
    df['Province/State'].replace('Westchester County, NY',
                                 'New York', inplace=True)
    df['Province/State'].replace('Queens County, NY', 'New York', inplace=True)
    df['Province/State'].replace('New York County, NY',
                                 'New York', inplace=True)
    df['Province/State'].replace('Nassau, NY', 'New York', inplace=True)
    df['Province/State'].replace('Nassau County, NY', 'New York', inplace=True)
    df['Province/State'].replace('Rockland County, NY',
                                 'New York', inplace=True)
    df['Province/State'].replace('Saratoga County, NY',
                                 'New York', inplace=True)
    df['Province/State'].replace('Suffolk County, NY',
                                 'New York', inplace=True)
    df['Province/State'].replace('Ulster County, NY', 'New York', inplace=True)
    df['Province/State'].replace('Fulton County, GA', 'Georgia', inplace=True)
    df['Province/State'].replace('Floyd County, GA', 'Georgia', inplace=True)
    df['Province/State'].replace('Polk County, GA', 'Georgia', inplace=True)
    df['Province/State'].replace('Cherokee County, GA',
                                 'Georgia', inplace=True)
    df['Province/State'].replace('Cobb County, GA', 'Georgia', inplace=True)
    df['Province/State'].replace('Wake County, NC',
                                 'North Carolina', inplace=True)
    df['Province/State'].replace('Chatham County, NC',
                                 'North Carolina', inplace=True)
    df['Province/State'].replace('Bergen County, NJ',
                                 'New Jersey', inplace=True)
    df['Province/State'].replace('Hudson County, NJ',
                                 'New Jersey', inplace=True)
    df['Province/State'].replace('Clark County, NV', 'Nevada', inplace=True)
    df['Province/State'].replace('Washoe County, NV', 'Nevada', inplace=True)
    df['Province/State'].replace('Williamson County, TN',
                                 'Tennessee', inplace=True)
    df['Province/State'].replace('Davidson County, TN',
                                 'Tennessee', inplace=True)
    df['Province/State'].replace('Shelby County, TN',
                                 'Tennessee', inplace=True)
    df['Province/State'].replace('Montgomery County, MD',
                                 'Maryland', inplace=True)
    df['Province/State'].replace('Harford County, MD',
                                 'Maryland', inplace=True)
    df['Province/State'].replace('Denver County, CO', 'Colorado', inplace=True)
    df['Province/State'].replace('Summit County, CO', 'Colorado', inplace=True)
    df['Province/State'].replace('Douglas County, CO',
                                 'Colorado', inplace=True)
    df['Province/State'].replace('El Paso County, CO',
                                 'Colorado', inplace=True)
    df['Province/State'].replace('Delaware County, PA',
                                 'Pennsylvania', inplace=True)
    df['Province/State'].replace('Wayne County, PA',
                                 'Pennsylvania', inplace=True)
    df['Province/State'].replace('Montgomery County, PA',
                                 'Pennsylvania', inplace=True)
    df['Province/State'].replace('Fayette County, KY',
                                 'Kentucky', inplace=True)
    df['Province/State'].replace('Jefferson County, KY',
                                 'Kentucky', inplace=True)
    df['Province/State'].replace('Harrison County, KY',
                                 'Kentucky', inplace=True)
    df['Province/State'].replace('Marion County, IN', 'Indiana', inplace=True)
    df['Province/State'].replace('Hendricks County, IN',
                                 'Indiana', inplace=True)
    df['Province/State'].replace('Ramsey County, MN',
                                 'Minnesota', inplace=True)
    df['Province/State'].replace('Carver County, MN',
                                 'Minnesota', inplace=True)
    df['Province/State'].replace('Fairfield County, CT',
                                 'Connecticut', inplace=True)
    df['Province/State'].replace('Charleston County, SC',
                                 'South Carolina', inplace=True)
    df['Province/State'].replace('Spartanburg County, SC',
                                 'South Carolina', inplace=True)
    df['Province/State'].replace('Kershaw County, SC',
                                 'South Carolina', inplace=True)
    df['Province/State'].replace('Davis County, UT', 'Utah', inplace=True)
    df['Province/State'].replace('Honolulu County, HI', 'Hawaii', inplace=True)
    df['Province/State'].replace('Tulsa County, OK', 'Oklahoma', inplace=True)
    df['Province/State'].replace('Fairfax County, VA',
                                 'Virginia', inplace=True)
    df['Province/State'].replace('St. Louis County, MO',
                                 'Missouri', inplace=True)
    df['Province/State'].replace('Unassigned Location, VT',
                                 'Vermont', inplace=True)
    df['Province/State'].replace('Bennington County, VT',
                                 'Vermont', inplace=True)
    df['Province/State'].replace('Johnson County, IA', 'Iowa', inplace=True)
    df['Province/State'].replace('Jefferson Parish, LA',
                                 'Louisiana', inplace=True)
    df['Province/State'].replace('Johnson County, KS', 'Kansas', inplace=True)
    df['Province/State'].replace('Washington, D.C.',
                                 'District of Columbia', inplace=True)

    # # Re-order the columns for readability
    # df = df[['date',
    #         'Country/Region',
    #         'Province/State',
    #         'Confirmed',
    #         'Deaths',
    #         'Recovered',
    #         'Latitude',
    #         'Longitude']]

    # # Fill missing values as 0; create Active cases column
    # df['Confirmed'] = df['Confirmed'].fillna(0).astype(int)
    # df['Deaths'] = df['Deaths'].fillna(0).astype(int)
    # df['Recovered'] = df['Recovered'].fillna(0).astype(int)
    # df['Active'] = df['Confirmed'] - df['Deaths'] - df['Recovered']

    # # Replace missing values for latitude and longitude
    # df['Latitude'] = df['Latitude'].fillna(df.groupby('Province/State')['Latitude'].transform('mean'))
    # df['Longitude'] = df['Longitude'].fillna(df.groupby('Province/State')['Longitude'].transform('mean'))
    return df


def us(data):
    states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
              'Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
              'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
              'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
              'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
              'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
              'New Jersey', 'New Mexico', 'New York', 'North Carolina',
              'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
              'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
              'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
              'West Virginia', 'Wisconsin', 'Wyoming', 'Recovered']
    df_us = data[data['Province/State'].isin(states)]
    # df_us = df_us.drop('Country/Region', axis=1)
    # df_us = df_us.rename(columns={'Province/State': 'Country/Region'})
    return df_us


def eu(data):
    eu = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium',
          'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus',
          'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France',
          'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy',
          'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg',
          'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands',
          'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania',
          'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden',
          'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom',
          'Vatican City']
    df_eu = data[data['Country/Region'].isin(eu)]
    df_eu = df_eu.groupby(['Country/Region'], as_index=False) \
        .agg({'Lat': 'mean',
              'Long': 'mean',
              'Confirmed': 'sum',
              'Latest confirmed': 'sum',
              'Deaths': 'sum',
              'Latest deaths': 'sum',
              'Recovered': 'sum',
              'Latest recovered': 'sum',
              'Active': 'sum',
              'Latest active': 'sum'})
    # df_eu = df_eu.append(pd.DataFrame({
    #     'date': [pd.to_datetime('2020-01-22'), pd.to_datetime('2020-01-23')],
    #     'Country/Region': ['France', 'France'],
    #     'Province/State': [np.nan, np.nan],
    #     'Confirmed': [0, 0],
    #     'Deaths': [0, 0],
    #     'Recovered': [0, 0],
    #     'Latitude': [np.nan, np.nan],
    #     'Longitude': [np.nan, np.nan],
    #     'Active': [0, 0]})).sort_index()
    return df_eu


def china(data):
    provinces = ['Anhui', 'Beijing', 'Chongqing', 'Fujian', 'Gansu', 'Guangdong',
                 'Guangxi', 'Guizhou', 'Hainan', 'Hebei', 'Heilongjiang', 'Henan',
                 'Hong Kong', 'Hubei', 'Hunan', 'Inner Mongolia', 'Jiangsu',
                 'Jiangxi', 'Jilin', 'Liaoning', 'Macau', 'Ningxia', 'Qinghai',
                 'Shaanxi', 'Shandong', 'Shanghai', 'Shanxi', 'Sichuan', 'Tianjin',
                 'Tibet', 'Xinjiang', 'Yunnan', 'Zhejiang']
    df_china = data[data['Province/State'].isin(provinces)]
    # df_china = df_china.drop('Country/Region', axis=1)
    # df_china = df_china.rename(columns={'Province/State': 'Country/Region'})
    return df_china


def df_move1st_tw(df_t):
    # Moving Singapore to the first row in the datatable
    df_t["new"] = range(1, len(df_t) + 1)
    df_t.loc[
        df_t[df_t['Country/Region'] == 'Taiwan'].index.values, 'new'] = 0
    df_t = df_t.sort_values("new").drop('new', axis=1)
    return df_t


def retrieve_data():
    ######################################
    # Retrieve data
    ######################################

    # get data directly from github. The data source provided by Johns Hopkins University.
    url_confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    url_deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
    url_recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

    df_confirmed = pd.read_csv(url_confirmed)
    df_deaths = pd.read_csv(url_deaths)
    df_recovered = pd.read_csv(url_recovered)

    df_confirmed = rename_coutries(df_confirmed)
    df_deaths = rename_coutries(df_deaths)
    df_recovered = rename_coutries(df_recovered)

    #########################################################################################
    # Data preprocessing for getting useful data and shaping data compatible to plotly plot
    #########################################################################################

    # Total cases
    df_confirmed_total = df_confirmed.iloc[:, 4:].sum(axis=0)
    df_deaths_total = df_deaths.iloc[:, 4:].sum(axis=0)
    df_recovered_total = df_recovered.iloc[:, 4:].sum(axis=0)

    # modified deaths dataset for mortality rate calculation
    df_deaths_confirmed = df_deaths.copy()
    df_deaths_confirmed['latest_confirmed'] = df_confirmed.iloc[:, -1]

    # Sorted - df_deaths_confirmed_sorted is different from others,
    # as it is only modified later. Careful of it dataframe structure
    df_deaths_confirmed_sorted = \
        df_deaths_confirmed.sort_values(by=df_deaths_confirmed.columns[-2],
                                        ascending=False)[['Country/Region', df_deaths_confirmed.columns[-2],
                                                          df_deaths_confirmed.columns[-1]]]
    df_recovered_sorted = \
        df_recovered.sort_values(by=df_recovered.columns[-1], ascending=False)[
            ['Country/Region', df_recovered.columns[-1]]]
    df_confirmed_sorted = \
        df_confirmed.sort_values(by=df_confirmed.columns[-1], ascending=False)[
            ['Country/Region', df_confirmed.columns[-1]]]

    # Single day increase
    df_deaths_confirmed_sorted['24hr'] = \
        df_deaths_confirmed_sorted.iloc[:, -2] - \
        df_deaths.sort_values(by=df_deaths.columns[-1],
                              ascending=False)[df_deaths.columns[-2]]

    df_recovered_sorted['24hr'] = \
        df_recovered_sorted.iloc[:, -1] - \
        df_recovered.sort_values(by=df_recovered.columns[-1],
                                 ascending=False)[df_recovered.columns[-2]]

    df_confirmed_sorted['24hr'] = \
        df_confirmed_sorted.iloc[:, -1] - \
        df_confirmed.sort_values(by=df_confirmed.columns[-1],
                                 ascending=False)[df_confirmed.columns[-2]]

    # Aggregate the countries with different province/state together
    df_deaths_confirmed_sorted_total = \
        df_deaths_confirmed_sorted.groupby('Country/Region').sum()
    df_deaths_confirmed_sorted_total = \
        df_deaths_confirmed_sorted_total \
        .sort_values(by=df_deaths_confirmed_sorted_total.columns[0],
                     ascending=False) \
        .reset_index()

    df_recovered_sorted_total = df_recovered_sorted.groupby(
        'Country/Region').sum()
    df_recovered_sorted_total = \
        df_recovered_sorted_total \
        .sort_values(by=df_recovered_sorted_total.columns[0],
                     ascending=False) \
        .reset_index()

    df_confirmed_sorted_total = df_confirmed_sorted.groupby(
        'Country/Region').sum()
    df_confirmed_sorted_total = \
        df_confirmed_sorted_total \
        .sort_values(by=df_confirmed_sorted_total.columns[0],
                     ascending=False) \
        .reset_index()

    # Modified recovery csv due to difference in number of rows.
    # Recovered will match ['Province/State','Country/Region']column with Confirmed ['Province/State','Country/Region']
    df_recovered['Province+Country'] = df_recovered[
        ['Province/State', 'Country/Region']].fillna('nann').agg('|'.join,
                                                                 axis=1)
    df_confirmed['Province+Country'] = df_confirmed[
        ['Province/State', 'Country/Region']].fillna('nann').agg('|'.join,
                                                                 axis=1)
    df_recovered_fill = df_recovered
    # df_recovered_fill.set_index("Province+Country")
    # df_recovered_fill \
    #     .set_index("Province+Country") \
    #     .reindex(df_confirmed['Province+Country'])
    df_recovered_fill = df_recovered_fill \
        .set_index("Province+Country") \
        .reindex(df_confirmed['Province+Country']) \
        .reset_index()

    # split Province+Country back into its respective columns
    new = df_recovered_fill["Province+Country"].str.split(
        "|", n=1, expand=True)
    df_recovered_fill['Province/State'] = new[0]
    df_recovered_fill['Country/Region'] = new[1]
    df_recovered_fill['Province/State'].replace('nann', 'NaN')

    # drop 'Province+Country' for all dataset
    df_confirmed.drop('Province+Country', axis=1, inplace=True)
    df_recovered.drop('Province+Country', axis=1, inplace=True)
    df_recovered_fill.drop('Province+Country', axis=1, inplace=True)

    # Data preprocessing for times series countries graph display
    # create temp to store sorting arrangement for all confirm, deaths and recovered.
    df_confirmed_sort_temp = df_confirmed.sort_values(
        by=df_confirmed.columns[-1],
        ascending=False)

    df_confirmed_t = df_move1st_tw(df_confirmed_sort_temp)
    df_confirmed_t['Province+Country'] = \
        df_confirmed_t[['Province/State', 'Country/Region']] \
        .fillna('nann').agg('|'.join, axis=1)
    df_confirmed_t = \
        df_confirmed_t.drop(['Province/State',
                             'Country/Region',
                             'Lat', 'Long'], axis=1).T

    df_deaths_t = df_deaths.reindex(df_confirmed_sort_temp.index)
    df_deaths_t = df_move1st_tw(df_deaths_t)
    df_deaths_t['Province+Country'] = \
        df_deaths_t[['Province/State', 'Country/Region']] \
        .fillna('nann').agg('|'.join, axis=1)
    df_deaths_t = df_deaths_t.drop(
        ['Province/State', 'Country/Region', 'Lat', 'Long'], axis=1).T

    # take note use reovered_fill df
    df_recovered_t = df_recovered_fill.reindex(df_confirmed_sort_temp.index)
    df_recovered_t = df_move1st_tw(df_recovered_t)
    df_recovered_t['Province+Country'] = \
        df_recovered_t[['Province/State', 'Country/Region']] \
        .fillna('nann').agg('|'.join, axis=1)
    df_recovered_t = \
        df_recovered_t.drop(['Province/State',
                             'Country/Region',
                             'Lat', 'Long'], axis=1).T

    df_confirmed_t.columns = df_confirmed_t.iloc[-1]
    df_confirmed_t = df_confirmed_t.drop('Province+Country')

    df_deaths_t.columns = df_deaths_t.iloc[-1]
    df_deaths_t = df_deaths_t.drop('Province+Country')

    df_recovered_t.columns = df_recovered_t.iloc[-1]
    df_recovered_t = df_recovered_t.drop('Province+Country')

    df_confirmed_t.index = pd.to_datetime(df_confirmed_t.index)
    df_deaths_t.index = pd.to_datetime(df_confirmed_t.index)
    df_recovered_t.index = pd.to_datetime(df_confirmed_t.index)

    # Highest 10 plot data preprocessing
    # getting highest 10 countries with confirmed case
    name = df_confirmed_t.columns.str.split("|", 1)
    df_confirmed_t_namechange = df_confirmed_t.copy()
    # name0 = [x[0] for x in name]
    name1 = [x[1] for x in name]
    df_confirmed_t_namechange.columns = name1
    df_confirmed_t_namechange = \
        df_confirmed_t_namechange \
        .groupby(df_confirmed_t_namechange.columns, axis=1) \
        .sum()
    df_confirmed_t_namechange10 = \
        df_confirmed_t_namechange \
        .sort_values(by=df_confirmed_t_namechange.index[-1],
                     axis=1, ascending=False) \
        .iloc[:, :10]
    df_confirmed_t_stack = df_confirmed_t_namechange10.stack()
    df_confirmed_t_stack = df_confirmed_t_stack.reset_index(level=[0, 1])
    df_confirmed_t_stack.rename(columns={"level_0": "Date",
                                         'level_1': 'Countries',
                                         0: "Confirmed"},
                                inplace=True)

    # getting highest 10 countries with deceased case
    name = df_deaths_t.columns.str.split("|", 1)
    df_deaths_t_namechange = df_deaths_t.copy()
    # name0 = [x[0] for x in name]
    name1 = [x[1] for x in name]
    df_deaths_t_namechange.columns = name1
    df_deaths_t_namechange = \
        df_deaths_t_namechange \
        .groupby(df_deaths_t_namechange.columns, axis=1) \
        .sum()
    df_deaths_t_namechange10 = \
        df_deaths_t_namechange \
        .sort_values(by=df_deaths_t_namechange.index[-1],
                     axis=1, ascending=False) \
        .iloc[:, :10]
    df_deaths_t_stack = df_deaths_t_namechange10.stack()
    df_deaths_t_stack = df_deaths_t_stack.reset_index(level=[0, 1])
    df_deaths_t_stack.rename(columns={"level_0": "Date",
                                      'level_1': 'Countries',
                                      0: "Deceased"},
                             inplace=True)

    # Recreate required columns for map data
    map_data = df_confirmed[["Province/State",
                             "Country/Region", "Lat", "Long"]]
    map_data['Confirmed'] = df_confirmed.loc[:, df_confirmed.columns[-1]]
    map_data['Deaths'] = df_deaths.loc[:, df_deaths.columns[-1]]
    map_data['Recovered'] = \
        df_recovered_fill.loc[:, df_recovered_fill.columns[-1]]
    # too covert value back to int and fillna with zero
    map_data['Recovered'] = map_data['Recovered'] \
        .fillna(0) \
        .astype(int)

    # Active cases
    map_data['Active'] = map_data['Confirmed'] - \
        map_data['Deaths'] - map_data['Recovered']

    # last 24 hours increase
    map_data['Deaths_24hr'] = df_deaths.iloc[:, -1] - df_deaths.iloc[:, -2]
    map_data['Recovered_24hr'] = \
        df_recovered_fill.iloc[:, -1] - df_recovered_fill.iloc[:, -2]
    map_data['Confirmed_24hr'] = \
        df_confirmed.iloc[:, -1] - df_confirmed.iloc[:, -2]
    map_data['Latest active'] = map_data['Confirmed_24hr'] \
        - map_data['Deaths_24hr'] \
        - map_data['Recovered_24hr']
    map_data.sort_values(by='Confirmed', ascending=False, inplace=True)
    # Moving Singapore to the first row in the datatable
    map_data["new"] = range(1, len(map_data) + 1)
    map_data.loc[map_data[map_data['Country/Region'] == 'Taiwan']
                 .index.values, 'new'] = 0
    map_data = map_data.sort_values("new").drop('new', axis=1)

    map_data = map_data.rename(columns={'Confirmed_24hr': 'Latest confirmed',
                                        'Deaths_24hr': 'Latest deaths',
                                        'Recovered_24hr': 'Latest recovered'})

    map_data_us = us(map_data)
    map_data_eu = eu(map_data)
    map_data_china = china(map_data)

    return df_deaths_confirmed_sorted_total, \
        df_confirmed, \
        df_deaths_total, \
        df_confirmed_total, \
        df_recovered_total, \
        df_confirmed_t, \
        df_deaths_t, \
        df_recovered_t, \
        df_confirmed_sorted_total, \
        df_confirmed_t_stack, \
        df_deaths_t_stack, \
        map_data_us, \
        map_data_eu, \
        map_data_china, \
        map_data

# if __name__ == '__main__':
