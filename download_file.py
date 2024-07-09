import gdown

# Replace with your file ID
file_id = '1evaM2R9ebZuR1U7NxUgdQPorvXG5GN1JsGp2pMaEc2Q'
url = f'https://drive.google.com/uc?id=1evaM2R9ebZuR1U7NxUgdQPorvXG5GN1JsGp2pMaEc2Q'

# Download the file
gdown.download(url, 'downloaded_file_name', quiet=False)
