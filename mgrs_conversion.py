import pandas as pd
import mgrs

def convert_mgrs_to_latlon(file_path):
    # Initialize MGRS converter
    converter = mgrs.MGRS()

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    lat_list, lon_list = [], []

    # Convert MGRS to geographic coordinates
    for coord in df['MGRS']:
        lat, lon = converter.toLatLon(coord)
        lat_list.append(lat)
        lon_list.append(lon)

    # Append latitude and longitude columns to the DataFrame
    df['Latitude'] = lat_list
    df['Longitude'] = lon_list
    
    # Display the updated DataFrame in the output
    print(df)

    # Save the updated DataFrame to a new CSV file
    df.to_csv('converted_coordinates.csv', index=False)

# Provide the path to the CSV file that contains the 'MGRS' column
convert_mgrs_to_latlon("/spartan_confusion/MGRS_sample_data.csv")

