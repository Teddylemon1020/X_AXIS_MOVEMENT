import movement
import processes
import time 
import schedule
if __name__ == "__main__":
    while True:
        # Step 1: Movement
        movement.run_movement()
        
        # Step 2: Processes (watering, lighting, notifications)
        processes.run_processes()

        schedule.run_pending()
        
        # Optional: small delay between cycles to avoid CPU overuse
        time.sleep(1)  # 1 second pause, adjust as needed