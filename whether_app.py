class LatitudeLongitude():
    def __init__(self):
        pass
    def main(self, args):
        import requests
        url = fr"http://api.openweathermap.org/geo/1.0/direct?q={args}&limit=1&appid=62ef109200f3637a5121ee0dd4c91736"

        response = requests.get(url)
        data = response.json()

        lat = data[0]["lat"]
        lon = data[0]["lon"]
        return lat, lon
    
result = LatitudeLongitude()
# city = input("Enter city name> ")
lat, lon = result.main("mumbai")
print(f"Lat: {lat}, Lon: {lon}")
    

