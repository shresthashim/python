import speedtest

# Create a Speedtest object
test = speedtest.Speedtest()

# Get the best server based on ping
test.get_best_server()

# Measure download speed
download = test.download() / 1_000_000  # Convert from bits per second to Mbps

# Measure upload speed
upload = test.upload() / 1_000_000  # Convert from bits per second to Mbps

# Measure ping
ping = test.results.ping

# Print the results
print(f"Download Speed: {download:.2f} Mbps")
print(f"Upload Speed: {upload:.2f} Mbps")
print(f"Ping: {ping} ms")
