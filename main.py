from pyhomebroker import HomeBroker

def main():
    hb = HomeBroker()
    instruments = hb.get_instruments()
    
    for i in instruments[:10]:  # Mostramos solo los primeros 10
        print(f"{i['symbol']} - {i['description']}")

if __name__ == "__main__":
    main()
