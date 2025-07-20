# test_network.py
import requests

TARGET_URL = "https://www.google.com"

print("--- Network Connectivity Test ---")
print(f"Attempting to connect to: {TARGET_URL}")
print("---------------------------------")

try:
    # We set a timeout to prevent it from hanging.
    response = requests.get(TARGET_URL, timeout=10)
    response.raise_for_status() # This will raise an error if the status code is bad

    print("\n✅ SUCCESS!")
    print(f"Successfully connected to {TARGET_URL}. Status Code: {response.status_code}")
    print("This means your Python environment CAN connect to the internet.")

except requests.exceptions.ProxyError as e:
    print("\n--- ❌ TEST FAILED: Proxy Error ---")
    print("This is the problem. Your computer is on a network (like a corporate or university network) that requires a proxy.")
    print("Your web browser uses it automatically, but Python does not.")
    print("\nError details:", e)

except requests.exceptions.SSLError as e:
    print("\n--- ❌ TEST FAILED: SSL Error ---")
    print("This is the problem. It's a common issue on corporate networks that inspect traffic.")
    print("It means we need to configure Python to trust your network's security certificates.")
    print("\nError details:", e)

except requests.exceptions.ConnectTimeout as e:
    print("\n--- ❌ TEST FAILED: Connection Timeout ---")
    print("This is the problem. A firewall or antivirus is blocking Python silently.")
    print("You need to add an 'allow rule' or 'exception' for python.exe in your security software.")
    print("\nError details:", e)

except requests.exceptions.ConnectionError as e:
    print("\n--- ❌ TEST FAILED: General Connection Error ---")
    print("This is the problem. It could be a DNS issue or a general network block.")
    print("\nError details:", e)

except Exception as e:
    print(f"\n--- ❌ TEST FAILED: An Unexpected Error ---")
    print("An unexpected error happened. Please share the full message below.")
    print("\nError details:", e)