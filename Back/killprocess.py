import subprocess

# اجرای دستور lsof برای یافتن پردازه‌های مرتبط با پورت 5432
command = "sudo lsof -i :80"
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE,\
                        stderr=subprocess.PIPE, text=True)

if result.returncode == 0:
    # پردازه‌های مرتبط با پورت 5432 یافت شده‌اند
    # جداگانه هر خط را بررسی کرده و پیدا کرده شده‌ی PID را ببندیم
    lines = result.stdout.split('\n')
    for line in lines:
        if "LISTEN" in line:
            pid = line.split()[1]
            # بستن پردازه با دستور kill
            kill_command = f"sudo kill {pid}"
            subprocess.run(kill_command, shell=True)
        else:
            print("پورت 80 در حال استفاده نیست.")
else:
    print("هیچ پردازه‌ای برای پورت 80 یافت نشد یا دسترسی لازم نیست.")


