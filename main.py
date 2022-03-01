from patcher import Patcher

patcher = Patcher()

print("리스크 오브 레인 2 번역 수정 패쳐에 오신 것을 환영합니다!")
print()
print("실행할 작업을 선택하세요.")
print("1. 패치  2. 되돌리기")
print()

while True:
    action = int(input("> "))

    if action not in [1, 2]:
        print("입력이 올바르지 않습니다.")
        continue
    else:
        break

print()

if action == 1:
    patcher.backup()
    patcher.download()
else:
    patcher.revert()

print()
print("모두 완료.")
print("계속하려면 아무 키나 누르십시오...")
input()