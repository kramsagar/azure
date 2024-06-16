import requests
import xml.etree.ElementTree as ET

# URL to list blobs in the Azure Blob Storage directory
url = "https://saaccountbyram.blob.core.windows.net/tempfiles?restype=directory&comp=list"

# Send GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML response
    root = ET.fromstring(response.content)

    # Extract blob names (file names)
    blob_names = [blob.find('Name').text for blob in root.findall('.//Blob')]

    # Generate HTML content to display images
    html_content = "<html><body>\n"
    for blob_name in blob_names:
        image_url = f"https://saaccountbyram.blob.core.windows.net/tempfiles/{blob_name}"
        html_content += f'<img src="{image_url}" alt="{blob_name}" style="max-width: 100%; height: auto;"><br>\n'
    html_content += "</body></html>"

    # Write HTML content to a file
    with open("images.html", "w") as file:
        file.write(html_content)

    print("HTML file 'images.html' created successfully.")
else:
    print("Failed to retrieve the list of blobs.")
