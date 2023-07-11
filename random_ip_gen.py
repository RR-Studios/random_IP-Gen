import random

def generate_random_ip():
    ip_parts = []
    for _ in range(4):
        ip_parts.append(str(random.randint(0, 255)))
    return ".".join(ip_parts)

# Generate a random IP address
random_ip = generate_random_ip()
print(random_ip)
