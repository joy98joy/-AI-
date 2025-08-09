# import random

# class DummySensor:
    
#     def __init__(self):
        
#         self.env_values = {
#             "mars_base_internal_temperature": 0.0,
#             "mars_base_external_temperature": 0.0,
#             "mars_base_internal_humidity": 0.0,
#             "mars_base_external_illuminance": 0.0,
#             "mars_base_internal_co2": 0.0,
#             "mars_base_internal_oxygen": 0.0,
#         }

#     def set_env(self):
#         """
#         각 환경 항목에 대해 지정된 범위 내의 랜덤 값을 생성하여 env_values에 설정합니다.
#         """
#         self.env_values["mars_base_internal_temperature"] = round(random.uniform(18.0, 30.0), 2)
#         self.env_values["mars_base_external_temperature"] = round(random.uniform(0.0, 21.0), 2)
#         self.env_values["mars_base_internal_humidity"] = round(random.uniform(50.0, 60.0), 2)
#         self.env_values["mars_base_external_illuminance"] = round(random.uniform(500.0, 715.0), 2)
#         self.env_values["mars_base_internal_co2"] = round(random.uniform(0.02, 0.1), 3)
#         self.env_values["mars_base_internal_oxygen"] = round(random.uniform(4.0, 7.0), 2)

#     def get_env(self):
#         """
#         env_values 딕셔너리를 반환합니다.
#         """
#         return self.env_values

# # DummySensor 클래스의 인스턴스 생성
# ds = DummySensor()

# # set_env() 메소드를 호출하여 env_values에 랜덤 값 설정
# ds.set_env()

# # get_env() 메소드를 호출하여 설정된 값을 확인하고 출력
# current_env_data = ds.get_env()
# print("현재 환경 데이터:")
# for key, value in current_env_data.items():
#     print(f"{key}: {value}")
import random
import time
import json
from datetime import datetime

# DummySensor 클래스 (문제 3에서 제작된 클래스)
class DummySensor:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": 0.0,
            "mars_base_external_temperature": 0.0,
            "mars_base_internal_humidity": 0.0,
            "mars_base_external_illuminance": 0.0,
            "mars_base_internal_co2": 0.0,
            "mars_base_internal_oxygen": 0.0,
        }

    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = round(random.uniform(18.0, 30.0), 2)
        self.env_values["mars_base_external_temperature"] = round(random.uniform(0.0, 21.0), 2)
        self.env_values["mars_base_internal_humidity"] = round(random.uniform(50.0, 60.0), 2)
        self.env_values["mars_base_external_illuminance"] = round(random.uniform(500.0, 715.0), 2)
        self.env_values["mars_base_internal_co2"] = round(random.uniform(0.02, 0.1), 3)
        self.env_values["mars_base_internal_oxygen"] = round(random.uniform(4.0, 7.0), 2)

    def get_env(self):
        return self.env_values

# MissionComputer 클래스
class MissionComputer:
    """
    미션 컴퓨터 클래스.
    DummySensor에서 데이터를 받아와 저장하고 JSON 형태로 출력합니다.
    """
    def __init__(self):
        """
        MissionComputer 클래스의 생성자.
        env_values 딕셔너리를 초기화하고 DummySensor 인스턴스를 생성합니다.
        """
        self.env_values = {
            "mars_base_internal_temperature": 0.0,
            "mars_base_external_temperature": 0.0,
            "mars_base_internal_humidity": 0.0,
            "mars_base_external_illuminance": 0.0,
            "mars_base_internal_co2": 0.0,
            "mars_base_internal_oxygen": 0.0,
        }
        self.ds = DummySensor()

    def get_sensor_data(self):
        """
        DummySensor에서 데이터를 가져와 env_values에 저장하고
        JSON 형태로 출력하는 작업을 5초마다 반복합니다.
        """
        while True:
            # 1. 센서의 값을 가져와서 env_values에 담기
            self.ds.set_env()
            self.env_values = self.ds.get_env()

            # 2. env_values의 값을 JSON 형태로 출력하기
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"--- 환경 데이터 수신 ({now}) ---")
            print(json.dumps(self.env_values, indent=4))
            print("-" * 35)

            # 3. 5초에 한 번씩 반복하기
            time.sleep(5)

# MissionComputer 클래스를 RunComputer라는 이름으로 인스턴스화
RunComputer = MissionComputer()

# RunComputer 인스턴스의 get_sensor_data() 메소드 호출
try:
    RunComputer.get_sensor_data()
except KeyboardInterrupt:
    print("\n미션 컴퓨터 프로그램이 종료되었습니다.")


import platform
import psutil
import json
import time

