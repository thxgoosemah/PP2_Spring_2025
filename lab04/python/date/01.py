from datetime import datetime, timedelta
current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print(f"Five days ago: {five_days_ago.strftime('%Y-%m-%d %H:%M:%S')}") 
