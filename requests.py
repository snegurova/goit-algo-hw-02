"""Module providing a function generating requests."""
import queue
import time
import random

# Create requests queue
request_queue = queue.Queue()

def generate_request():
    """Function generating request"""
    request_id = random.randint(1000, 9999)
    print(f"New request has been created with ID: {request_id}")
    request_queue.put(request_id)

def process_request():
    """Function processing requests"""
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Request ID: {request_id} is being processed")
    else:
        print("Queue is empty")

def main():
    """Main cycle"""
    while True:
        user_input = input("Please press Enter to generate new request or 'q' to quit: ") \
            .strip().lower()
        if user_input == 'q':
            break
        generate_request()
        process_request()
        time.sleep(1)

if __name__ == "__main__":
    main()