class MissionComputer:
    """
    미션 컴퓨터 클래스.
    시스템 정보를 확인하고 부하를 모니터링하는 기능을 추가했습니다.
    """

    def __init__(self):
        """
        MissionComputer 클래스의 생성자.
        """
        pass

    def get_mission_computer_info(self):
        """
        미션 컴퓨터의 시스템 정보를 가져와 JSON 형식으로 출력합니다.
        """
        info = {
            "운영체계": platform.system(),
            "운영체계 버전": platform.version(),
            "CPU 타입": platform.processor(),
            "CPU 코어 수": psutil.cpu_count(logical=False),
            "메모리 크기 (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2)
        }
        print("--- 미션 컴퓨터 시스템 정보 ---")
        print(json.dumps(info, indent=4, ensure_ascii=False))
        print("-" * 30)
        return info

    def get_mission_computer_load(self):
        """
        미션 컴퓨터의 실시간 부하 정보를 가져와 JSON 형식으로 출력합니다.
        """
        load = {
            "CPU 실시간 사용량 (%)": psutil.cpu_percent(interval=1),
            "메모리 실시간 사용량 (%)": psutil.virtual_memory().percent
        }
        print("--- 미션 컴퓨터 실시간 부하 ---")
        print(json.dumps(load, indent=4, ensure_ascii=False))
        print("-" * 30)
        return load

# MissionComputer 클래스를 runComputer라는 이름으로 인스턴스화
runComputer = MissionComputer()

# 시스템 정보 가져오기 및 출력
runComputer.get_mission_computer_info()

# 실시간 부하 정보 가져오기 및 출력
# 3초 동안 1초 간격으로 실시간 부하를 측정하여 출력
for _ in range(3):
    runComputer.get_mission_computer_load()
    time.sleep(1)


#멀티 쓰레딩을 사용하여 구현

import threading
import time
import json
import random
import psutil
import platform
from datetime import datetime

# DummySensor 클래스 (이전 문제에서 작성된 클래스)
class DummySensor:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": 0.0,
            "mars_base_external_temperature": 0.0,
            "mars_base_internal_humidity": 0.0,
            "mars_base_external_illuminance": 0.0,
            "mars_base_internal_co2": 0.0,
            "mars_base_internal_oxygen": 0.0,
        }

    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = round(random.uniform(18.0, 30.0), 2)
        self.env_values["mars_base_external_temperature"] = round(random.uniform(0.0, 21.0), 2)
        self.env_values["mars_base_internal_humidity"] = round(random.uniform(50.0, 60.0), 2)
        self.env_values["mars_base_external_illuminance"] = round(random.uniform(500.0, 715.0), 2)
        self.env_values["mars_base_internal_co2"] = round(random.uniform(0.02, 0.1), 3)
        self.env_values["mars_base_internal_oxygen"] = round(random.uniform(4.0, 7.0), 2)

    def get_env(self):
        return self.env_values

# MissionComputer 클래스
class MissionComputer:
    def __init__(self):
        self.ds = DummySensor()

    def get_sensor_data(self):
        while True:
            self.ds.set_env()
            env_data = self.ds.get_env()
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[Thread-Sensor] 환경 데이터 수신 ({now})")
            print(json.dumps(env_data, indent=4))
            time.sleep(5)

    def get_mission_computer_info(self):
        while True:
            info = {
                "운영체계": platform.system(),
                "운영체계 버전": platform.version(),
                "CPU 타입": platform.processor(),
                "CPU 코어 수": psutil.cpu_count(logical=False),
                "메모리 크기 (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2)
            }
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[Thread-Info] 시스템 정보 수신 ({now})")
            print(json.dumps(info, indent=4, ensure_ascii=False))
            time.sleep(20)

    def get_mission_computer_load(self):
        while True:
            load = {
                "CPU 실시간 사용량 (%)": psutil.cpu_percent(interval=1),
                "메모리 실시간 사용량 (%)": psutil.virtual_memory().percent
            }
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[Thread-Load] 실시간 부하 수신 ({now})")
            print(json.dumps(load, indent=4, ensure_ascii=False))
            time.sleep(20)

# MissionComputer 클래스를 runComputer 인스턴스화
runComputer = MissionComputer()

# 각 메서드를 위한 쓰레드 생성
thread_sensor = threading.Thread(target=runComputer.get_sensor_data, daemon=True)
thread_info = threading.Thread(target=runComputer.get_mission_computer_info, daemon=True)
thread_load = threading.Thread(target=runComputer.get_mission_computer_load, daemon=True)

# 쓰레드 시작
thread_sensor.start()
thread_info.start()
thread_load.start()

# 메인 쓰레드가 종료되지 않도록 무한 루프
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n프로그램을 종료합니다.")
#멀티 프로세싱을 사용하여 구현
import multiprocessing
import time
import json
import random
import psutil
import platform
from datetime import datetime

# DummySensor 클래스 (이전 문제에서 작성된 클래스)
class DummySensor:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": 0.0,
            "mars_base_external_temperature": 0.0,
            "mars_base_internal_humidity": 0.0,
            "mars_base_external_illuminance": 0.0,
            "mars_base_internal_co2": 0.0,
            "mars_base_internal_oxygen": 0.0,
        }

    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = round(random.uniform(18.0, 30.0), 2)
        self.env_values["mars_base_external_temperature"] = round(random.uniform(0.0, 21.0), 2)
        self.env_values["mars_base_internal_humidity"] = round(random.uniform(50.0, 60.0), 2)
        self.env_values["mars_base_external_illuminance"] = round(random.uniform(500.0, 715.0), 2)
        self.env_values["mars_base_internal_co2"] = round(random.uniform(0.02, 0.1), 3)
        self.env_values["mars_base_internal_oxygen"] = round(random.uniform(4.0, 7.0), 2)

    def get_env(self):
        return self.env_values

