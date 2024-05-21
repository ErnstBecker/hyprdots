import psutil
import json


class SystemMonitor:
  def monitor(self):
    memory_usage = psutil.virtual_memory().percent
    cpu_usage = psutil.cpu_percent(interval=1)
    data = {
      "text": f"  {cpu_usage}%      {memory_usage}%",
      "class": "custom-system-monitor",
      "tooltip": "System Monitor"
    }
    return data


def main():
  monitor = SystemMonitor()
  data = monitor.monitor()
  print(json.dumps(data))


if __name__ == "__main__":
  main()
