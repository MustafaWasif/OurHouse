import Client

def Location():
   location = []
   location.append("1695 Sheridan Avenue")
   x= Client.signup()
   print(x)
   for house_addresses in location:
      print(house_addresses)

   return location

if __name__ == "__main__":
   Location()