# MissionComputer 클래스
class MissionComputer:
    def __init__(self):
        self.ds = DummySensor()

    def get_sensor_data(self):
        while True:
            self.ds.set_env()
            env_data = self.ds.get_env()
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[Process-Sensor] 환경 데이터 수신 ({now})")
            print(json.dumps(env_data, indent=4))
            time.sleep(5)

    def get_mission_computer_info(self):
        while True:
            info = {
                "운영체계": platform.system(),
                "운영체계 버전": platform.version(),
                "CPU 타입": platform.processor(),
                "CPU 코어 수": psutil.cpu_count(logical=False),
                "메모리 크기 (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2)
            }
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[Process-Info] 시스템 정보 수신 ({now})")
            print(json.dumps(info, indent=4, ensure_ascii=False))
            time.sleep(20)

    def get_mission_computer_load(self):
        while True:
            load = {
                "CPU 실시간 사용량 (%)": psutil.cpu_percent(interval=1),
                "메모리 실시간 사용량 (%)": psutil.virtual_memory().percent
            }
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[Process-Load] 실시간 부하 수신 ({now})")
            print(json.dumps(load, indent=4, ensure_ascii=False))
            time.sleep(20)

if __name__ == '__main__':
    # 3개의 MissionComputer 인스턴스 생성
    runComputer1 = MissionComputer()
    runComputer2 = MissionComputer()
    runComputer3 = MissionComputer()

    # 각 인스턴스의 메서드를 위한 프로세스 생성
    process_sensor = multiprocessing.Process(target=runComputer1.get_sensor_data, daemon=True)
    process_info = multiprocessing.Process(target=runComputer2.get_mission_computer_info, daemon=True)
    process_load = multiprocessing.Process(target=runComputer3.get_mission_computer_load, daemon=True)

    # 프로세스 시작
    process_sensor.start()
    process_info.start()
    process_load.start()

    # 메인 프로세스가 종료되지 않도록 무한 루프
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")

# import random
# from datetime import datetime

# class DummySensor:
#     """
#     더미 센서 클래스.
#     환경 데이터를 시뮬레이션하기 위해 랜덤 값을 생성합니다.
#     """
#     def __init__(self):
#         """
#         DummySensor 클래스의 생성자.
#         env_values 딕셔너리를 초기화합니다.
#         """
#         self.env_values = {
#             "mars_base_internal_temperature": 0.0,
#             "mars_base_external_temperature": 0.0,
#             "mars_base_internal_humidity": 0.0,
#             "mars_base_external_illuminance": 0.0,
#             "mars_base_internal_co2": 0.0,
#             "mars_base_internal_oxygen": 0.0,
#         }
#         self.log_file = "sensor_log.txt"

    

#     def set_env(self):
#         """
#         각 환경 항목에 대해 지정된 범위 내의 랜덤 값을 생성하여 env_values에 설정합니다.
#         """
#         self.env_values["mars_base_internal_temperature"] = round(random.uniform(18.0, 30.0), 2)
#         self.env_values["mars_base_external_temperature"] = round(random.uniform(0.0, 21.0), 2)
#         self.env_values["mars_base_internal_humidity"] = round(random.uniform(50.0, 60.0), 2)
#         self.env_values["mars_base_external_illuminance"] = round(random.uniform(500.0, 715.0), 2)
#         self.env_values["mars_base_internal_co2"] = round(random.uniform(0.02, 0.1), 3)
#         self.env_values["mars_base_internal_oxygen"] = round(random.uniform(4.0, 7.0), 2)

#     def get_env(self):
#         """
#         env_values 딕셔너리를 반환하고, 동시에 로그 파일에 데이터를 기록합니다.
#         """
#         now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         log_data = (
#             f"{now},"
#             f"{self.env_values['mars_base_internal_temperature']},"
#             f"{self.env_values['mars_base_external_temperature']},"
#             f"{self.env_values['mars_base_internal_humidity']},"
#             f"{self.env_values['mars_base_external_illuminance']},"
#             f"{self.env_values['mars_base_internal_co2']},"
#             f"{self.env_values['mars_base_internal_oxygen']}\n"
#         )
        
#         with open(self.log_file, "a", encoding="utf-8") as f:
#             f.write(log_data)
        
#         return self.env_values

# # DummySensor 클래스의 인스턴스 생성
# ds = DummySensor()

# print("랜덤 데이터를 생성하고 로그 파일에 기록합니다.")
# for i in range(5):
#     ds.set_env()
#     current_env_data = ds.get_env()
#     print(f"데이터 기록 완료: {current_env_data}")
