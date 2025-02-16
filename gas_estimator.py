import requests

# Replace with your own Etherscan API Key (Get it free from https://etherscan.io/apis)
ETHERSCAN_API_KEY = "Your_API_Key_Here"

# API URL to fetch gas price
ETHERSCAN_URL = f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={ETHERSCAN_API_KEY}"

def get_gas_fees():
    try:
        response = requests.get(ETHERSCAN_URL)
        data = response.json()
        
        if data["status"] == "1":
            print("🚀 Ethereum Gas Fees 🚀")
            print(f"🔹 Low: {data['result']['SafeGasPrice']} Gwei")
            print(f"🔸 Average: {data['result']['ProposeGasPrice']} Gwei")
            print(f"🔥 High: {data['result']['FastGasPrice']} Gwei")
        else:
            print("❌ Error fetching gas fees:", data["message"])
    except Exception as e:
        print("❌ Error:", str(e))

# Run the function
get_gas_fees()
