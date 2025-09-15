import schedule
import time

def send_daily_report():
    print("Sending daily report...")
    # Your notification logic here

def run_processes():
    # change for calibration of plant care processes
    schedule.every().day.at("09:00").do(send_daily_report)
    schedule.every().day.at("18:00").do(send_daily_report)

    # Check and run scheduled jobs (non-blocking)
    schedule.run_pending()
