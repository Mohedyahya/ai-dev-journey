# Day 17 - Smart Agent Project: Workflow Automation
import requests
import time
import json
from datetime import datetime

print("=" * 55)
print("🤖 SMART AGENT: Workflow Automation System")
print("=" * 55)

# ========== الإعدادات ==========
AGENT_URL = "http://localhost:5000/chat"
LOG_FILE = "workflow_log.txt"

def send_to_agent(message):
    """
    يرسل رسالة للوكيل (Flask) ويستلم الرد
    إذا الوكيل مو شغال، يرجع خطأ ويكمل بدونه
    """
    try:
        response = requests.post(
            AGENT_URL,
            data={"message": message},
            timeout=10
        )
        return "✅ SUCCESS: Agent replied"
    except Exception as e:
        return "⚠️ OFFLINE: " + str(e)

def log_task(task_name, result):
    """
    يكتب سجل في ملف نصي بتاريخ ووقت كل عملية
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] TASK: {task_name} | RESULT: {result}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)
    print(f"   📝 Logged to {LOG_FILE}")

def workflow_welcome():
    """مهمة 1: ترحيب العملاء الجدد"""
    print("\n📋 TASK 1: Welcome New Customers")
    result = send_to_agent("Welcome new customers")
    print(f"   {result}")
    log_task("Welcome New Customers", result)

def workflow_report():
    """مهمة 2: توليد تقرير يومي"""
    print("\n📋 TASK 2: Generate Daily Report")
    result = send_to_agent("Generate daily sales report")
    print(f"   {result}")
    log_task("Generate Daily Report", result)

def workflow_check_orders():
    """مهمة 3: فحص الطلبات المتأخرة"""
    print("\n📋 TASK 3: Check Pending Orders")
    result = send_to_agent("Check pending orders")
    print(f"   {result}")
    log_task("Check Pending Orders", result)

def workflow_followup():
    """مهمة 4: إرسال متابعة للعملاء"""
    print("\n📋 TASK 4: Send Follow-up Messages")
    result = send_to_agent("Send follow-up to customers")
    print(f"   {result}")
    log_task("Send Follow-up", result)

# ========== تشغيل سير العمل ==========
print("\n🚀 Starting Automated Workflow...")
print("-" * 55)

# تشغيل المهام بالتسلسل
workflow_welcome()
time.sleep(2)

workflow_report()
time.sleep(2)

workflow_check_orders()
time.sleep(2)

workflow_followup()

print("\n" + "=" * 55)
print("🎉 WORKFLOW COMPLETE!")
print(f"📄 Check log: {LOG_FILE}")
print("=" * 55)

