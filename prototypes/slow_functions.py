def main():
    n = 30000
    a = range(n)

    for i in a:
        if i > 1:
            a[i-1] = i+1
            
if __name__ == "__main__":
    main()