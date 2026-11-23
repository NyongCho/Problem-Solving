def main():
    T = int(input())

    for t in range(T):
        memory = list(input())
        cnt = 0
        p = '0'
        if memory[0] == '1':
            cnt =  1
            p = '1'

        for i in range(1, len(memory)):
            if p != memory[i]:
                cnt += 1
            p = memory[i]

        print(f'#{t+1} {cnt}')

if __name__ == "__main__":
    main()