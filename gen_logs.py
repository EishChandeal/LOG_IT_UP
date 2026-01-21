import random
import datetime

# Configuration
output_file = "server.log"
num_lines = 100000  # Start with 100k lines (approx 5-10MB)

ip_addresses = ["192.168.1.1", "10.0.0.1", "172.16.0.5", "192.168.0.10"]
endpoints = ["/home", "/login", "/dashboard", "/api/data", "/images/logo.png"]
status_codes = [200, 201, 400, 401, 404, 500]

print(f"Generating {num_lines} lines...")

# with open(output_file, "w") as f:
#     for _ in range(num_lines):
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         ip = random.choice(ip_addresses)
#         endpoint = random.choice(endpoints)
#         status = random.choice(status_codes)
        
#         # Log Format: [TIMESTAMP] INFO - IP - METHOD ENDPOINT - STATUS
#         log_line = f"[{timestamp}] INFO - {ip} - GET {endpoint} - {status}\n"
#         f.write(log_line)

print("Done! 'server.log' created.")
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(type(timestamp))